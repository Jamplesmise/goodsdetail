from crawler.scheduler import main_spider
from utils.countdown import countdown
from config.settings import SLEEP_INTERVAL

while True:
    
    main_spider()
    countdown(SLEEP_INTERVAL)
    



