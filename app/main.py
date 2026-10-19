from fastapi import FastAPI

app=FastAPI(title="Student APT")

@app.get("/")
def home():
    return{
        "message": "Welcome to Student API"
    }
@app.get("/health")
def home2():
    return{
        "message": "Server is Heathy"
    }
@app.get("/darshan")
def home3():
    return{
        "message": "Hello Darshan"
    }