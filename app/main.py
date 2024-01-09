from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from . import models
from .database import engine, get_db
from .routers import post, users, auth, vote
from .config import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.project_title, version=settings.project_version)

origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router) 
app.include_router(vote.router) 



@app.get("/")
def test_ost(db: Session = Depends(get_db)):
    post = db.query(models.Blog).all()

    return  {"message": "Hello Docker deployment"}
    



