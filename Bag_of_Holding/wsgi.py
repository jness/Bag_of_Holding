"""
WSGI config for Bag_of_Holding project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Bag_of_Holding.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
