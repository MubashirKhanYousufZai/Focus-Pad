from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os
from typing import List, Dict, Any

app = FastAPI()

DATA_FILE = "todos.json"

class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

class TodosData(BaseModel):
    todos: List[Todo]
    counter: int

def get_todos_data() -> TodosData:
    if not os.path.exists(DATA_FILE):
        return TodosData(todos=[], counter=0)
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return TodosData(**data)

def save_todos_data(todos_data: TodosData):
    with open(DATA_FILE, "w") as f:
        json.dump(todos_data.dict(), f, indent=4)

@app.get("/todos/", response_model=List[Todo])
def read_todos():
    todos_data = get_todos_data()
    return todos_data.todos

@app.post("/todos/", response_model=Todo)
def create_todo(title: str, description: str = ""):
    todos_data = get_todos_data()
    todos_data.counter += 1
    new_todo = Todo(
        id=todos_data.counter,
        title=title,
        description=description,
        completed=False
    )
    todos_data.todos.append(new_todo)
    save_todos_data(todos_data)
    return new_todo

@app.get("/todos/{todo_id}", response_model=Todo)
def read_todo(todo_id: int):
    todos_data = get_todos_data()
    for todo in todos_data.todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, completed: bool):
    todos_data = get_todos_data()
    for todo in todos_data.todos:
        if todo.id == todo_id:
            todo.completed = completed
            save_todos_data(todos_data)
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    todos_data = get_todos_data()
    todo_to_delete = None
    for todo in todos_data.todos:
        if todo.id == todo_id:
            todo_to_delete = todo
            break
    
    if todo_to_delete:
        todos_data.todos.remove(todo_to_delete)
        save_todos_data(todos_data)
        return todo_to_delete
    raise HTTPException(status_code=404, detail="Todo not found")
