# 📝 Focus Pad (Streamlit + SQLAlchemy)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.26.1-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A **simple, clean, and productive Todo application** built with **Python**, **Streamlit**, and **SQLAlchemy**.  
This project is designed as a **single-file full-stack app**, making it easy to run locally and deploy on Streamlit Cloud.  

> This is **Hackathon 2 Phase 2** project by **Sir Ameen Alam** (GIAIC) and developed by **Mubashir**.

## 🚀 Features

- ➕ Add new tasks
- ✅ Mark tasks as completed (checkbox)
- ✏️ Edit existing tasks
- 🗑️ Delete tasks
- 🎨 Clean & modern UI (Streamlit)
- 💾 Persistent storage using SQLite
- ⚡ Single-file app (frontend + backend together)

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** – UI & frontend
- **SQLAlchemy** – ORM & database handling
- **SQLite** – Lightweight database (local)

---

## 📁 Project Structure

```

todo_app/
│
├── app.py          # Main Streamlit app (UI + backend logic)
├── todos.db        # SQLite database (auto-created)
├── README.md       # Project documentation
├── venv/           # Virtual environment
└── **pycache**/    # Python cache files

````

> ⚠️ You only need to run **`app.py`** — no separate backend or frontend folders.

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/MubashirKhanYousufZai/Focus-Pad.git
cd Focus-Pad
````

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install streamlit sqlalchemy
```

### 4️⃣ Run the app

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧠 Notes

* Database (`todos.db`) is **auto-created** on first run
* If you face DB column errors, simply:

  * Stop the app
  * Delete `todos.db`
  * Run again

---

## 🚀 Deployment

This app is **Streamlit Cloud ready**:

1. Push code to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Select repository
4. Choose `app.py`
5. Deploy 🎉

---

## 📌 Future Improvements

* ⏳ Due dates
* 🎯 Task priorities
* 📊 Progress bar
* 🌙 Dark mode toggle
* ☁️ Cloud database (Neon / Supabase)
* 🔐 User authentication

---

## 👨‍💻 Author

**Mubashir**
Web Developer | Python & Streamlit Enthusiast
📍 Pakistan

---
```

