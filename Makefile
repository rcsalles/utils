PROJECT_NAME := ssh-utils
PYTHON_VERSION := 3.6.6
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

my-on:
	python create_tunnel.py --user=SSH_USER --host=SSH_HOST --port=SSH_PORT --turn=on

on:
	python create_tunnel.py --turn=on

off:
	python create_tunnel.py --turn=off

setup:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)
	pip install -r requirements.txt
