# Create PostgreSQL database in Docker container
docker run --name db_scrapad -p 5432:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_DB=scrapad -d postgres

      