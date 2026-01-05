# 🤖 Gemini Context File – Focus Pad

This document provides **context, architecture, and rules** for AI models (Gemini / GPT) working on this project.

---

## 📌 Project Overview

This is a **single-file full-stack Todo application** built using:

- **Streamlit** for UI
- **SQLAlchemy** for ORM
- **SQLite** for persistent storage

The entire frontend and backend logic lives in **`app.py`** to ensure:
- Easy deployment on Streamlit Cloud
- No separate backend/frontend folders
- Simple maintainability

---

## 🧠 Core Features

- Add new todo tasks
- Edit existing tasks
- Mark tasks as completed
- Delete tasks
- Persistent database storage
- Clean, modern Streamlit UI

---

## 📂 Project Structure (Important)

```

todo_app/
├── app.py          # UI + backend logic (single entry point)
├── todos.db        # SQLite database (auto-generated)
├── README.md
├── gemini.md       # This file
├── venv/
└── **pycache**/

```

⚠️ **Do NOT introduce multiple backend/frontend folders**  
⚠️ **Do NOT split the app into multiple files unless explicitly requested**

---

## 🗄️ Database Schema

Table name: `todos`

| Column     | Type     | Description                  |
|-----------|----------|------------------------------|
| id        | Integer  | Primary key                  |
| title     | String   | Task title                   |
| completed | Boolean  | Task completion status       |

---

## ⚙️ Technical Rules (VERY IMPORTANT)

When modifying or extending this project:

1. ✅ Keep everything inside `app.py`
2. ✅ Use SQLAlchemy ORM (no raw SQL)
3. ✅ Use Streamlit-native components
4. ❌ Do not introduce FastAPI / Flask
5. ❌ Do not create separate backend servers
6. ❌ Do not require environment variables unless necessary

---

## 🎨 UI Guidelines

- Minimal & clean design
- Proper spacing
- Clear call-to-action buttons
- Emojis allowed but not excessive
- Must remain beginner-friendly

---

## 🚀 Allowed Future Enhancements

AI models may safely add:

- Due dates
- Task priority levels
- Search & filter
- Progress bar
- Dark/light theme toggle
- PostgreSQL / NeonDB (optional)
- User authentication (optional)

---

## 🧪 Debugging Instructions

If database errors occur:
- Stop the app
- Delete `todos.db`
- Restart the app

This resets the schema safely.

---

## 👤 Author Context

The project is created by **Mubashir**, a web developer and Python learner from Pakistan, using this project for:
- Learning full-stack concepts
- Portfolio building
- Deployment practice

AI responses should:
- Stay beginner-friendly
- Avoid overengineering
- Explain logic clearly when requested

---

