from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
from apis.base import api_router
from fastapi.middleware.cors import CORSMiddleware


def create_tables():
     Base.metadata.create_all(bind=engine)

def start_application():
     app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
     create_tables()
     app.include_router(api_router)   #new
     # Add this middleware to allow your Next.js app to communicate with FastAPI
     app.add_middleware(
          CORSMiddleware,
          allow_origins=["http://localhost:3000"], # Your Next.js frontend origin
          allow_credentials=True,
          allow_methods=["*"], # Allows all methods (GET, POST, etc.)
          allow_headers=["*"], # Allows all headers
     )
     
     return app

app = start_application()

@app.get("/")
def home():
     return {"message": "Hello fastapi"}