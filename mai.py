from datetime import datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {f"Hello to app rest in interview {datetime.now()}"}


@app.get("/test_interview")
def read_item():
    return {"testingFastApi": "ApiRest for interview"}


@app.get("/test_interview/{item_id}")
def read_item(name: str = None):
    name = "Santiago"
    return {"Mi Nombre es ": name}


@app.get("/test_interview/{item_id}")
def read_item(lastName: str = None):
    lastName = "Perea Castillo"
    age = 26
    return {"Mis Apellidos ": lastName}


@app.get("/test_interview/{item_id}")
def read_item(age: int = None):
    age = 26
    return {f"Mi edad es: {age}"}


@app.post("/test_interview/newUser/{item_id}", responses=200)
def read_item(userNew):
    userNew = {
        "name": {},
        "lastName": {},
        "age": {}
    }
    return {userNew}
