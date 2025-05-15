# Makefile for LDM Dashboard (Redis version)

.PHONY: db-up db-down db-testdata streamlit-up all

# Redis settings
db_container=ldm_redis
db_port=6379

# Start Redis with Docker
db-up:
	docker run --rm -d --name $(db_container) -p $(db_port):6379 redis:7

# Stop Redis
db-down:
	docker stop $(db_container)

# Load test data into Redis
db-testdata:
	python3 redis_test_data_loader.py

# Run Streamlit app
streamlit-up:
	streamlit run streamlit_app.py

# Full setup (db, test data, streamlit)
all: db-up db-testdata streamlit-up
