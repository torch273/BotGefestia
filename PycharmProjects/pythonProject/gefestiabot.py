import telebot
from telebot import types
import smtplib
from email.mime.text import MIMEText

bot = telebot.TeleBot('7810590914:AAH5TmZuFJ_0AF7X7WbcaVJkGJfHCelCAEQ')

SMTP_SERVER = 'smtp.yandex.ru'
SMTP_PORT = 587
FROM_EMAIL = 'mega.tamu@yandex.ru'
PASSWORD = 'xkdxdidokeiktfby'
TO_EMAIL = 'mega.tamu@yandex.ru'


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Наши цены")
    btn2 = types.KeyboardButton("Примеры работ")
    btn3 = types.KeyboardButton("Оставить заявку")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Добрый день, {0.first_name}! Я бот для строительно-ремонтной компании Гефестия.".format(
                         message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id, text="Нажмите на кнопки ниже для большей информации.".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Наши цены"):
        bot.send_message(message.chat.id, text="В процессе разработки...")
    elif (message.text == "Примеры работ"):
        bot.send_message(message.chat.id, text="В процессе разработки...")
    elif (message.text == "Оставить заявку"):
        msg = MIMEText(message.text)
        msg['Subject'] = f"Новая заявка"
        msg['From'] = FROM_EMAIL
        msg['To'] = TO_EMAIL

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
        server.quit()
    else:
        bot.send_message(message.chat.id, text="ЧЕ ТЫ ЕМУ ПИШЕШЬ??? ВИДИШЬ НЕ ГОТОВ БОТЯРА???")


bot.polling(none_stop=True)