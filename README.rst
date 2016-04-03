yaml2json
=========

| |Source|
| |Open Issues|
| |Author|

Converts YAML input to JSON output.

Examples
--------

.. code:: bash

    yaml2json sample.yml
    yaml2json sample.yml --pretty
    yaml2json sample.yml --output sample.json
    yaml2json sample.yml --output sample.json --pretty

    cat sample.yml | yaml2json
    cat sample.yml | yaml2json --pretty
    cat sample.yml | yaml2json --output sample.json
    cat sample.yml | yaml2json --output sample.json --pretty

Installation
------------

Using Pip:

.. code:: bash

    pip install yaml2json

GPG Signing
-----------

Each release (i.e., git tag) is GPG-signed. You can easily verify the
contents using `Keybase <https://keybase.io>`__.

.. code:: bash

    keybase dir verify

If you're more familiar with traditional GPG signing, view ``SIGNED.md``
for the information you need to do the verification.

Contributing
------------

Here's the process for contributing:

#. Fork yaml2json to your GitHub account.
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
`contributors <https://github.com/skyzyx/yaml2json/contributors>`__ who
participated in this project.

Licensed for use under the terms of the
`MIT <http://www.opensource.org/licenses/mit-license.php>`__ license.

.. |Source| image:: http://img.shields.io/badge/source-skyzyx/yaml2json-blue.svg?style=flat-square
   :target: https://github.com/skyzyx/yaml2json
.. |Open Issues| image:: http://img.shields.io/github/issues/skyzyx/yaml2json.svg?style=flat-square
   :target: https://github.com/skyzyx/yaml2json/issues
.. |Author| image:: http://img.shields.io/badge/author-@skyzyx-blue.svg?style=flat-square
   :target: https://twitter.com/skyzyx
