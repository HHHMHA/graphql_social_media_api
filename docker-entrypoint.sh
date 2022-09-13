#!/usr/bin/env bash

python3 manage.py migrate
python3 manage.py loaddata users.json
python3 manage.py loaddata posts.json
python3 manage.py runserver 0:8000
