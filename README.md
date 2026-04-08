# TaskFlow API

A backend REST API for task and workflow management, built with **Python**, **Django**, **Django REST Framework**, and **Docker**.

This project is designed as a scalable backend system and will be developed step by step, starting from a clean MVP and evolving into a more advanced task management platform.

---

## 🚀 Project Vision

**TaskFlow API** aims to provide:

- User authentication system
- Task management (CRUD)
- Project organization
- Task priorities and statuses
- Filtering and search
- Collaboration features (future)
- Fully containerized environment using Docker

---

## 🎯 Main Goals

- Build a production-ready REST API using Django REST Framework
- Use PostgreSQL as the primary database
- Containerize the application with Docker
- Maintain clean and scalable architecture
- Prepare for future deployment and CI/CD

---

## 🧩 MVP Features (Phase 1)

### Authentication
- Register user
- Login user
- Token-based authentication
- Get current user profile

### Tasks
- Create task
- List tasks
- Retrieve task details
- Update task
- Delete task

### Task Fields
- `id`
- `title`
- `description`
- `status` (todo / in_progress / done)
- `priority` (low / medium / high)
- `due_date`
- `created_at`
- `updated_at`
- `owner`

### Filtering & Search
- Filter by status
- Filter by priority
- Filter by due date
- Search by title/description
- Ordering

---

## 🧠 Future Features

- Projects system
- Team collaboration
- Task assignment to users
- Comments & activity logs
- Notifications
- Tags / labels
- Analytics dashboard
- Background jobs (Celery + Redis)
- JWT authentication
- API documentation (Swagger / OpenAPI)

---

## 🛠 Tech Stack

### Core
- Python 3.x
- Django
- Django REST Framework

### Database
- PostgreSQL

### DevOps
- Docker
- Docker Compose

### Optional (future)
- Celery
- Redis
- Nginx
- Gunicorn
- drf-spectacular

---

## 📁 Proposed Structure

```bash
taskflow-api/
├── apps/
│   ├── users/
│   ├── tasks/
│   └── common/
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── local.py
│   │   └── production.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── docker/
├── requirements/
├── tests/
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── README.md
