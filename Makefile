PROJECT_DIR=chat

install-docker:

format:
	ruff format $(PROJECT_DIR)
	@isort $(PROJECT_DIR)

run:
	docker compose up --build
