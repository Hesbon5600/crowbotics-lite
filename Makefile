#@-- help command to show usage of make commands --@#
help:
	@echo "----------------------------------------------------------------------------"
	@echo "-                     Available commands                                   -"
	@echo "----------------------------------------------------------------------------"
	@echo "---> make activate         - To activate virtual environment"
	@echo "---> make install          - To install dependencies from Pipfile.lock"
	@echo "---> make update           - To update the Pipfile.lock"
	@echo "---> make makemigrations   - To create a migration file for the changes in the models"
	@echo "---> make migrate          - To update the database with the latest migration"
	@echo "---> make run              - To start the server"
	@echo " "


activate:
	@ echo '<<<<<<<<<<creating virtual environment>>>>>>>>>'
	poetry shell
	@ echo ''


install:
	@ echo '<<<<<<<<<<installing requirements>>>>>>>>>'
	poetry install
	@ echo ''

makemigrations:
	@ echo '<<<<<<<<<<creating migrations>>>>>>>>>'
	python manage.py makemigrations
	@ echo ''

migrate:
	@ echo '<<<<<<<<<<creating migrations>>>>>>>>>'
	python manage.py migrate
	@ echo ''

run:
	@ echo '<<<<<<<<<<starting server>>>>>>>>>'
	python manage.py runserver
	@ echo ''

default: help
