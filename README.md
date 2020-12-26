# Authenticated Full-Stack Streamlit

### Purpose
Basic

### Authentication
The nginx project.conf file puts everything behind basic htpasswd authentication by including this in the top "server" block:

    auth_basic "closed site";
    auth_basic_user_file /nginx/auth/.htpasswd;

## how to make an htpasswd
You need to install apache2-utils
    sh sudo apt update
    sh sudo apt install apache2-utils

### Env Files
API, PGAdmin4, and Postgres each have ".env.template" files that you'll use to create your own ".env" files in each corresponding subdirectory. The ".env" files themselves are .gitignore'd

## Guides Referenced when Building This

### Alembic
When you run your first alembic migration, type this:
    docker-compose run [service name] alembic revision --autogenerate -m "First migration"

And when you make other revisions you can just type in:
    docker-compose run [service name] alembic revision --autogenerate

replace [service name] with the docker-compose service name. In this case, it's called "api" per docker-compose.yaml in the top directory

[Reference I used to learn alembic in this context](https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396)

### FastAPI Quirks
1. [How to get openapi.json to load, required for the /docs/ endpoint](https://github.com/tiangolo/fastapi/issues/102#issuecomment-739520277)
2. [But also need to define root-path="/api/v1" for /docs to work](https://fastapi.tiangolo.com/advanced/behind-a-proxy/)

### PGAdmin4 References when Setting This Up:
Connect to postgres server in pgadmin(ctrl+f for "connect to a database server,": https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396

- [Fully comprehensive, did this one first. But also see below. Nginx should port_forward to 80, not 5050, for the GUI](https://www.enterprisedb.com/postgres-tutorials/reverse-proxying-pgadmin)
- [But needs to do the port 80 in nginx config, not the 5050 for me to use it](https://stackoverflow.com/questions/61802782/reverse-proxy-in-docker-using-nginx-for-pgadmin4)
