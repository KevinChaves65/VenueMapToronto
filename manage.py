#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

<<<<<<< HEAD
<<<<<<< HEAD
# Access Eventbrite Private Token
EVENTBRITE_PRIVATE_TOKEN = os.getenv("EVENTBRITE_PRIVATE_TOKEN")
=======
# Access Eventbrite API Key
EVENTBRTIE_API_KEY = os.getenv("EVENTBRITE_API_KEY")
>>>>>>> origin/main
=======
# Access Eventbrite API Key
EVENTBRTIE_API_KEY = os.getenv("EVENTBRITE_API_KEY")
>>>>>>> origin/main


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kitchen.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
