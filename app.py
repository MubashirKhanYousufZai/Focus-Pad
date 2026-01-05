import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Todo App",
    page_icon="📝",
    layout="centered"
)

# -------------------------------
# Custom CSS (UI Boost)
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.todo-card {
    background: #111827;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    border: 1px solid #1f2937;
}
.todo-title {
    font-size: 18px;
    font-weight: 600;
    color: #e5e7eb;
}
.completed {
    text-decoration: line-through;
    color: #9ca3af;
}
.small-btn button {
    padding: 5px 10px;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Database Setup (SQLite)
# -------------------------------
DATABASE_URL = "sqlite:///./todos.db"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

# -------------------------------
# App Title
# -------------------------------
st.markdown(
    "<h1 style='text-align:center;color:#38bdf8;'>📝 Todo App</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;color:#9ca3af;'>Simple • Clean • Productive</p>",
    unsafe_allow_html=True
)

# -------------------------------
# Add Task
# -------------------------------
st.subheader("➕ Add New Task")

new_task = st.text_input(
    "Task name",
    placeholder="What do you want to do today?"
)

if st.button("Add Task 🚀"):
    if new_task.strip():
        db = SessionLocal()
        db.add(Todo(title=new_task))
        db.commit()
        db.close()
        st.success("Task added successfully!")
        st.rerun()

# -------------------------------
# Fetch Tasks
# -------------------------------
db = SessionLocal()
tasks = db.query(Todo).order_by(Todo.id.desc()).all()

# -------------------------------
# Task List
# -------------------------------
st.subheader("📋 Your Tasks")

if not tasks:
    st.info("No tasks yet. Start adding some ✨")

for task in tasks:
    with st.container():
        st.markdown("<div class='todo-card'>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([0.1, 0.6, 0.3])

        # Complete checkbox
        with col1:
            checked = st.checkbox(
                "",
                value=task.completed,
                key=f"check_{task.id}"
            )
            if checked != task.completed:
                task.completed = checked
                db.commit()
                st.rerun()

        # Title / Edit
        with col2:
            if st.session_state.get(f"edit_{task.id}", False):
                new_title = st.text_input(
                    "Edit task",
                    value=task.title,
                    key=f"input_{task.id}"
                )
                if st.button("Save 💾", key=f"save_{task.id}"):
                    task.title = new_title
                    st.session_state[f"edit_{task.id}"] = False
                    db.commit()
                    st.rerun()
            else:
                title_class = "completed" if task.completed else "todo-title"
                st.markdown(
                    f"<span class='{title_class}'>{task.title}</span>",
                    unsafe_allow_html=True
                )

        # Actions
        with col3:
            c1, c2 = st.columns(2)

            with c1:
                if st.button("✏️", key=f"editbtn_{task.id}"):
                    st.session_state[f"edit_{task.id}"] = True
                    st.rerun()

            with c2:
                if st.button("🗑️", key=f"del_{task.id}"):
                    db.delete(task)
                    db.commit()
                    st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

db.close()

# -------------------------------
# Footer
# -------------------------------
st.markdown(
    "<hr style='border:1px solid #1f2937'>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;color:#6b7280;'>Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
