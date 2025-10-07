from fastapi import FastAPI
from app.routers import users, follows, posts, likes

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(follows.router, prefix="/follows", tags=["follows"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(likes.router, prefix="/likes", tags=["likes"])
