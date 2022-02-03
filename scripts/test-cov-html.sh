#!/bin/sh
set -e
set -x

sh scripts/test.sh --cov-report=html "${@}"
