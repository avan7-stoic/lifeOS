from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
db = SQLAlchemy()

# User model
class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)

    tasks = relationship("Task", back_populates="user")
    goals = relationship("Goal", back_populates="user")
    habits = relationship("Habit", back_populates="user")

# Task model
class Task(db.Model):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    goal_id = Column(Integer, ForeignKey("goals.id"), nullable=True)
    title = Column(String(255), nullable=False)
    description = Column(String)
    due_date = Column(DateTime)
    priority = Column(Enum("low", "medium", "high", name="priority"))
    tags = Column(String)  # comma-separated
    recurring = Column(String)  # daily/weekly/monthly
    status = Column(String, default="todo")
    focus = Column(Boolean, default=False)

    user = relationship("User", back_populates="tasks")
    goal = relationship("Goal", back_populates="tasks")
    subtasks = relationship("SubTask", back_populates="task")

class SubTask(db.Model):
    __tablename__ = "subtasks"
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    title = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)

    task = relationship("Task", back_populates="subtasks")

# Goal model
class Goal(db.Model):
    __tablename__ = "goals"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String)
    deadline = Column(DateTime)

    user = relationship("User", back_populates="goals")
    tasks = relationship("Task", back_populates="goal")

# Habit model
class Habit(db.Model):
    __tablename__ = "habits"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    frequency = Column(String)  # daily/weekly
    streak = Column(Integer, default=0)
    success_rate = Column(Float, default=0.0)

    user = relationship("User", back_populates="habits")
