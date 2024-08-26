import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient
from bson import InvalidDocument
from config.settings import LOCALSQLURL, ENGINE_OPTIONS, MONGO_URI, MONGO_DB_NAME, MONGO_COLLECTION_NAME, MAX_POOL_SIZE,MIN_POOL_SIZE

engine = create_engine(LOCALSQLURL, **ENGINE_OPTIONS)

# 创建MongoDB客户端
# 创建 MongoDB 客户端并配置连接池
client = MongoClient(
    MONGO_URI,
    maxPoolSize=MAX_POOL_SIZE,
    minPoolSize=MIN_POOL_SIZE
)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]


def save_data_to_db(df, table_name):
    df.to_sql(table_name, con=engine, if_exists='append', index=False)


def save_data_to_excel(df, file_path):
    df.to_excel(file_path, index=False)


def save_data_to_mongo(df):
    data_to_insert = df.to_dict('records')
    try:
        collection.insert_many(data_to_insert)
        print(f"数据已保存到MongoDB")
    except InvalidDocument as e:
        print("遇到无效文档错误:", e)
        for doc in data_to_insert:
            try:
                collection.insert_one(doc)
            except InvalidDocument:
                print(f"错误文档: {doc}")
