code/lint:
	mypy ./game ./test && black --check . && flake8 .

code/test:
	pytest .

make run:
	python ./code/main.py

PHONY: test
