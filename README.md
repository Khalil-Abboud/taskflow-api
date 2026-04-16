# TaskFlow API

TaskFlow API is a backend REST API for task management built with **Python**, **Django**, **Django REST Framework**, **PostgreSQL**, and **Docker**.

This project is an MVP that provides user authentication and personal task management with filtering, search, ordering, pagination, and basic automated testing.

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
    │   ├── urls.py
    │   └── tests.py
    ├── users/
    │   ├── serializers.py
    │   ├── views.py
    │   ├── urls.py
    │   └── tests.py
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    ├── manage.py
    └── README.md

---

## Task Model Fields

Each task includes:

- `id`
- `owner`
- `title`
- `description`
- `status`
- `priority`
- `created_at`
- `due_date`

### Status choices
- `todo`
- `done`

### Priority choices
- `low`
- `medium`
- `high`

---

## API Endpoints

### Authentication

#### Register

`POST /api/users/register/`

Example request body:

    {
      "username": "testuser",
      "email": "user@example.com",
      "password": "yourpassword123"
    }

#### Login

`POST /api/users/login/`

Example request body:

    {
      "username": "testuser",
      "password": "yourpassword123"
    }

Example response:

    {
      "token": "your_token_here",
      "username": "testuser",
      "email": "user@example.com"
    }

---

### Tasks

#### List tasks

`GET /api/tasks/`

#### Create task

`POST /api/tasks/`

Example request body:

    {
      "title": "Finish Django project",
      "description": "Complete the MVP and test endpoints",
      "status": "todo",
      "priority": "high",
      "due_date": "2026-04-20"
    }

#### Retrieve task

`GET /api/tasks/<id>/`

#### Update task

`PUT /api/tasks/<id>/`  
`PATCH /api/tasks/<id>/`

#### Delete task

`DELETE /api/tasks/<id>/`

---

## Authentication Header

`Authorization: Token your_token_here`

---

## Query Examples

### Filtering

`GET /api/tasks/?status=todo`  
`GET /api/tasks/?priority=high`  
`GET /api/tasks/?due_date=2026-04-20`

### Search

`GET /api/tasks/?search=django`

### Ordering

`GET /api/tasks/?ordering=title`  
`GET /api/tasks/?ordering=-created_at`  
`GET /api/tasks/?ordering=due_date`

---

## Running with Docker

### 1. Create `.env`

    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost

    POSTGRES_DB=your_db_name
    POSTGRES_USER=your_db_user
    POSTGRES_PASSWORD=your_db_password
    POSTGRES_HOST=your_db_host
    POSTGRES_PORT=your_db_port

### 2. Run project

`docker compose up --build`

### 3. Apply migrations

`docker compose exec web python manage.py migrate`

### 4. Create superuser (optional)

`docker compose exec web python manage.py createsuperuser`

### 5. Open in browser

`http://localhost:8000/`

---

## Tests

Run automated tests:

`docker compose exec web python manage.py test`

The project includes tests for:
- User registration
- User login
- Task creation
- Task ownership isolation
- Permission checks

---

## Notes

- This is an MVP backend project
- Uses DRF TokenAuthentication
- All task endpoints require authentication
- Users can only access their own tasks
- PostgreSQL data is persisted with a Docker volume

---

## Future Improvements

- Add more advanced tests
- Add user profile endpoint
- Add `in_progress` status
- Add API documentation (Swagger)
- Switch to JWT authentication
- Prepare production settings