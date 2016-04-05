#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Convert YAML to JSON

@author: Ryan Parman <ryan@ryanparman.com>
"""

from __future__ import print_function
import argparse
import datetime
import dateutil.parser
import json
import sys
import yaml

# -----------------------------------------------------------------------------

class JsonTimeEncoder(json.JSONEncoder):
    """
    Converts datetime objects into strings for JSON.
    """
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            if int(obj.strftime('%f')) is 0:
                return obj.strftime('%Y-%m-%dT%H:%M:%S%z')
            else:
                return obj.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

# -----------------------------------------------------------------------------

def timestamp_constructor(loader, node):
    return dateutil.parser.parse(node.value)

def main():
    # Available CLI flags.
    parser = argparse.ArgumentParser(
        description="Convert YAML to JSON.",
    )

    parser.add_argument(
        "input",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="The YAML file to use as input.")

    parser.add_argument(
        "-o", "--output",
        help="The JSON file to use as output. If not set, will output to STDOUT.")

    parser.add_argument(
        "-p", "--pretty",
        dest='pretty',
        action='store_true',
        help="By default, the JSON is unprettified. This will enable prettification.")

    parser.set_defaults(pretty=False)

    flags = parser.parse_args()

    if flags.output:
        with open(flags.output, 'w') as outfile:
            if flags.pretty:
                json.dump(
                    yaml.load(flags.input.read()),
                    outfile,
                    # sort_keys=True,
                    indent=4,
                    separators=(',', ': '),
                    cls=JsonTimeEncoder
                )
            else:
                json.dump(
                    yaml.load(flags.input.read()),
                    outfile,
                    cls=JsonTimeEncoder
                )
    else:
        if flags.pretty:
            print(json.dumps(
                yaml.load(flags.input.read()),
                # sort_keys=True,
                indent=4,
                separators=(',', ': '),
                cls=JsonTimeEncoder
            ))
        else:
            print(json.dumps(
                yaml.load(flags.input.read()),
                cls=JsonTimeEncoder
            ))

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    yaml.add_constructor(u'tag:yaml.org,2002:timestamp', timestamp_constructor)
    main()
