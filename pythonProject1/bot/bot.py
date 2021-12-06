import sqlite3
import time

import requests
import telebot
import threading
from cfg import TOKEN
from models import sub
from database import add_subscription, search_city_code
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def greetings(message):
    bot.send_message(message.chat.id, text='Приветствие...')

@bot.message_handler(commands=['subscriptions'])
def sub(message):
    bot.send_message(message.chat.id, text='Ваши подписки')

@bot.message_handler(commands=['add'])
def citydepart(message):
    msg = bot.send_message(message.chat.id, text='Введите город отправки')
    bot.register_next_step_handler(msg,citydest)
def citydest(message):
    sub.city_depart = message.text
    msg = bot.send_message(message.chat.id, text='Введите город назначения')
    bot.register_next_step_handler(msg,datedepart)
def datedepart(message):
    sub.city_destination = message.text
    msg = bot.send_message(message.chat.id, text='Введите дату отправки в формате ДДММГГ')
    bot.register_next_step_handler(msg,dateback)
def dateback(message):
    sub.date_depart = message.text
    msg = bot.send_message(message.chat.id, text='Введите дату возвращения в формате ДДММГГ')
    bot.register_next_step_handler(msg,price)
def price(message):
    sub.date_back = message.text
    msg = bot.send_message(message.chat.id,text='Введите максимальную цену билета')
    bot.register_next_step_handler(msg,add)
def add(message):
    sub.price = message.text
    try:
        add_subscription(depart_city=sub.city_depart,dest_city=sub.city_destination,date_depart=sub.date_depart, date_back=sub.date_back, price_lim=sub.price, user_id=message.from_user.id)
    except sqlite3.Error as e:
        print(e)
    r = requests.get(f'https://www.onetwotrip.com/_api/rzd/metaTimetable?adults=1&children=0&infants=0&date={sub.date_depart}&from={search_city_code(sub.city_depart)}&to={search_city_code(sub.city_destination)}&isReturn=false&referrer_mrk=google.com%7C%2Fru%2Flandings').json()

    if r["result"][0] == None:
        bot.send_message(message.chat.id, text='Билеты не найдены')
    else:
        cost = r["result"][0]["places"][0]["cost"]
        start = r["result"][0]["from"]["metaName"]
        finish = r["result"][0]["to"]["metaName"]
        time_start = r["result"][0]["departure"]["isoTime"]
        link = r["result"][0]["deeplink"]
        print(cost)
        print(start)
        print(finish)
        print(time_start)
        try:
            bot.send_message(message.chat.id,text=f'Подписка успешно добавлена!\n💵 {cost} Рублей\n➡️ Город отправления:{start}\nГород прибытия:{finish}\n{time_start}\n{link}')
        except:
            bot.send_message(message.chat.id, text='Неизвестная ошибка')


if __name__ == "__main__":
    bot.polling()




