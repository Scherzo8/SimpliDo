from fastapi import FastAPI


app = FastAPI(title='Todo Application', 
              description='A complex to-do application with user authentication and task management.', 
              version='0.1.0')

@app.get("/", summary="Root Endpoint")
def home() -> dict: 

    return {"message": "Welcome to Simplido"}