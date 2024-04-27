from fastapi import FastAPI
from .config.database import Base, engine


app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get('/')
def root():
    return {
        "status": 200,
        "message": "Hello World"
    }