#!/bin/sh
set -e

pipenv lock -r > requirements.txt

docker build -t escobar0216/fastapi_saas_backend .

echo "build done"
exec "$@"
