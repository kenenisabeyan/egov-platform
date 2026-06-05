#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.accounts.models import User

try:
    user = User.objects.create_user(
        username='demo',
        email='demo@test.com',
        phone='+251900123456',
        password='password123'
    )
    print(f"✓ User created: {user.username} | {user.email} | {user.phone}")
except Exception as e:
    print(f"✗ Error: {e}")
