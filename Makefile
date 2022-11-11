dev:
	pip install -r backend/requirements.txt
	cd frontend && yarn install --dev

migrate:
	python backend/manage.py makemigrations
	python backend/manage.py migrate

run:
	yarn --cwd front start & python backend/manage.py runserver