# Create PostgreSQL database in Docker container
docker run --name db_scrapad -p 5432:5432 -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=db_scrapad -d postgres

# Create Postgre GUI with pgAdmin
docker pull dpage/pgadmin4:latest
docker run --name pgadmin4 -p 5051:80 -e "PGADMIN_DEFAULT_EMAIL=inaki.garcianoya@gmail.com" -e "PGADMIN_DEFAULT_PASSWORD=password" -d dpage/pgadmin4

# Alembic commands
alembic upgrade head