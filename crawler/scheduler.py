import pandas as pd
import time
import random
from crawler.data_fetcher import fetch_url
from crawler.data_parser import detail_parse_data
from crawler.data_storage import save_data_to_db, save_data_to_excel, save_data_to_mongo
from utils.data_utils import process_single_element_to_dict, list_of_dicts_to_single_dict
from config.settings import SLEEP_INTERVAL, xlsx_columns


def fetch_in_loop(url_list, name):
    urls_list = []
    provider_data_list = []
    meta_data_list = []
    fhLocation_data_list = []
    category_data_list = []
    price_data_list = []
    prodTag_data_list = []
    createdAt = []
    dataclass = []
    datasource = []
    name_list = []
    num_count = 0
    error_count = 0
    df = pd.DataFrame(columns=xlsx_columns)
    for url in url_list:
        num_count += 1
        print(f"产品名：{name}，当前进度：{num_count}/{len(url_list)}")
        try:
            response = fetch_url(url)
            if response is not None:
                provider_data, meta_data, fhLocation_data, category_data, price_data, prodTag_data = detail_parse_data(
                    response)
                urls_list.append(url)
                name_list.append(name)
                provider_data_list.append(provider_data)
                meta_data_list.append(meta_data)
                fhLocation_data_list.append(fhLocation_data)
                category_data_list.append(category_data)
                price_data_list.append(price_data)
                prodTag_data_list.append(prodTag_data)
                createdAt.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                dataclass.append('商品内页')
                datasource.append('百度爱采购')

        except Exception as e:
            error_count += 1
            print(f"Error count: {error_count}")
            if error_count % 5 == 0:
                sleep_num = random.randint(20, 30)
                print(f"Pausing for {sleep_num} seconds...")
                time.sleep(sleep_num)
            print(f"Error parsing data: {e}")
            continue

    df['dataclass'] = dataclass
    df['datasource'] = datasource
    df['keyname'] = name_list
    df['url'] = urls_list
    df['provider'] = provider_data_list
    df['good_detail'] = meta_data_list
    df['fhLocation'] = fhLocation_data_list
    df['category'] = category_data_list
    df['price_info'] = price_data_list
    df['prodTag'] = prodTag_data_list
    df['createdAt'] = createdAt
    df['good_detail'] = df['good_detail'].fillna("kk").apply(process_single_element_to_dict)
    df['price_info'] = df['price_info'].fillna("kk").apply(list_of_dicts_to_single_dict)
    return df


def main_spider():
    name_df = pd.read_excel('E:/中转站/搜索列表.xlsx', sheet_name='原版')
    name_list = name_df['名称'].tolist()
    for name in name_list:
        url_df = pd.read_excel(f'D:/Data_Pool/Static_Pool/{name}更新.xlsx')
        urls = url_df['jumpUrl'].tolist()
        result_df = fetch_in_loop(urls, name)
        save_data_to_excel(result_df, f'D:/Data_Pool/Detail_Pool/{name}详情页.xlsx')
        if result_df.empty:
            print(f"{name}详情页数据为空，跳过")
            continue
        else:
            save_data_to_mongo(result_df)
        random_sleep_num = random.randint(60, 120)
        time.sleep(random_sleep_num)
