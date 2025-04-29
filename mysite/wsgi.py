import os

from django.core.wsgi import get_wsgi_application
from asgiref.wsgi import WsgiToAsgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
application = WsgiToAsgi(application)