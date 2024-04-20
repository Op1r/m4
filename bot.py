from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from logic import *
import schedule
import time
from config import *

bot = TeleBot(API_TOKEN)






#@bot.message_handler(commands=['start'])
#def handle_start(message):
    #user_id = message.chat.id
    #if user_id in manager.get_users():
        #bot.reply_to(message, "Рады тебя видеть снова!")
    #else:
        #manager.add_user(user_id, message.from_user.username)
        #bot.reply_to(message, """Привет! Добро пожаловать! """)


@bot.message_handler(commands=['dishes'])
def handle_dishes(message):
    bot.reply_to(message, "Мясные тефтели с картофелем и сладким перцем, Спагетти с фасолью, беконом и сыром фета, Картофель, запеченный в духовке, с грибами")

@bot.message_handler(commands=['1'])
def handle_1(message):
    bot.reply_to(message, "Фарш мясной — 400 г Картофель — 300 г Перец болгарский — 150 г лук репчатый — 100 г Морковь — 100 г Сухари панировочные — 75 г Томатная паста — 200 г Масло растительное — 100 мл Яйцо — 1 шт. Перец красный острый молотый — 0,5 ч. ложки Перец черный молотый — 0,5 ч. ложки Петрушка свежая — 15 гТмин молотый — 0,5 ч. ложки Соль — 1 ч. ложка (или по вкусу)")
                    
@bot.message_handler(commands=['2'])
def handle_1(message):
    bot.reply_to(message, "Спагетти - 180 г Фасоль консервированная - 150 г (вес без маринада) Помидоры консервированные в с/соку - 300 г Бекон - 70 г Сыр фета - 60 г Лук репчатый - 70 г Чеснок - 1 зубчик (4 г) Масло растительное - 1 ст. ложка Базилик сушёный - 0,5 ч. ложки Петрушка свежая - 5 г Соль - по вкусу Перец чёрный молотый - по вкусу")    

@bot.message_handler(commands=['3'])
def handle_1(message):
    bot.reply_to(message, "Картофель - 900 г (9 шт.) Грибы шампиньоны - 350 г Лук репчатый - 130 г Масло сливочное - 100 г Чеснок - 1-2 зубчика Соль - по вкусу Перец черный молотый - по вкусу Прованские травы - 0,5 ч. ложки")    


@bot.message_handler(commands=['start'])
def start_handler(message):
    url_button = InlineKeyboardButton(text="2")
    url_buttons = InlineKeyboardButton(text="3")
    url_buttons1 = InlineKeyboardButton(text="1")
    keyboard = InlineKeyboardMarkup(row_width=3)
    keyboard.add(url_button, url_buttons, url_buttons1)
    bot.send_message(message.chat.id, f'Приветствую тебя, {message.from_user.first_name}!')
    bot.send_message(message.chat.id, "10", reply_markup=keyboard)

if __name__ == '__main__':
    manager = DatabaseManager(DATABASE)
    manager.create_tables()
    bot.polling(none_stop=True)

  
