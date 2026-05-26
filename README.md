# 📌 Project Explanation

## Overview
TaskFlow is a premium **task management web application** developed using **plain Django** with server-side rendering. The project allows users to create, manage, and track tasks using a visual **Kanban board** interface.

Unlike modern SPA frameworks, TaskFlow uses Django templates, forms, and session-based authentication to deliver a complete full-stack experience.

---

## Objective
The purpose of TaskFlow is to provide a simple and responsive platform where users can:

- Organize tasks efficiently
- Track task progress visually
- Manage work using categorized stages
- Experience a clean and modern user interface

---

## System Workflow

```text
User Authentication
        ↓
Access Dashboard
        ↓
Create / Edit / Delete Tasks
        ↓
Store Data in SQLite Database
        ↓
Display Tasks in Kanban Board
        ↓
Search and Track Progress
```

---

## Core Functionalities

### User Authentication
TaskFlow uses Django’s built-in session authentication system.

Features:
- User Registration
- User Login
- Session Management
- Secure Access Control

---

### Task Management
Users can perform complete CRUD operations:

- Create tasks
- View tasks
- Update task information
- Delete tasks

Each task includes:
- Title
- Description
- Stage

---

### Kanban Dashboard
Tasks are organized into three workflow stages:

- **To Do** → Tasks waiting to start
- **In Progress** → Tasks currently being worked on
- **Done** → Completed tasks

This structure helps users visualize productivity and progress.

---

### Search System
TaskFlow includes an instant search feature that:

- Filters tasks dynamically
- Searches title and description
- Updates task counts automatically

---

### UI Design
The application follows an **Obsidian Glassmorphism Theme**.

Features:
- Dark Mode
- Light Mode
- Smooth Transitions
- Responsive Design
- Interactive Password Toggle (🙈 / 🙉)

---

## Technologies Used

### Backend
- Django
- Gunicorn
- WhiteNoise

### Database
- SQLite3

### Frontend
- HTML5
- CSS3
- JavaScript

### Deployment
- Render

---

## Conclusion
TaskFlow is a lightweight yet complete Django-based task management system that combines authentication, task tracking, and modern UI design into a responsive productivity platform.