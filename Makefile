venv:
	python3.9 -m venv .venv
	echo 'run `source .venv/bin/activate` to start develop asyncDB'

develop:
	pip install wheel==0.37.0
	pip install -e .
	python -m pip install -Ur docs/requirements.txt

dev:
	flit install --symlink

release: lint test clean
	flit publish

format:
	python -m black proxylist

lint:
	python -m pylint --rcfile .pylint proxylist/*.py
	python -m black --check proxylist

test:
	python -m coverage run -m tests
	python -m coverage report
	python -m mypy proxylist/*.py
	python -m mypy proxylist/proxies/*.py

distclean:
	rm -rf .venv
