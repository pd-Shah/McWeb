#!/usr/bin/env bash
echo 'powerd by @pd' &&
echo 'WARNING...' &&
echo 'A DEEP CLEANING HAS BEEN RANNING...' &&
echo 'PRESS CTL+C TO STOP' &&
source venv/bin/activate &&
pip install -r requirments.txt &&
python dropdb.py
