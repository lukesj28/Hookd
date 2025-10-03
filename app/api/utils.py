from typing import Optional
import time

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import SecurityScopes, HTTPAuthorizationCredentials, HTTPBearer

from app.api.config import get_settings


class UnauthorizedException(HTTPException):
    def __init__(self, detail: str, **kwargs):
        super().__init__(status.HTTP_403_FORBIDDEN, detail=detail)


class UnauthenticatedException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Requires authentication"
        )


class VerifyToken:
    def __init__(self):
        self.config = get_settings()

        jwks_url = f'https://{self.config.auth0_domain}/.well-known/jwks.json'
        self.jwks_client = jwt.PyJWKClient(jwks_url)

    async def verify(self,
                     security_scopes: SecurityScopes,
                     token: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer())
                     ):
        if token is None:
            raise UnauthenticatedException

        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(
                token.credentials
            ).key
        except jwt.exceptions.PyJWKClientError as error:
            raise UnauthorizedException(str(error))
        except jwt.exceptions.DecodeError as error:
            raise UnauthorizedException(str(error))

        decode_options = {"require": ["exp", "iat"]}
        try:
            payload = jwt.decode(
                token.credentials,
                signing_key,
                algorithms=self.config.auth0_algorithms,
                audience=self.config.auth0_api_audience,
                issuer=self.config.auth0_issuer,
                options=decode_options,
                leeway=self.config.auth0_leeway,
            )
        except jwt.ExpiredSignatureError:
            raise UnauthorizedException("Token expired")
        except jwt.InvalidAudienceError:
            raise UnauthorizedException("Invalid audience")
        except jwt.InvalidIssuerError:
            raise UnauthorizedException("Invalid issuer")
        except jwt.InvalidIssuedAtError:
            raise UnauthorizedException("Invalid 'iat' in token")
        except jwt.ImmatureSignatureError:
            raise UnauthorizedException("Token is not yet valid (nbf)")
        except jwt.PyJWTError as error:
            raise UnauthorizedException(str(error))

        iat = payload.get("iat")
        if not isinstance(iat, (int, float)):
            raise UnauthorizedException("Missing or invalid iat claim")
        now = time.time()
        if (now - float(iat)) > self.config.auth0_max_token_age:
            raise UnauthorizedException("Token is too old")

        return payload
