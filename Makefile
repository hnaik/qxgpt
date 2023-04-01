.PHONY: black
format:
	python -m black

.PHONY: jupyter
jupyter:
	python -m jupyter lab --notebook-dir=./nb

.PHONY: pip-refresh
pip-update:
	python -m pip install --upgrade -r requirements.txt

.PHONY: test
test:
	python -m pytest -s

