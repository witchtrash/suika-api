# suika

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Requirements

Make sure to have Python 3.10 and poetry installed.

I recommend using [pyenv](https://github.com/pyenv/pyenv) to manage your Python versions.

Additionally, if you use Postgres, you need to have build dependencies for psycopg2 installed, usually `lib-pq` but this depends on which distro you're running. Consult your local swamp witch for detailed requirements.

## Setup

1. Spawn a shell with `poetry shell`
2. Install dependencies with `poetry install`
3. Copy `.env.example` to `.env` and update the settings
4. Run the migrations with `alembic upgrade head`
5. Run the API with `uvicorn suika.main:app`

## Testing

Tests are contained within the `/tests` folder, and use the `.env.testing` variables.

Run the tests with `pytest`

### Local and testing database

You can use the included `docker-compose` file to spin up a local postgres database. Start it with `docker-compose up -d` and go to `http://localhost:8001` to log into pgAdmin.

The default password and username can be found in the docker-compose file.

You can then connect to the database server with pgAdmin with the hostname `suika-db`. The user and password for the database server can also be found in the docker-compose file.
