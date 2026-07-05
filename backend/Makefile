.PHONY: help install sync run dev test lint format check clean

help:
	@echo "Available commands:"
	@echo "  make install  - Install dependencies"
	@echo "  make sync     - Sync dependencies"
	@echo "  make run      - Run FastAPI"
	@echo "  make dev      - Run FastAPI with auto reload"
	@echo "  make test     - Run tests"
	@echo "  make lint     - Run linter"
	@echo "  make format   - Format code"
	@echo "  make check    - Run formatting + lint + tests"
	@echo "  make clean    - Remove cache files"

install:
	uv sync

sync:
	uv sync

run:
	uv run uvicorn app.main:app

dev:
	uv run uvicorn app.main:app --reload

test:
	uv run pytest

lint:
	uv run ruff check .

format:
	uv run ruff format .

check:
	uv run ruff format --check .
	uv run ruff check .
	uv run pytest

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +