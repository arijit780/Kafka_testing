PYTHON=python3
VENV=.venv

.PHONY: up down logs venv install run-producer run-consumer

up:
	@docker-compose up -d

down:
	@docker-compose down

logs:
	@docker-compose logs -f kafka

venv:
	@$(PYTHON) -m venv $(VENV)
	@echo "Created venv at $(VENV). Activate with 'source $(VENV)/bin/activate'"

install: venv
	@$(VENV)/bin/pip install -r requirements.txt

run-producer:
	@$(PYTHON) producer.py

run-consumer:
	@$(PYTHON) consumer.py
