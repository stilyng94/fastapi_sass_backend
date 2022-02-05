#!/bin/sh
set -e
celery -A app.worker worker -l info
exec "$@"
