from fastapi import FastAPI
from app.database.db import Base, engine
from app.routes import user, task
from app.update_version import get_version



Base.metadata.create_all(bind=engine)

app = FastAPI(title='Todo Application', 
              description='A complex to-do application with user authentication and task management.', 
              version=get_version())

@app.include_router(user.router)
@app.include_router(task.router)

@app.get("/", summary="Root Endpoint", tags=["Root"])
def home() -> dict: 

    return {"message": "Welcome to Simplido"}