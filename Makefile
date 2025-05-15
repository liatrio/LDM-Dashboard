# Makefile for LDM Dashboard

.PHONY: db-up db-down db-init db-testdata streamlit-up all

# Database settings
db_container=ldm_pg
db_user=ldm_user
db_pass=ldm_pass
db_name=ldm_db
db_port=5432

# Start Postgres with Docker
db-up:
	docker run --rm -d --name $(db_container) -e POSTGRES_USER=$(db_user) -e POSTGRES_PASSWORD=$(db_pass) -e POSTGRES_DB=$(db_name) -p $(db_port):5432 postgres:15

# Stop Postgres
 db-down:
	docker stop $(db_container)

# Wait for Postgres to be available
wait-for-db:
	@echo "Waiting for database to be ready..."; \
	for i in `seq 1 20`; do \
		PGPASSWORD=$(db_pass) psql -h localhost -U $(db_user) -d $(db_name) -p $(db_port) -c "\q" 2>/dev/null && break; \
		echo "Waiting... ($$i)"; \
		sleep 1; \
	done

# Initialize DB schema
db-init: wait-for-db
	PGPASSWORD=$(db_pass) psql -h localhost -U $(db_user) -d $(db_name) -p $(db_port) -f db_schema.sql

# Populate DB with test data
db-testdata: wait-for-db
	PGPASSWORD=$(db_pass) psql -h localhost -U $(db_user) -d $(db_name) -p $(db_port) -f db_test_data.sql

# Run Streamlit app
streamlit-up:
	streamlit run streamlit_app.py

# Full setup (db, schema, test data, streamlit)
all: db-up db-init db-testdata streamlit-up
