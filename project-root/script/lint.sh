#!/bin/bash
set -e

pip install pylint
pylint src/*.py tests/*.py --fail-under=8.0
