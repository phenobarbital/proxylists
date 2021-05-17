.venv:
	python3.8 -m venv .venv
	source .venv/bin/activate && make setup dev
	echo 'run `source .venv/bin/activate` to start develop asyncDB'

venv: .venv

setup:
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

distclean: clean
	rm -rf .venv
