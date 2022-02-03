#!/bin/sh
set -e

pipenv lock -r > requirements.txt
docker build -t escobar0216/fastapi_saas_backend .

rm -f requirements.txt

echo "build done"
exec "$@"
