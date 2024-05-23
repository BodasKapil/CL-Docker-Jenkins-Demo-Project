from typing import Union
from typing import Optional
from fastapi import FastAPI,Path
from pydantic import BaseModel
app = FastAPI()


class Student(BaseModel):
    name:str
    age:int
    clas:str


class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    clas:Optional[str]=None


students={
    1:{
        "name":"Kapil",
        "age":20,
        "class":"TY AIDS"
    },
    2:{
        "name":"Mrunal",
        "age":20,
        "class":"TY AIDS"
    },
    3:{
        "name":"Dyotak",
        "age":20,
        "class":"TY AIDS"
    }
}

@app.get("/")
def demo():
    return {"Name": "Hi"}


@app.get("/students")
def get_students():
    return students

#path parameter
@app.get("/get-student/{s_id}")
def get_student_infp(s_id:int):
    return students[s_id]

#query string
@app.get("/get-student-name")
#def get_student_name(name:Optional[str]=None):
def get_student_name(name1:str):
    for s_id in students:
        if(students[s_id]["name"]==name1):
            return students[s_id]
    return {"Data":"Not found"}




@app.post("/create-student/{s_id}")
def create_student(s_id:int, student:Student): 
    if s_id in students:
        return{"Error":"Student Exists"}
    
    students[s_id]=student
    return students[s_id]


 
# @app.put("/update-student/{s_id}")
# def update_student(s_id:int, student=Student):
#     if s_id not in students:
#         return{"Error":"Student does not exists"}
    
#     students[s_id]=student
#     return students[s_id]


@app.put("/update-student/{s_id}")
def update_student(s_id: int, student: Student):
    if s_id not in students:
        return {"Error": "Student does not exist"}

    students[s_id] = student.dict()
    return {"message": "Student updated successfully"}


@app.delete("/delete-student/{s_id}")
def delete_student(s_id:int):
    if s_id not in students:
        return {"Error":"Student does not exists"}
    
    del students[s_id]
    return {"Message":"Student Deleted Successfully"}



