Displays a list of vaccinations available in different countries

# Getting started locally

Prerequisites:
- Docker Desktop (macOS and Windows) / Docker engine and docker-compose (Linux)
- Python 3

Configure development environment:
1. Run `pip install -r src/requirements-dev.txt`
1. Install pre-commit hook: `pre-commit install`
1. (Optional) run hook: `pre-commit run --all-files`

Running the app locally:
1. Start Docker Desktop / the daemon
1. While in the root directory of this project, run the database container: `docker compose up`
1. Run `src/backend/covid19/init.sql` to create the database
1. Move into the `covid19` directory: `cd src/backend/covid19`
1. Apply Django database migrations: `python manage.py migrate`
1. Start and run the development server: `python src/backend/covid19/manage.py runserver`

# Access database

To access the database via `http://127.0.0.1:8000/admin/`:
1. Create a superuser: `python manage.py createsuperuser`
1. Login using the username and password you created

To access psql of the running database container:
1. Find the container ID: `docker ps -a`
1. `docker exec -it <container_id> psql -U dbuser -d covid19 --password`
1. Enter in the database password: `dbpassword`
