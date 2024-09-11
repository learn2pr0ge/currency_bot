import telebot
import config
import os
from config import cur_list
from extensions import APIException, APIWork
token = config.BOT_TOKEN
bot = telebot.TeleBot(token)




#обработчик команд /start /help
@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.reply_to(message, "Добро пожаловать в бота конвертера валют\n"
                     "Доступные команды: /start /help /values\n"
                     "Команда /values отображает список доступных валют"
                     "Для того чтобы начать конвертацию введите исходную валюту\n"
                     "Валюту которую хотите получить и сумму\n"
                     "Пример запроса: USD EUR 100\n")

#обработчик команд /values
@bot.message_handler(commands=['values'])
def list_cur(message):
    cur_str = ''
    for i in cur_list:
        cur_str += i + ' '
    bot.send_message(message.chat.id, f"Список доступных валют: {cur_str}")

@bot.message_handler(content_types=['text'])
def make_conv(message):
    mes_to_func = message.text.split()
    if len(mes_to_func) != 3:
        bot.send_message(message.chat.id, f"Неправильный формат запроса. Пример запроса: USD EUR 100")
    else:
        base, quote, amount = mes_to_func
        result = APIWork.get_price(base, quote, amount)
        bot.send_message(message.chat.id, result)

bot.polling(none_stop=True)
