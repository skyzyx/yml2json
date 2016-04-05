#! /usr/bin/env bash

for yml in $(find . -type f | grep -i yml); do
    out=$(echo $yml | sed -e 's/yml/json/')
    echo "$yml => $out"
    python ../yml2json/__init__.py $yml -p -o $out;
done;
