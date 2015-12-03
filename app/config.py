import os
import yaml

ENV = os.environ.get('ENVIRONMENT', 'dev')
SECRET_KEY = os.environ.get('SECRET_KEY')
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
ROOT_PATH = BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
CSRF_ENABLED = True
PORT = os.environ.get('PORT')
DEBUG = os.environ.get('DEBUG', False)

with open('settings.yaml', 'r') as f:
    tmp = yaml.load(f)
    DEVICES = tmp["devices"]
