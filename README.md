To easily update database records, go to http://127.0.0.1:8000/admin/

# Setup

Prerequisites:
- PostgreSQL
- Python 3

Configure development environment:
1. Run `pip install -r src/requirements-dev.txt`
1. Install pre-commit hook: `pre-commit install`
1. (Optional) run hook: `pre-commit run --all-files`

To run locally:

1. Run `src/backend/covid19/init.sql` to create the database
1. Start and run the development server: `python src/backend/covid19/manage.py runserver`
