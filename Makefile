.PHONY: docs
.PHONY: list
.PHONY: lint
.PHONY: upload
.PHONY: venv
.PHONY: venv3
.PHONY: active
.PHONY: active3
.PHONY: dev
.PHONY: dev3
.PHONY: tox
.PHONY: cov
.PHONY: covhtml

list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs

active3: #run surrounded by backticks
	. .venv/bin/activate

active: #run surrounded by backticks
	. .virtualenv/bin/activate

dev:
	python27 setup.py develop

dev3:
	python3 setup.py develop

venv:
	virtualenv .virtualenv
	.virtualenv/bin/pip install -e .
	.virtualenv/bin/pip install -r requirements.txt

venv3:
	python3 -m venv .venv
	.venv/bin/pip install -e .
	.venv/bin/pip install -r requirements.txt

test:
	pytest

lint:
	pylint --ignore=test nyc-mt-cc

cov:
	py.test --cov=nyc-mt-cc nyc-mt-cc/test/

covhtml:
	py.test --cov-report html:docs/cov --cov=nyc-mt-cc nyc-mt-cc/test/

upload: docs
	python setup.py sdist upload

docs:
	python setup.py build_sphinx --build-dir docs

tox:
	tox
