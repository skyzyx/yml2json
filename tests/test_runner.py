#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import glob
import string
import yml2json

# -----------------------------------------------------------------------------

def test_actual_vs_expected():
    yaml_files = glob.glob("tests/samples/*.yml")

    for yf in yaml_files:
        with open(yf, 'r') as yaml:
            actual = yml2json.pretty_output(yaml.read())

        with open(string.replace(yf, 'yml', 'json'), 'r') as json:
            expected = json.read()

        print(yf)

        try:
            assert actual == expected
        except Exception as e:
            print("--------")
            print(actual)
            print(expected)
            print("--------")
            raise e

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    test_actual_vs_expected()
