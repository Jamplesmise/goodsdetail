import requests
import random
import time
import logging
from config.settings import HEADERS

def fetch_url(url):
    try:
        random_number = random.randint(1, 2)
        time.sleep(random_number)
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            return response.text
        else:
            logging.error(f"Request failed for URL: {url} with status code: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Request failed for URL: {url} with exception: {e}")
        return None
