#!/bin/bash
python3 -m venv env_python
source env_python/bin/activate
if [ $VIRTUAL_ENV ]; then
    pip install -r requirements.txt
else
    echo "The venv couldn't be created"
fi