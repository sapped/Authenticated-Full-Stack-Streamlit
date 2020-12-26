# Authenticated Full-Stack Streamlit

### Purpose
Basic

### Authentication
The nginx project.conf file puts everything behind basic htpasswd authentication by including this in the top "server" block:

    auth_basic "closed site";
    auth_basic_user_file /nginx/auth/.htpasswd;

### Env Files
API, PGAdmin4, and Postgres each have ".env.template" files that you'll use to create your own ".env" files in each corresponding subdirectory. The ".env" files themselves are .gitignore'd


### Alembic
When you run your first alembic migration, type this:
    docker-compose run [service name] alembic revision --autogenerate -m "First migration"

And when you make other revisions you can just type in:
    docker-compose run [service name] alembic revision --autogenerate

replace [service name] with the docker-compose service name. In this case, it's called "api" per docker-compose.yaml in the top directory