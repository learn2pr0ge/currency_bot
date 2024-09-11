import os
from dotenv import load_dotenv, find_dotenv
cur_list = ['USD','EUR','RUB']

if not find_dotenv():
    exit('Отсутсвует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
API_KEY = os.getenv("API_KEY")