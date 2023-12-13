from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

db = []

class TodoItem(BaseModel):
    id: int
    task: str
    completed: bool = False

@app.post("/todos/", response_model=TodoItem)
def create_todo_item(task: str):
    new_todo = TodoItem(id=len(db) + 1, task=task)
    db.append(new_todo)
    return new_todo

@app.get("/todos/", response_model=List[TodoItem])
def get_todo_list():
    return db

@app.put("/todos/{todo_id}/", response_model=TodoItem)
def update_todo_item(todo_id: int, completed: bool):
    for todo in db:
        if todo.id == todo_id:
            todo.completed = completed
            return todo


