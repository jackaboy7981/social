# Social

## Setup

1. Clone the repo.
2. Copy/verify environment values in `docker-compose.yml` (`DATABASE_URL`, Postgres credentials).
3. Build and start all services: `docker compose up --build`
4. Backend runs at `http://localhost:8000`, frontend at `http://localhost:8080`.
5. Postgres is available on the host at `localhost:5433`.
6. Apply database migrations: `cd backend && alembic upgrade head`

## Commands

### Docker

| Action | Command |
| --- | --- |
| Build and start all services | `docker compose up --build` |
| Build and start in the background | `docker compose up --build -d` |
| Stop all services | `docker compose down` |
| Tail logs | `docker compose logs -f` |
| Run a one-off command in the backend container | `docker compose run --rm backend <command>` |

### Database migrations (Alembic)

Run from `backend/`, with the venv active (`source .venv/bin/activate`):

| Action | Command |
| --- | --- |
| Create a migration from model changes | `alembic revision --autogenerate -m "<description>"` |
| Apply all pending migrations (upgrade to latest) | `alembic upgrade head` |
| Roll back one migration | `alembic downgrade -1` |
| Show current DB revision | `alembic current` |
| Show migration history | `alembic history` |
