import telebot
from telebot import types  # для указание типов


bot = telebot.TeleBot('7810590914:AAH5TmZuFJ_0AF7X7WbcaVJkGJfHCelCAEQ')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Наши цены")
    btn2 = types.KeyboardButton("Примеры работ")
    btn3 = types.KeyboardButton("Оставить заявку")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Добрый день, {0.first_name}! Я бот для строительно-ремонтной компании Гефестия. Нажмите на кнопки ниже.".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Наши цены"):
        bot.send_message(message.chat.id, text="В процессе разработки...")
    elif (message.text == "Примеры работ"):
        bot.send_message(message.chat.id, text="В процессе разработки...")
    elif (message.text == "Оставить заявку"):
        bot.send_message(message.chat.id, text="В процессе разработки...")
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)