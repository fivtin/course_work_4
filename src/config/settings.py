import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

HH_API_URL = os.getenv('HH_API_URL')

