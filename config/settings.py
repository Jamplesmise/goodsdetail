import logging

# Logging configuration
logging.basicConfig(filename='logs/crawler_errors.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Headers for requests
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}

# Database configuration
LOCALSQLURL = "mysql+pymysql://xx:xxx@xxxx:xxx/historydatacenter"
ENGINE_OPTIONS = {
    'pool_size': 10,
    'max_overflow': 20,
    'pool_timeout': 30,
    'pool_recycle': 3600,
    'pool_pre_ping': True
}
xlsx_columns = ['dataclass',
                'datasource',
                'keyname',
                'url',
                'provider',
                'good_detail',
                'fhLocation',
                'category',
                'price_info',
                'prodTag',
                'createdAt']
# MongoDB configuration
MONGO_URI = "mongodb://xxxx:xxxxx"
MONGO_DB_NAME = "historydatacenter"
MONGO_COLLECTION_NAME = "product_summary_detail"
MAX_POOL_SIZE = 50
MIN_POOL_SIZE = 10

# General settings
SLEEP_INTERVAL = 3600 * 24 * 7
