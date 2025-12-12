# Interactive To-Do Application

This project provides a professional, console-based to-do list application. It features an interactive command-line interface that allows users to manage their tasks efficiently. The application is designed with a hybrid architecture, utilizing a FastAPI backend that runs seamlessly in a background thread to handle data persistence and business logic, while the main thread provides a responsive and engaging user experience through a decorative console menu.

## Features

-   **Add Tasks:** Easily add new to-do items with a title and optional description.
-   **List Tasks:** View all outstanding and completed tasks.
-   **Complete Tasks:** Mark tasks as complete, providing a clear overview of progress.
-   **Remove Tasks:** Delete unwanted tasks from the list.
-   **Persistent Storage:** All to-do items are automatically saved to `todos.json` for persistence across sessions.
-   **Professional UI:** An aesthetically pleasing console interface enhanced with emojis and symbols for improved readability and user engagement.
-   **FastAPI Backend:** Leverages FastAPI for robust and scalable backend logic, demonstrating modern application development practices.

## Setup Instructions

To get started with the To-Do Application, follow these steps:

1.  **Navigate to the Project Directory:**
    Open your terminal or command prompt and change your current directory to the location of the `todo_app` project:
    ```bash
    cd C:\Users\DELL 5540\Desktop\New folder\todo_app
    ```

2.  **Ensure Python Virtual Environment is Active (or create one):**
    This project requires a Python virtual environment to manage dependencies. If you haven't already, create and activate a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
    (On Linux/macOS, use `source venv/bin/activate`)

3.  **Install Dependencies:**
    Install all required Python packages using pip. The `fastapi`, `uvicorn`, `pydantic`, and `requests` libraries are essential for the application's hybrid architecture.
    ```bash
    .\venv\Scripts\pip install fastapi uvicorn pydantic requests
    ```

## How to Run the Application

Once the setup is complete, you can launch the interactive To-Do application with a single command:

1.  **Start the Application:**
    Ensure your terminal is in the project's root directory.
    ```bash
    python main.py
    ```

2.  **Interact with the Menu:**
    Upon execution, the application will display a welcome message and an interactive menu. You can select options by entering the corresponding number (1-5) and pressing Enter.

The application will automatically start the FastAPI service in a background thread, handling all data operations behind the scenes.

## Usage Examples

-   **Add a Task:**
    Enter `1` for "Add a new to-do", then follow the prompts for the title and description.
-   **List Tasks:**
    Enter `2` for "List all to-dos" to see your current tasks.
-   **Mark Task as Complete:**
    Enter `3` for "Mark a to-do as complete", then provide the ID of the task.
-   **Remove Task:**
    Enter `4` for "Remove a to-do", then provide the ID of the task.
-   **Exit Application:**
    Enter `5` to gracefully exit the application.

## Project Structure

-   `main.py`: The core application file containing both the interactive console UI and the embedded FastAPI backend logic.
-   `todos.json`: A JSON file used for persistent storage of to-do items.
-   `venv/`: The Python virtual environment directory.

This setup ensures a professional and user-friendly experience, blending the simplicity of a console application with the robustness of a modern web framework.
