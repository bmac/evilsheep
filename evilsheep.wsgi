import os
import sys

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'evilsheep.settings'
sys.path.insert(0, '/home/bmac/webapps/django/')
sys.path.insert(0, '/home/bmac/webapps/django/evilsheep/')


application = WSGIHandler()
