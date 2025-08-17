.PHONY: up down test fmt

up:
	docker compose up --build

down:
	docker compose down -v

test:
	docker compose run --rm backend pytest -q

fmt:
	docker compose run --rm backend ruff format .
