#!/bin/sh
set -e
python -m smtpd -c DebuggingServer -n localhost:"$SMTP_PORT"
exec "$@"
