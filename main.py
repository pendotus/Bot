

import telebot
from telebot import types
import requests
import bs4
from bs4 import BeautifulSoup
from GuessGame import guessgame
import dz

###########

bot = telebot.TeleBot("5129865898:AAFDCkKgtLRj9qBj-XSBJHphvHLr4Lv1wxg")

###########

KeyboardStart = types.ReplyKeyboardMarkup(True)
KeyboardStart.row("Главное меню", "Обо мне")

KeyboardHelp = types.ReplyKeyboardMarkup(True)
KeyboardHelp.row("/menu", "/web", "/about")
KeyboardHelp.row("/dog", "/rofl",)
KeyboardHelp.row("/back", "/start")

KeyboardMenu = types.ReplyKeyboardMarkup(True)
KeyboardMenu.row("Пришли анекдот", "Пришли собаку", "Игра")
KeyboardMenu.row("Пришли мангу", "/back")

KeyboardRoflMenu = types.ReplyKeyboardMarkup(True)
KeyboardRoflMenu.row("Пришли анекдот", "Пришли собаку", "Игра")
KeyboardRoflMenu.row("Пришли мангу", "/back" )

KeyboardGame = types.ReplyKeyboardMarkup(True)
KeyboardGame.row ("Выше", "Ниже")
KeyboardGame.row ("Главное меню")


############

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот, че тут сказать.', reply_markup=KeyboardStart)

@bot.message_handler(commands=["menu"])
def menu(message):
    bot.send_message(message.chat.id, "А вот и главное меню", reply_markup=KeyboardMenu)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "А вот и меню помощи", reply_markup=KeyboardHelp)

@bot.message_handler(commands=["back"])
def back(message):
    bot.send_message(message.chat.id, "Один момент!", reply_markup=KeyboardStart)

@bot.message_handler(commands=["dog"])
def dog(message):
    contents = requests.get("https://random.dog/woof.json").json()
    urlDOG = contents["url"]
    bot.send_photo(message.chat.id, photo=urlDOG, caption="Лови пса!")
        
@bot.message_handler(commands=["rofl"])
def rofl():
    array_rofls = []
    req_rf = requests.get('http://anekdotme.ru/random')
    soup = bs4.BeautifulSoup(req_rf.text, "html.parser")
    result_find = soup.select('.anekdot_text')
    for result in result_find:
        array_rofls.append(result.getText().strip())
    return array_rofls[0]

@bot.message_handler(commands=["web"])
def WEBCum(message):
    bot.send_message(message.chat.id, "Заглушка")

@bot.message_handler(commands=["control"])
def control(message):
    bot.send_message(message.chat.id, "Заглушка")

@bot.message_handler(commands=["roflmenu"])
def roflmenu(message):
    bot.send_message(message.chat.id, "А вот и развлечения!", reply_markup=KeyboardRoflMenu)

@bot.message_handler(commands=["about"])
def about(message):
    bot.send_message(message.from_user.id, "Меня зовут Марк, я студент группы 1-МД-20. Приятно познакомится!")
    bot.send_photo(message.chat.id, open("me.jpg", "rb"))

@bot.message_handler(command=["game"])
def game(message):
    gameInstance = guessgame(message.chat.id)
    bot.send_message(message.chat.id, "У нас работает игра на угадывание", reply_markup=KeyboardGame)
    bot.send_photo(message.chat.id, photo=gameInstance.getCard("first", message.chat.id), caption="Игра запущена, первая карта:")

@bot.message_handler(command=["hight"])
def hight(message):
    gameInstance = guessgame(message.chat.id)
    status = gameInstance.getResults("higher", message.chat.id)
    if status == True:
        bot.send_photo(message.chat.id, photo=gameInstance.getCard("second", message.chat.id), caption="Вы победили, вторая карта:",  reply_markup=KeyboardMenu)
    else:
        bot.send_photo(message.chat.id, photo=gameInstance.getCard("second", message.chat.id), caption="Вы проиграли, вторая карта:",  reply_markup=KeyboardMenu)
    gameInstance.resetGame(message.chat.id)

@bot.message_handler(command=["low"])
def low(message):
    gameInstance = guessgame(message.chat.id)
    status = gameInstance.getResults("lower", message.chat.id)
    if status == True:
        bot.send_photo(message.chat.id, photo=gameInstance.getCard("second", message.chat.id), caption="Вы победили, вторая карта:",  reply_markup=KeyboardMenu)
    else:
        bot.send_photo(message.chat.id, photo=gameInstance.getCard("second", message.chat.id), caption="Вы проиграли, вторая карта:",  reply_markup=KeyboardMenu)
    gameInstance.resetGame(message.chat.id)

def get_manga():
    req_anime = requests.get('https://manga-chan.me/manga/random')
    soup = bs4.BeautifulSoup(req_anime.text, "html.parser")
    result_find = soup.find("div", class_="content_row")
    result_find_name = result_find.find("h2")
    array_anime_in = []
    result_find_in = result_find.find("div", class_="tags")
    im = []
    for img in result_find.findAll("img"):
        im.append(img.get("src"))
    return result_find_name, result_find_in, im

def dollar():
    usd = requests.get('https://free.currconv.com/api/v7/convert?apiKey=fe46166a438567209072&q=USD_RUB&compact=ultra').json()
    euro = requests.get('https://free.currconv.com/api/v7/convert?apiKey=fe46166a438567209072&q=EUR_RUB&compact=ultra').json()
    return usd, euro
#############

@bot.message_handler(command=["dz1"])
def dz1(message):
    dz.dz1

@bot.message_handler(command=["dz2"])
def dz2(message):
    dz.dz2

@bot.message_handler(command=["dz3"])
def dz3(message):
    dz.dz3


@bot.message_handler(command=["dz4"])
def dz4(message):
    dz.dz4

@bot.message_handler(command=["dz5"])
def dz5(message):
    dz.dz5

@bot.message_handler(command=["dz6"])
def dz6(message):
    dz.dz6

@bot.message_handler(command=["dz7"])
def dz7(message):
    dz.dz7

@bot.message_handler(command=["dz8"])
def dz8(message):
    dz.dz8

@bot.message_handler(command=["dz9"])
def dz9(message):
    dz.dz9


#############

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    gameInstance = guessgame(message.chat.id)


    if message.text == "Главное меню" or message.text == "главное меню":
        bot.register_next_step_handler(message, menu)
    elif message.text == "Помощь" or message.text == "помощь":
        bot.register_next_step_handler(message, help)
    elif message.text == "Развлечение":
        bot.register_next_step_handler(message, roflmenu)
    elif message.text == "Пришли собаку":
        bot.register_next_step_handler(message, dog)
    elif message.text == "Пришли анекдот":
        bot.send_message(message.chat.id, text=rofl())
    elif message.text == "Web-Камера":
        bot.register_next_step_handler(message, WEBCum)
    elif message.text == "Управление":
        bot.register_next_step_handler(message, control)
    elif message.text == "Обо мне":
        bot.register_next_step_handler(message, about)
    elif message.text == "Игра":
        bot.register_next_step_handler(message, game)
    elif message.text == "Выше":
        bot.register_next_step_handler(message, hight)
    elif message.text == "Ниже":
        bot.register_next_step_handler(message, low)
    elif message.text == "Пришли мангу":
        result_find_name, result_find_in, im = get_manga()
        bot.send_message(message.chat.id, result_find_name)
        bot.send_photo(message.chat.id, photo=(im[0]))
        bot.send_message(message.chat.id, result_find_in)
    elif message.text == "Курс валют":
        usd, euro = dollar()
        bot.send_message(message.chat.id, usd['USD_RUB'])
        bot.send_message(message.chat.id, euro['EUR_RUB'])
    else:
        pass

#############

bot.polling(none_stop=True)
