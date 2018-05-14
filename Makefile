.PHONY: init
init:
	pip install pipenv --upgrade
	pipenv install --dev

.PHONY: test
test:
	pipenv run python -m pytest ./tests
	pipenv run mypy ./pymmwr.py

.PHONY: publish
publish:
	pipenv run python setup.py sdist
	pipenv run twine upload dist/*
	rm -rf build dist
