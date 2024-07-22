#!/usr/bin/env bash

openssl genrsa -out ./certs/private.pem 2048
openssl rsa -in ./certs/private.pem -outform PEM -pubout -out ./certs/public.pem

alembic upgrade head

exec "$@"