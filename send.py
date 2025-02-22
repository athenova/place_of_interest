import os
import telebot
import json
import glob

from datetime import date
from helpers.images import gen_image
from helpers.textes import gen_text

BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
CHAT_ID = '@place_of_interest'

def job(CHAT_ID=CHAT_ID, text_gen=False, image_gen=False, offset = 0):
    index = date.today().timetuple().tm_yday + offset
    tasks = json.load(open('files/in_progress.json', 'rt', encoding='UTF-8'))
    for task in tasks:
        if task['index'] == index:
            folder_name = glob.escape(f"files/data/{task['group'].replace('/', ',')}/{task['name'].replace('/', ',')}")
            text_file_name = f"{folder_name}/text.txt"
            image_file_name = f"{folder_name}/image.png"

            if text_gen:
                gen_text(task, text_gen)
            if image_gen:
                gen_image(task)

            bot = telebot.TeleBot(BOT_TOKEN)
            if os.path.exists(image_file_name):
                bot.send_photo(chat_id=CHAT_ID, photo=open(image_file_name, 'rb'), parse_mode="Markdown")

            if os.path.exists(text_file_name):
                bot.send_message(chat_id=CHAT_ID, text=open(text_file_name, 'rt', encoding='UTF-8').read(), parse_mode="Markdown")

if __name__ == '__main__':
    job()