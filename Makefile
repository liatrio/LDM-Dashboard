# Makefile for LDM Dashboard (Redis version)

.PHONY: db-up db-down db-testdata streamlit-up all

# Redis settings
db_container=ldm_redis
db_port=6379

# Start Redis with Docker
# Docker Compose targets
compose-up:
	docker-compose up -d

compose-down:
	docker-compose down

compose-build:
	docker-compose build

compose-logs:
	docker-compose logs -f

# Load test data into Redis (must be run from dashboard container or locally with Redis running)
db-testdata:
	python3 dashboard/redis_test_data_loader.py

# Full setup (compose up, test data)
all: compose-up db-testdata
