PIP := venv/bin/pip
PYTHON3 := venv/bin/python3
TESTS_PATH := tests.py

install_requirements:
	${PIP} install -r requirements.txt

run:
	${PYTHON3} runner.py

test:
	${PYTHON3} ${TESTS_PATH}
