yml2json
========

| |Source|
| |Open Issues|
| |Author|

Converts YAML input to JSON output.

Examples
--------

.. code:: bash

    yml2json sample.yml
    yml2json sample.yml --pretty
    yml2json sample.yml --output sample.json
    yml2json sample.yml --output sample.json --pretty

    cat sample.yml | yml2json
    cat sample.yml | yml2json --pretty
    cat sample.yml | yml2json --output sample.json
    cat sample.yml | yml2json --output sample.json --pretty

Installation
------------

Using `Pip <https://pypi.python.org/pypi/yml2json>`__:

.. code:: bash

    pip install yml2json

Developing
----------

First, install `VirtualEnv <https://virtualenv.pypa.io>`__.

.. code:: bash

    pip install --upgrade virtualenv

Next, activate your virtual environment and install the dependencies.

.. code:: bash

    virtualenv vendor && \
    source vendor/bin/activate && \
    pip install -r requirements.txt

Contributing
------------

Here's the process for contributing:

#. Fork yml2json to your GitHub account.
#. Clone your GitHub copy of the repository into your local workspace.
#. Write code, fix bugs, and add tests with 100% code coverage.
#. Commit your changes to your local workspace and push them up to your
   GitHub copy.
#. You submit a GitHub pull request with a description of what the
   change is.
#. The contribution is reviewed. Maybe there will be some banter
   back-and-forth in the comments.
#. If all goes well, your pull request will be accepted and your changes
   are merged in.

Authors, Copyright & Licensing
------------------------------

-  Copyright (c) 2016 `Ryan Parman <http://ryanparman.com>`__.

See also the list of
`contributors <https://github.com/skyzyx/yml2json/contributors>`__ who
participated in this project.

Licensed for use under the terms of the
`MIT <http://www.opensource.org/licenses/mit-license.php>`__ license.

.. |Source| image:: http://img.shields.io/badge/source-skyzyx/yml2json-blue.svg?style=flat-square
   :target: https://github.com/skyzyx/yml2json
.. |Open Issues| image:: http://img.shields.io/github/issues/skyzyx/yml2json.svg?style=flat-square
   :target: https://github.com/skyzyx/yml2json/issues
.. |Author| image:: http://img.shields.io/badge/author-@skyzyx-blue.svg?style=flat-square
   :target: https://twitter.com/skyzyx
