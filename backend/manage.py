#!/usr/bin/env python
import os
import sys

def main():
    try:
        from dotenv import load_dotenv
        # .env is located in the parent directory of manage.py
        load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
    except ImportError:
        pass
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError("Couldn't import Django")
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()