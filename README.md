# 🚀 TaskFlow – Plain Django Task Manager

TaskFlow is a premium **Task Management Web Application** developed using **plain Django**, standard templates, forms, and session-based authentication.

It provides a modern **Kanban Board interface** for organizing and tracking tasks using an elegant **Obsidian Glassmorphism UI** with responsive layouts and smooth interactions.

---

# 📌 Project Explanation

## Overview

TaskFlow is designed to help users create, manage, and track tasks efficiently.

The application uses **server-side rendering with Django templates**, making it lightweight and easy to deploy.

Users can:

- Create tasks
- Edit tasks
- Delete tasks
- Track progress visually
- Organize workflow into stages

---

## Workflow

```text
User Authentication
        ↓
Dashboard Access
        ↓
Create / Manage Tasks
        ↓
Store in Database
        ↓
Display in Kanban Board
        ↓
Search and Track Progress
```

---

# ✨ Features

<table>
<tr>

<td width="50%">

### 📝 Task Management
- Create Tasks
- Update Tasks
- Delete Tasks
- Organize Tasks

</td>

<td width="50%">

### 📋 Kanban Dashboard
- 🟠 To Do
- 🔵 In Progress
- 🟢 Done

</td>

</tr>
</table>

---

<table>
<tr>

<td width="50%">

### 🔐 Authentication
- Registration
- Login
- Session Management

</td>

<td width="50%">

### 🎨 UI Features
- 🌑 Dark Theme
- ☀️ Light Theme
- 📱 Responsive Design
- 🔍 Dynamic Search
- 🙈🙉 Password Toggle

</td>

</tr>
</table>

---

# 🛠️ Tech Stack

<table>
<tr>

<td width="25%" valign="top">

### Backend
- Django  
- Gunicorn  
- WhiteNoise  

</td>

<td width="25%" valign="top">

### Frontend
- HTML5  
- CSS3  
- JavaScript  

</td>

<td width="25%" valign="top">

### Database
- SQLite3  

</td>

<td width="25%" valign="top">

### Deployment
- Render  

</td>

</tr>
</table>

---

# 📷 Screenshots

## 📱 Responsive Layout (All Devices)

<p align="center">
<img src="screenshots/responsive_all_devices.png" width="95%">
</p>

---

# ☀️ Light Theme

<table>
<tr>

<td align="center">
<b>Login</b><br>
<img src="screenshots/light_login.png" width="100%">
</td>

<td align="center">
<b>Signup</b><br>
<img src="screenshots/light_signup.png" width="100%">
</td>

<td align="center">
<b>Dashboard</b><br>
<img src="screenshots/light_dashboard.png" width="100%">
</td>

</tr>
</table>

---

# 🌑 Dark Theme

<table>
<tr>

<td align="center">
<b>Login</b><br>
<img src="screenshots/dark_login.png" width="100%">
</td>

<td align="center">
<b>Signup</b><br>
<img src="screenshots/dark_signup.png" width="100%">
</td>

<td align="center">
<b>Dashboard</b><br>
<img src="screenshots/dark_dashboard.png" width="100%">
</td>

</tr>
</table>

---

# 💻 Local Setup

## Clone Repository

```bash
git clone https://github.com/gudurujeevankumar/Task-Manager.git
cd Task-Manager/backend
```

---

## Create Virtual Environment

### macOS / Linux

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

# ☁️ Deployment (Render)

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

**Jeevan Kumar**

Built using Django with responsive UI and Kanban workflow.
