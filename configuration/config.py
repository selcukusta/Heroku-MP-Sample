import os
dirname = os.path.dirname(__file__)

DEBUG = True
COMPRESS_RESPONSE = True
PORT = 1905
STATIC_PATH = os.path.join(dirname, '../assets')
TEMPLATE_PATH = os.path.join(dirname, '../templates')