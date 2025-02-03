#!/bin/bash

echo "Running Uvicorn Server"

uvicorn main:app --host 0.0.0.0
