PIP := venv/bin/pip
PYTHON3 := venv/bin/python3
TESTS_PATH := tests.py

clear:
	rm -rf venv

venv:
	python3 -m venv venv

install_requirements:
	${PIP} install -r requirements.txt

run:
	${PYTHON3} runner.py

test:
	${PYTHON3} ${TESTS_PATH}

up_service:
	make clear
	make venv
	make install_requirements
	make run
