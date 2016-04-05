# yml2json

[![Source](http://img.shields.io/badge/source-skyzyx/yml2json-blue.svg?style=flat-square)](https://github.com/skyzyx/yml2json)
[![Open Issues](http://img.shields.io/github/issues/skyzyx/yml2json.svg?style=flat-square)](https://github.com/skyzyx/yml2json/issues)
[![Author](http://img.shields.io/badge/author-@skyzyx-blue.svg?style=flat-square)](https://twitter.com/skyzyx)

Converts YAML input to JSON output. Relies on [PyYaml](http://pyyaml.org/wiki/PyYAML), which supports [YAML 1.0](http://yaml.org/spec/1.0/) and [1.1](http://yaml.org/spec/1.1/), but not [1.2](http://www.yaml.org/spec/1.2/spec.html).


## Examples

```bash
yml2json sample.yml
yml2json sample.yml --pretty
yml2json sample.yml --output sample.json
yml2json sample.yml --output sample.json --pretty

cat sample.yml | yml2json
cat sample.yml | yml2json --pretty
cat sample.yml | yml2json --output sample.json
cat sample.yml | yml2json --output sample.json --pretty
```

## Installation

Using [Pip](https://pypi.python.org/pypi/yml2json):
```bash
pip install yml2json
```

## Developing

First, install [VirtualEnv](https://virtualenv.pypa.io).

```bash
pip install --upgrade virtualenv
```

Next, activate your virtual environment and install the dependencies.

```bash
virtualenv vendor && \
source vendor/bin/activate && \
pip install -r requirements.txt && \
pip install -r requirements2.txt
```

## Contributing
Here's the process for contributing:

1. Fork yml2json to your GitHub account.
2. Clone your GitHub copy of the repository into your local workspace.
3. Write code, fix bugs, and add tests with 100% code coverage.
4. Commit your changes to your local workspace and push them up to your GitHub copy.
5. You submit a GitHub pull request with a description of what the change is.
6. The contribution is reviewed. Maybe there will be some banter back-and-forth in the comments.
7. If all goes well, your pull request will be accepted and your changes are merged in.


## Authors, Copyright & Licensing

* Copyright (c) 2016 [Ryan Parman](http://ryanparman.com).

See also the list of [contributors](https://github.com/skyzyx/yml2json/contributors) who participated in this project.

Licensed for use under the terms of the [MIT] license.

  [MIT]: http://www.opensource.org/licenses/mit-license.php
