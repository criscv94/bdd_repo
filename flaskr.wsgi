#!/usr/bin/python3
activate_this = '/var/www/flaskr/venv/bin/activate_this.py'
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/flaskr/")

from flaskr import app as application
application.secret_key = 'Add your secret key'
