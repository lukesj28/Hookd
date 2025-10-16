from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, follows, posts, likes

app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:80',
    'http://localhost:5173'
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(follows.router, prefix="/follows", tags=["follows"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(likes.router, prefix="/likes", tags=["likes"])
