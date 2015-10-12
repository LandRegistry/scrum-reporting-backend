#!/usr/bin/env bash

if [ "$1" = "-d" ]
  then
  source ./environment.sh
  python run.py
else
  gunicorn --log-file=- --log-level DEBUG -b 0.0.0.0:5000 --timeout 120 application.server:app
fi
