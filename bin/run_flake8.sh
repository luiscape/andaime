#!/bin/bash

#
#  Running PEP8 linter.
#
echo 'Running flake8: Python linter.'
source venv/bin/activate
    flake8 --ignore=D300,D400,D205,D200,E501 ui
    flake8 --ignore=D300,D400,D205,D200,E501,F403 andaime
    flake8 --ignore=D300,D400,D205,D200,D301,E501,D401 cli.py
    flake8 --ignore=D300,D400,D205,D200,D301,D401,E501,E721,E501 tests
deactivate
echo 'flake8 has completed all checks.'