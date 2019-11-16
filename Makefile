.PHONY: venv
venv:
	python3 -m venv venv
	venv/bin/pip install -U pip
	venv/bin/pip install -r requirements.txt

docker/dev/up:
	docker-compose --project-directory . -f ./deployments/dev/docker-compose.yml up --build

docker/dev/up/silent:
	docker-compose --project-directory . -f ./deployments/dev/docker-compose.yml up --build -d

docker/dev/down:
	docker-compose --project-directory . -f ./deployments/dev/docker-compose.yml down
