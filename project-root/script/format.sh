#!/bin/bash
set -e

pip install black
black --check src/ tests/

