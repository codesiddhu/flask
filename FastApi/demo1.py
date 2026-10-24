from fastapi import FastAPI, Path, Query, HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"name": "siddhu"}


students = {
    1: {
        "name": "siddhu",
        "age": 24,
        "college": "svcet",
        "Location": "chitoor"
    }
}


@app.get("/student/{id}")
def get_student(
    id: int = Path(
        ...,
        description="Enter the student ID",
        gt=0,
        lt=3
    )
):
    if id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    return students[id]


@app.get("/data")
def user_data(name: str = Query(..., description="Enter the student name")):
    for student_id in students:
        if students[student_id]["name"].lower() == name.lower():
            return students[student_id]

    raise HTTPException(status_code=404, detail="Student not found")