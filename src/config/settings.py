import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

HH_API_URL = os.getenv('HH_API_URL')
HH_MAX_LOAD_PAGES = int(os.getenv('HH_MAX_LOAD_PAGES'))
HH_MAX_PER_PAGE = int(os.getenv('HH_MAX_PER_PAGE'))

JSON_DATA_DIR = os.getenv('JSON_DATA_DIR')

JSON_DATA_FILE = os.getenv('JSON_DATA_FILE')
