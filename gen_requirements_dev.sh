#!/bin/sh
set -e

pipenv lock -r --dev > requirements.txt
docker build -f Dockerfile-dev -t escobar0216/fastapi_saas_backend_dev .
rm -f requirements.txt

echo "build done"
exec "$@"
