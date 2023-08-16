#!/bin/bash
set -e
python3 -m interference.app &
python3 gui_app.py
tail -f /dev/null