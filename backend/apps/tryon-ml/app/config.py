# Centralize environment and filesystem setup for the ML service. This includes:
# - Debug mode flag
# - Base directory for all files related to the ML service
# - Subdirectories for input, output, and debug files


# TODO: 
# swap /tmp → /data
# disable debug artifacts
# mount volumes in Docker


import os

DEBUG_MODE = True

BASE_DIR = "/tmp/tryon"
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
DEBUG_DIR = os.path.join(BASE_DIR, "debug")

for d in [INPUT_DIR, OUTPUT_DIR, DEBUG_DIR]:
    os.makedirs(d, exist_ok=True)
