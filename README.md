# TaskFlow API

TaskFlow API is a backend REST API for task management built with **Python**, **Django**, **Django REST Framework**, **PostgreSQL**, and **Docker**.

This project is an MVP that provides user authentication and personal task management with filtering, search, ordering, and pagination.

---

## Features

### Authentication
- User registration
- User login
- Token-based authentication using DRF TokenAuthentication

### Tasks
- Create a task
- List user tasks
- Retrieve task details
- Update a task
- Delete a task

### Task Ownership
- Each task belongs to one user
- Each user can only view and manage their own tasks

### Filtering, Search, and Ordering
- Filter tasks by:
  - `status`
  - `priority`
  - `due_date`
- Search tasks by:
  - `title`
  - `description`
- Order tasks by:
  - `created_at`
  - `title`
  - `due_date`

### Pagination
- Page number pagination is enabled
- Default page size: `5`

### Database and Environment
- PostgreSQL database
- Dockerized development environment
- Environment variables managed with `.env`

---

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Docker Compose

---

## Project Structure

```bash
taskflow-api/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── users/
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md
Task Model Fields

Each task includes:

id
owner
title
description
status
priority
created_at
due_date
Status choices
todo
done
Priority choices
low
medium
high
API Endpoints
Authentication
Register
POST /api/users/register/

Example request body:

{
  "username": "ex",
  "email": "ex@example.com",
  "password": "yourpassword"
}
Login
POST /api/users/login/

Example request body:

{
  "username": "ex",
  "password": "yourpassword"
}

Example response:

{
  "token": "your_token_here",
  "username": "khalil",
  "email": "khalil@example.com"
}
Tasks
List tasks
GET /api/tasks/
Create task
POST /api/tasks/

Example request body:

{
  "title": "Finish Django project",
  "description": "Complete the MVP and test endpoints",
  "status": "todo",
  "priority": "high",
  "due_date": "2026-04-20"
}
Retrieve task details
GET /api/tasks/<id>/
Update task
PUT /api/tasks/<id>/
PATCH /api/tasks/<id>/
Delete task
DELETE /api/tasks/<id>/
Authentication Header

For protected endpoints, include the token in the request header:

Authorization: Token your_token_here
Query Parameters
Filtering
GET /api/tasks/?status=todo
GET /api/tasks/?priority=high
GET /api/tasks/?due_date=2026-04-20
Search
GET /api/tasks/?search=django
Ordering
GET /api/tasks/?ordering=title
GET /api/tasks/?ordering=-created_at
GET /api/tasks/?ordering=due_date
Running the Project with Docker
1. Create a .env file
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

POSTGRES_DB=taskflow
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123
POSTGRES_HOST=db
POSTGRES_PORT=5432
2. Build and run containers
docker compose up --build
3. Apply migrations
docker compose exec web python manage.py migrate
4. Create a superuser (optional)
docker compose exec web python manage.py createsuperuser
5. Open the app
http://localhost:8000/
Notes
This project is an MVP focused on backend fundamentals
Authentication is handled with DRF TokenAuthentication
All task endpoints are protected
Users can only access their own tasks
PostgreSQL data is persisted using a Docker volume
Future Improvements
Add automated tests
Add user profile endpoint
Add task status like in_progress
Add API documentation
Add JWT authentication
Prepare production settings
