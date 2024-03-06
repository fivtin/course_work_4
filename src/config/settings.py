import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

HH_API_URL = os.getenv('HH_API_URL')

JSON_DATA_DIR = os.getenv('JSON_DATA_DIR')

JSON_DATA_FILE = os.getenv('JSON_DATA_FILE')
