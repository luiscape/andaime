#!/bin/bash

#
#  Deploying local Python
#  virtual environment and installing
#  dependencies.
#
if [[ $CIRCLECI ]]
    then
    pyvenv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
fi
