#!/usr/bin/env bash
# exit on error
set -o errexit

uvicorn main:app --host 0.0.0.0 --port 80
