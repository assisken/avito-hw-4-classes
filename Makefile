PYTHON='python3'

test:
	${PYTHON} -m pytest tests

coverage:
	${PYTHON} -m pytest --cov=. --cov-config=setup.cfg tests
