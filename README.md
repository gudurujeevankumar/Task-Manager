# 🚀 TaskFlow – Plain Django Task Manager

TaskFlow is a premium **Task Management Web Application** developed using **plain Django**, standard templates, forms, and session-based authentication.

The application provides a clean and modern **Kanban Board interface** for managing tasks visually while maintaining a responsive and elegant user experience using an **Obsidian Glassmorphism UI Theme**.

---

# 📌 Project Explanation

## Overview
TaskFlow is designed to help users organize and track tasks efficiently.

The application follows a traditional **server-side rendering architecture**, where Django handles both backend processing and frontend rendering.

Users can:

- Create tasks
- Edit tasks
- Delete tasks
- Track progress visually
- Manage workflow through categorized stages

---

## Workflow

```text
User Authentication
       ↓
Dashboard Access
       ↓
Create / Update Tasks
       ↓
Store in Database
       ↓
Display in Kanban Board
       ↓
Search and Track Progress
```

---

# ✨ Features

## Task Management
- Create Tasks
- Update Tasks
- Delete Tasks
- Organize Tasks

---

## Kanban Dashboard
Tasks are categorized into:

- 🟠 To Do
- 🔵 In Progress
- 🟢 Done

---

## Authentication
Secure authentication using:

- Registration
- Login
- Session Management

---

## UI Features

- 🌑 Dark Theme
- ☀️ Light Theme
- 📱 Responsive Layout
- 🔍 Dynamic Search
- 🙈🙉 Password Visibility Toggle
- ✨ Smooth Animations

---

# 🛠️ Tech Stack

## Backend
- Django
- Gunicorn
- WhiteNoise

## Frontend
- HTML5
- CSS3
- JavaScript

## Database
- SQLite3

## Deployment
- Render

---

# 📷 Screenshots

## 1. 📱 Responsive Screenshots (All Devices)

Desktop • Tablet • Mobile

<p align="center">
<img src="screenshots/responsive_all_devices.png" width="100%">
</p>

---

# ☀️ Light Theme

## Login • Signup • Dashboard

<table>
<tr>

<td align="center">
<b>Login Page</b><br>
<img src="screenshots/light_login.png" width="300">
</td>

<td align="center">
<b>Signup Page</b><br>
<img src="screenshots/light_signup.png" width="300">
</td>

<td align="center">
<b>Dashboard</b><br>
<img src="screenshots/light_dashboard.png" width="300">
</td>

</tr>
</table>

---

# 🌑 Dark Theme

## Login • Signup • Dashboard

<table>
<tr>

<td align="center">
<b>Login Page</b><br>
<img src="screenshots/dark_login.png" width="300">
</td>

<td align="center">
<b>Signup Page</b><br>
<img src="screenshots/dark_signup.png" width="300">
</td>

<td align="center">
<b>Dashboard</b><br>
<img src="screenshots/dark_dashboard.png" width="300">
</td>

</tr>
</table>

---

# 💻 Local Setup

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Task-Manager.git
cd Task-Manager/backend
```

## Create Virtual Environment

### macOS/Linux

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Migrations

```bash
python manage.py migrate
```

---

## Start Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# ☁️ Render Deployment

Configure:

```text
Runtime:
Python
```

```text
Root Directory:
backend
```

```text
Build Command:
./build.sh
```

```text
Start Command:
gunicorn task_manager.wsgi:application
```

Environment Variables:

```text
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=*
```

---

# 📂 Project Structure

```text
Task-Manager
│
├── backend
│   ├── task_manager
│   ├── tasks
│   ├── templates
│   ├── static
│   └── manage.py
│
├── screenshots
│   ├── responsive_all_devices.png
│   ├── light_login.png
│   ├── light_signup.png
│   ├── light_dashboard.png
│   ├── dark_login.png
│   ├── dark_signup.png
│   └── dark_dashboard.png
│
└── README.md
```

---

# 👨‍💻 Author

Developed using Django with a modern responsive UI and Kanban workflow system.