PROJECT_DIR=chat

format:
	ruff format $(PROJECT_DIR)
	@isort $(PROJECT_DIR)