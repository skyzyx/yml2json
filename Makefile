all:
	@cat Makefile | grep : | grep -v PHONY | grep -v @ | sed 's/:/ /' | awk '{print $$1}' | sort

#-------------------------------------------------------------------------------

.PHONY: build
build:
	python setup.py sdist
	python setup.py bdist_wheel
	cp pkginfo.txt yml2json.egg-info/PKG-INFO

.PHONY: readme
readme:
	pandoc -r markdown_github -w rst -o README.rst README.md

.PHONY: push
push:
	twine upload dist/*
