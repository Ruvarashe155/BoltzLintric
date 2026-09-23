"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()

# Auto create superuser on startup
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'boltzlintric')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@boltzlintric.co.zw')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'lintric=97')
    
    if username and password and not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"Superuser {username} created!")
except Exception as e:
    print(f"Skip superuser creation: {e}")
