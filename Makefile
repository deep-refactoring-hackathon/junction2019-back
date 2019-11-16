.PHONY: venv
venv:
	python -m venv venv
	venv/bin/pip install -U pip
	venv/bin/pip install -r requirements.txt
