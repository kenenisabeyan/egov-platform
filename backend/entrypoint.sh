#!/bin/sh
python manage.py migrate_schemas --shared
python manage.py create_tenant_schemas
python manage.py collectstatic --noinput
exec "$@"