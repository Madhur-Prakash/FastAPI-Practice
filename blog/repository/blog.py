from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog,db: Session):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)# the RHS comes from the schemas.py file and the LHS comes from the models.py file
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
     # blog=db.query(models.Blog).get(id)           
     # we can also use ".get(id)" instead of ".filter(models.Blog.id==id).first() as done above"

    blog.delete(synchronize_session=False)
    db.commit()
    # blog=db.query(models.Blog).filter(models.Blog.id==id).delete()   # alternative method to delete the blog,need to use db.commit() after this
    return 'done'

def update(id:int,request:schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.update({"title":request.title,"body":request.body})
        # blog.update(updated_blog) causes error
    db.commit()
    return {"detail":f"blog with id {id} updated"}

def show(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
 # response.status_code=status.HTTP_404_NOT_FOUND           ->>  alternative method to raise HTTPException(line 40 and 41)
    # return {"detail":f"blog with id {id} not found"}         ->> when using the method defined in line 44 and 45 , we need to use:   
                                                                # "response: Response" in the function parameters

    return blog