from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: str
    name: str
    age: int
    course: str


def load_data():
    with open("studentDB.json", "r") as file:
        data = json.load(file)
    return data


@app.get("/home")
def home():
    return "Student API is running"

@app.get("/students")
def get_students():
    return load_data()

@app.get("/students/{student_id}")
def get_student(student_id: str):
    data = load_data()
    for student in data:
        if student_id == student["id"]:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students")
def add_student(student: Student):
    data = load_data()
    data.append(student.model_dump())
    with open("studentDB.json", "w") as file:
        json.dump(data, file, indent = 4)
    return f"Student added succesfully {student}"

@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    data = load_data()
    # updated_data = [student for student in data if student["id"] != student_id]

    updated_data = []
    for student in data:
        if student["id"] != student_id:
            updated_data.append(student)

    if len(updated_data) == len(data):
        raise HTTPException(status_code=404, detail="Student not found")

    with open("studentDB.json", "w") as file:
        json.dump(updated_data, file, indent=4)

    return {"message": "Student record deleted"}