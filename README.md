# Todo Apps API

A RESTful Todo API built with **FastAPI**, **SQLModel**, and **SQLite**, featuring full CRUD operations, input validation, and database migrations.

## Tech Stack

- **FastAPI** — High-performance async web framework
- **SQLModel** — SQL database ORM (SQLAlchemy + Pydantic)
- **Alembic** — Database migrations
- **SQLite** — Lightweight relational database
- **Pydantic** — Data validation and settings management
- **Uvicorn** — ASGI server

## Features

- Create, Read, Update, and Delete todos
- UUID-based primary keys
- Enum-based status tracking (`pending`, `ongoing`, `done`)
- Input validation with Pydantic schemas
- Partial updates (only update provided fields)
- Pagination support via query parameters
- API versioning (`/api/v1`)
- Interactive API docs (Swagger UI at `/docs`, Scalar at `/scalar`)
- Database migrations with Alembic

## Getting Started

### Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/todo-apps.git
   cd todo-apps/backend
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   uv venv
   uv sync
   ```

   Or with pip:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Copy the environment file and configure it:

   ```bash
   cp .env.example .env
   ```

4. Run database migrations:

   ```bash
   alembic upgrade head
   ```

5. Start the development server:
   ```bash
   make dev
   ```
   Or directly:
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`.

## API Endpoints

| Method   | Endpoint            | Description       |
| -------- | ------------------- | ----------------- |
| `GET`    | `/api/v1/todo/`     | List all todos    |
| `GET`    | `/api/v1/todo/{id}` | Get a todo by ID  |
| `POST`   | `/api/v1/todo/`     | Create a new todo |
| `PUT`    | `/api/v1/todo/{id}` | Update a todo     |
| `DELETE` | `/api/v1/todo/{id}` | Delete a todo     |

### Documentation

- Swagger UI: `http://localhost:8000/docs`
- Scalar: `http://localhost:8000/scalar`

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── core/
│   │   └── settings.py      # App configuration & environment variables
│   ├── models/
│   │   ├── database.py      # SQLModel database models
│   │   └── engine.py        # Database engine & session
│   ├── router/
│   │   └── todo.py          # API route handlers
│   ├── schema/
│   │   └── todo.py          # Request/Response schemas
│   └── utils/
│       ├── list_status.py   # Status enum definition
│       └── standard_query_param.py
├── alembic/                  # Database migrations
├── alembic.ini
├── pyproject.toml
└── Makefile
```

## License

This project is open source and available under the [MIT License](LICENSE).
