import telebot
from telebot import TeleBot, types
import property

TOKEN = property.Settings().token()  # todo: add your token to settings JSON
bot = TeleBot(TOKEN)
def get_main_keyboard(): # todo add all buttons
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text=...) # todo: add text
    ...
    keyboard.add(button1,...)
@bot.message_handler(commands=['start'])
def start(message:types.Message):
    pass

@bot.message_handler(func=lambda message: True)
def button_hendler(message:types.Message):
    if message.text == "": # todo: add all hendlers
        pass
