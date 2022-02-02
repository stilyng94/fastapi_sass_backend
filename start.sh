#!/bin/sh
set -e

uvicorn app.main:create_app --reload --host=0.0.0.0 --port=80 --factory
exec "$@"
