code/lint:
	mypy . && black --check . && flake8 .

code/test:
	pytest .

make run:
	python ./code/main.py

PHONY: test
