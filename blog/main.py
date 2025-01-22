# to run the server, run the following command in terminal: uvicorn blog.main:app --reload
from fastapi import FastAPI
from . import  models
from .database import engine
from  .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
