migrate:
	uv run alembic upgrade head

dev: 
	uvicorn app.main:app --host 0.0.0.0 --port 8000

