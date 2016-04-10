all:
	@cat Makefile | grep : | grep -v PHONY | grep -v @ | sed 's/:/ /' | awk '{print $$1}' | sort

#-------------------------------------------------------------------------------

.PHONY: build
build:
	python setup.py sdist
	python setup.py bdist_wheel

.PHONY: readme
readme:
	pandoc -r markdown_github -w rst -o README.rst README.md

.PHONY: push
push:
	twine upload dist/*

.PHONY: clean
clean:
	rm -Rf **/*.pyc build/ dist/ docs/ yml2json.egg-info/

.PHONY: test
test:
	pip install -e .
	nose2
