from fastapi import FastAPI, Body
from typing import List
from pydantic import BaseModel, Field

app = FastAPI(
    title="FastAPI - Hello World",
    description="This is the Hello World of FastAPI.",
    version="1.0.0",
) 

class Student(BaseModel):
   id: int
   name :str = Field(None, title="name of student", max_length=10)
   subjects: List[str] = []


@app.get("/")
def hello_world():
    return {"Hello": "World"}

@app.post("/students/model")
def student_data(s1: Student):
   return s1

@app.post("/students/body")
def student_data(name:str=Body(...), marks:int=Body(...)):
   return {"name":name,"marks": marks}

@app.post("/students/{college}")
def student_data(college:str, age:int, student:Student):
   retval={"college":college, "age":age, **student.dict()}
   return retval