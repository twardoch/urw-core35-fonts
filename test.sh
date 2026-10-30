#!/bin/sh
# this_file: test.sh
set -eu
cd "$(dirname "$0")"
exec uv run --with 'fonttools>=4.50' python -m unittest discover -s tests -v
