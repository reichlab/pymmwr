.PHONY: init
init:
	pip install pipenv --upgrade
	pipenv install --dev

.PHONY: test
test:
	pipenv run pytest ./tests.py
	pipenv run mypy ./pymmwr.py

.PHONY: publish
publish:
	pipenv run python setup.py sdist
	pipenv run twine upload dist/*
	rm -rf build dist
