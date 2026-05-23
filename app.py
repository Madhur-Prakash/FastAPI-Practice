# to run the server, run the following command in terminal: uvicorn app:app --reload
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app = FastAPI()

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.get("/")
def index():
    return  {"data":{"name":"jhon"}}   

@app.get('/about')
def about(limit=10,published:bool=True,sort:Optional[str]=None):
    # in limit it can also be written as limit:int=10 instead of limit=10
    # default value: either set for all parameters or first write the parameter without default value and then write the parameter with default value
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blogs from db'} 

@app.get("/about/{id}")
def about(id:int    ):
    return {"data":id}

@app.post("/blog")
def create_blog(blog:Blog):
    return {"data":f"Blog is created with title as {blog.title} and body as {blog.body} and published as {blog.published}"}


# if __name__ == "__main__":
#     uvicorn.run(debug=True)
