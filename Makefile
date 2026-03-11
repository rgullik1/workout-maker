.PHONY: run format check commitizen-check pre-commit-install pre-commit

commitizen-check:
	uv run cz check -m "$(shell git log -1 --pretty=%B)"

pre-commit-install:
	uv run pre-commit install

pre-commit:
	uv run pre-commit run --all-files

run:
	cd src && uvicorn interface.app:app --reload

format:
	uv run ruff check --fix src/
	uv run ruff format src/

check:
	uv run pyright src
