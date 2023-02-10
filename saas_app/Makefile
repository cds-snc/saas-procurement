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

shell:
	python3 manage.py shell

run:
	python manage.py runserver

lint:
	flake8 .

test:
	coverage run -m pytest -s -vv tests &&\
	coverage report -m

lint-ci:
	flake8 .

fmt-ci:
	black --check . --target-version py310
