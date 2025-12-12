import json
import os
import requests
import sys
import threading
import uvicorn
import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# --- Configuration ---
DATA_FILE = "todos.json"
API_HOST = "127.0.0.1"
API_PORT = 8000
API_URL = f"http://{API_HOST}:{API_PORT}"

# --- Part 1: FastAPI Backend Logic ---
app = FastAPI()

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
        try:
            data = json.load(f)
            return TodosData(**data)
        except (json.JSONDecodeError, TypeError):
            return TodosData(todos=[], counter=0)

def save_todos_data(todos_data: TodosData):
    with open(DATA_FILE, "w") as f:
        json.dump(todos_data.dict(), f, indent=4)

@app.get("/todos/", response_model=List[Todo])
def read_todos():
    todos_data = get_todos_data()
    return todos_data.todos

@app.post("/todos/", response_model=Todo)
def create_todo_api(title: str, description: str = ""):
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

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo_api(todo_id: int):
    todos_data = get_todos_data()
    for todo in todos_data.todos:
        if todo.id == todo_id:
            todo.completed = True
            save_todos_data(todos_data)
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo_api(todo_id: int):
    todos_data = get_todos_data()
    todo_to_delete = next((todo for todo in todos_data.todos if todo.id == todo_id), None)
    if todo_to_delete:
        todos_data.todos.remove(todo_to_delete)
        save_todos_data(todos_data)
        return todo_to_delete
    raise HTTPException(status_code=404, detail="Todo not found")

# --- Part 2: Interactive Console UI ---
def display_menu():
    print("\n✨~~~ To-Do App Menu (Professional Edition) ~~~✨")
    print("1. 📝 Add a new to-do")
    print("2. 📋 List all to-dos")
    print("3. ✅ Mark a to-do as complete")
    print("4. ❌ Remove a to-do")
    print("5. 👋 Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def add_todo_ui():
    title = input("✍️ Enter to-do title: ").strip()
    if not title:
        print("❌ Error: Title cannot be empty.")
        return
    description = input("💬 Enter description (optional): ").strip()
    try:
        response = requests.post(f"{API_URL}/todos/", params={"title": title, "description": description})
        response.raise_for_status()
        new_todo = response.json()
        print(f"🎉 Successfully added to-do item with ID: {new_todo['id']}")
    except requests.exceptions.RequestException as e:
        print(f"🚨 Error communicating with API: {e}")

def list_todos_ui():
    try:
        response = requests.get(f"{API_URL}/todos/")
        response.raise_for_status()
        todos = response.json()
        if not todos:
            print("📭 No to-do items yet.")
            return

        print("\n~~~ Your To-Do List ~~~")
        for todo in todos:
            status = "✅" if todo["completed"] else "⏳"
            print(f"{status} ID: {todo['id']} - {todo['title']}")
            if todo["description"]:
                print(f"    📝 Description: {todo['description']}")
        print("~~~~~~~~~~~~~~~~~~~~~~~")
    except requests.exceptions.RequestException as e:
        print(f"🚨 Error communicating with API: {e}")

def complete_todo_ui():
    todo_id_str = input("✨ Enter the ID of the to-do to mark as complete: ").strip()
    try:
        todo_id = int(todo_id_str)
        response = requests.put(f"{API_URL}/todos/{todo_id}")
        if response.status_code == 404:
             print(f"⚠️ Error: To-do item with ID {todo_id} not found.")
             return
        response.raise_for_status()
        print(f"🎉 To-do item {todo_id} marked as complete.")
    except ValueError:
        print("❌ Error: Invalid ID. Please enter a number.")
    except requests.exceptions.RequestException as e:
        print(f"🚨 Error communicating with API: {e}")

def remove_todo_ui():
    todo_id_str = input("🗑️ Enter the ID of the to-do to remove: ").strip()
    try:
        todo_id = int(todo_id_str)
        response = requests.delete(f"{API_URL}/todos/{todo_id}")
        if response.status_code == 404:
             print(f"⚠️ Error: To-do item with ID {todo_id} not found.")
             return
        response.raise_for_status()
        print(f"🗑️ To-do item {todo_id} removed.")
    except ValueError:
        print("❌ Error: Invalid ID. Please enter a number.")
    except requests.exceptions.RequestException as e:
        print(f"🚨 Error communicating with API: {e}")

def console_ui():
    """Main function for the interactive console user interface."""
    # Give the server a moment to start
    time.sleep(1)
    
    print("🌟🌟🌟 Welcome to your interactive To-Do App! 🌟🌟🌟")
    print("🚀 Powered by a background FastAPI service. 🚀")

    while True:
        display_menu()
        choice = input("👉 Enter your choice (1-5): ").strip()
        if choice == '1':
            add_todo_ui()
        elif choice == '2':
            list_todos_ui()
        elif choice == '3':
            complete_todo_ui()
        elif choice == '4':
            remove_todo_ui()
        elif choice == '5':
            print("👋 Exiting To-Do App. Goodbye! 👋")
            # The background server thread will exit automatically as it's a daemon
            break
        else:
            print("🚫 Invalid choice. Please enter a number between 1 and 5.")

# --- Part 3: Server and Main Execution ---
def run_server():
    """Runs the Uvicorn server in a separate thread."""
    uvicorn.run(app, host=API_HOST, port=API_PORT, log_level="warning")

if __name__ == "__main__":
    # Start the FastAPI server in a background daemon thread
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Run the console UI in the main thread
    try:
        console_ui()
    except (KeyboardInterrupt, SystemExit):
        print("\n👋 Shutting down. Goodbye! 👋")
    sys.exit(0)
    