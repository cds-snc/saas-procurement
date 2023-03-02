.PHONY: fmt install install-dev migration migrate superuser run lint test fmt-ci lint-ci

fmt:
	black . $(ARGS) --target-version py310

install:
	pip3 install --user -r requirements.txt

install-dev:
	pip3 install --user -r requirements_dev.txt

migrate:
	python3 manage.py migrate

migration:
	python3 manage.py makemigrations

superuser:
	python3 manage.py createsuperuser

run:
	python manage.py runserver

lint:
	flake8 .

test:
	python manage.py test

lint-ci:
	flake8 .

fmt-ci:
	black --check . --target-version py310
