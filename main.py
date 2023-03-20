from typing import Union
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()


# GET
# POST
# PUT
# DELETE

class Person(BaseModel):
    name: str | None = Field(
        default=None, title="The name's person", max_length=60
    )
    lastName: str | None = Field(
        default=None, title="The lastName's person", max_length=60
    )
    age: int | None = Field(gt=18, description="the age must be greater than eighteen") 
    
person_list = {
    1: {"name": "Pedro", "lastName": "Martinez", "age": 15},
    2: {"name": "Mauricio", "lastName": "Lopez", "age": 23},
    3: {"name": "Maria", "lastName": "Gutierrez", "age": 30},
}

@app.get("/people")
async def get_all_people():
    return {"data": person_list}

@app.get("/people/{id_person}", response_model=Person)
async def get_person(id_person: int):
    
    if id_person not in person_list:
        raise HTTPException(status_code=404, detail="Person not found")
    
    return person_list[id_person]

@app.post("/people", response_model=Person)
async def new_person(person: Person):
    contador = len(person_list) + 1
    person_list[contador] = {"name": person.name, "lastName": person.lastName, "age": person.age}
    return person_list[contador]

@app.put("/people/{id_person}", response_model=Person)
async def update_person(id_person: int, person: Person):
    
    if id_person not in person_list:
        raise HTTPException(status_code=404, detail="Person not found")
    
    person_list[id_person] = {"name": person.name, "lastName": person.lastName, "age": person.age}
    return person_list[id_person]


@app.delete("/people/{id_person}")
async def delete_person(id_person: int):
    if id_person not in person_list:
        raise HTTPException(status_code=404, detail="Person not found")
    
    del person_list[id_person]
    return "Person deleted"