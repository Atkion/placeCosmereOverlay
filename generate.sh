#!/usr/bin/env bash

python -m venv venv

source venv/bin/activate

pip install -r generator/requirements.txt

python generator/generator.py
