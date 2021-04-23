#!/bin/bash

gunicorn -c ../config.py --reload app:app