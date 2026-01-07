#!/bin/bash

/usr/bin/supervisord &

sleep 3

cd /app
python3 BetaFintrack.py