# 🗂️ Todo App – Project Plan

This document outlines the **planning, development phases, and future roadmap** for the Todo App project.

---

## 🎯 Project Goal

To build a **simple, clean, and fully functional Todo application** using Python and Streamlit, while keeping:

- Single-file architecture
- Easy deployment
- Beginner-friendly code
- Portfolio-ready quality

---

## 🧩 Scope of the Project

### In Scope
- Task management (CRUD)
- Persistent database storage
- Clean UI
- Local & cloud deployment

### Out of Scope (for now)
- Multi-user authentication
- Mobile-native app
- Heavy frontend frameworks

---

## 🛠️ Technology Decisions

| Area        | Choice        | Reason |
|------------|--------------|--------|
| Language   | Python        | Simple & powerful |
| UI         | Streamlit     | Fast UI + deployable |
| ORM        | SQLAlchemy    | Clean DB abstraction |
| Database   | SQLite        | Lightweight & local |
| Structure | Single file   | Streamlit-friendly |

---

## 🏗️ Development Phases

### Phase 1 – Console App ✅
- Basic todo logic
- JSON storage
- CRUD operations

---

### Phase 2 – UI Conversion ✅
- Streamlit interface
- Input forms
- Task listing

---

### Phase 3 – Database Integration ✅
- SQLite database
- SQLAlchemy ORM
- Auto table creation

---

### Phase 4 – Feature Enhancements ✅
- Edit tasks
- Mark completed
- Delete tasks
- UI cleanup

---

### Phase 5 – UI Polish ✅
- Modern layout
- Emojis & spacing
- User-friendly UX

---

## 🧪 Testing Strategy

- Manual testing through UI
- Edge cases:
  - Empty task
  - Long text
  - Edit & delete same task
- Database reset testing

---

## 🚀 Deployment Plan

### Local
```bash
streamlit run app.py
````

### Cloud

* Push to GitHub
* Deploy via Streamlit Cloud
* Select `app.py` as entry point

---

## 📈 Future Roadmap

### Short-Term

* Task priorities
* Due dates
* Filters (completed / pending)

### Mid-Term

* Progress analytics
* Dark mode
* Search functionality

### Long-Term

* PostgreSQL / NeonDB
* AI-based task suggestions
* User authentication

---

## 📌 Risks & Mitigation

| Risk             | Mitigation              |
| ---------------- | ----------------------- |
| DB schema errors | Delete & recreate DB    |
| Over-complexity  | Keep single-file design |
| UI clutter       | Minimalist design       |

---

## 🧠 Learning Outcomes

* Streamlit full-stack workflow
* ORM-based database handling
* UI/UX thinking
* Deployment readiness
* Project structuring

---

## 👨‍💻 Author

**Mubashir**
Web Developer | Python Learner
Pakistan 🇵🇰

---