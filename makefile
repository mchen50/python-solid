SHELL := /bin/bash

.ONESHELL:

setup: clean install

install:
	python -m venv venv; \
	source venv/bin/activate; \
	pip install -r requirements.txt \

test: clean
	source venv/bin/activate; \
	pytest tests/

clean-all: clean
	rm -rf venv; 

clean:
	rm -rf .coverage; \
	rm -rf .pytest_cache; \
	rm -rf tests/.pytest_cache; \
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

check-format:
	source venv/bin/activate; \
	black --check --diff .

format:
	source venv/bin/activate; \
	black .