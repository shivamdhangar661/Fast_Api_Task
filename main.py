from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
students ={
    1: {
        "name" : "Himansh",
        "age" : 23,
        "course": "btech"
    },
    2 : {
        "name" : "Ravi",
        "age" : 24,
        "course": "BCA"
    }
}


class Students(BaseModel):
    name:str
    age: int
    course: str

class UpdateStudent(BaseModel):
    name:str|None
    age:int | None
    cournse:str | None

#simple get method
@app.get("/")
def index():
    return {"name": "Himanshu"}


#path parameter 
@app.get("/get-student/{student_id}")
def get_students(student_id:int):
    return students[student_id]


#query parameter
@app.get("get-by-name")
def get_students(name : str = None):
    for students_id in students:
        if students[students_id]["name"] == name:
            return students[students_id]
        return {"Data":"Not found"}


#post data
@app.post("/create-student/{students_id}")
def create_students(student_id: int, student: Students):
    if student_id in students:
        return {"Error": "Students Alredy Exits"}
    students[student_id] = student
    return students[student]


#update data
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student doesn't exist"}
    students[student_id] = student


#delete data
@app.delete("/delete-stuetns/{students_id}")
def delete_students(student_id: int):
    if student_id not in students:
        return {"Error Students doen't exist"}
    del students[student_id]
    return {"message": "student Deleted successfully"}


