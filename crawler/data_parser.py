import json
import re
from bs4 import BeautifulSoup
import logging

def detail_parse_data(html_content):
    if html_content:
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            script_tags = soup.find_all('script')
            script_content = None
            for script in script_tags:
                if script.string and "window.data" in script.string:
                    script_content = script.string

            if script_content:
                match = re.search(r'window\.data\s*=\s*(\{.*\});', script_content, re.DOTALL)
                if match:
                    json_data_str = match.group(1)
                    json_data_str = re.sub(r'//.*?\n|/\*.*?\*/', '', json_data_str, flags=re.DOTALL)
                    json_data = json.loads(json_data_str)

                    provider_data = json_data.get("provider", {})
                    meta_data = json_data['item']['meta']
                    fhLocation_data = json_data['item']['fhLocation']
                    category_data = json_data['item']['category']
                    price_data = json_data['item']['priceList']
                    prodTag_data = json_data['item']['prodTag']

                    return provider_data, meta_data, fhLocation_data, category_data, price_data, prodTag_data

                else:
                    logging.error("No JSON data found")
            else:
                logging.error("No script content found for parsing")

        except Exception as e:
            logging.error(f"Error parsing data: {e}")

    else:
        logging.error("HTML content is empty")

    return None, None, None, None, None, None
