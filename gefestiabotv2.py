import telebot
from telebot import types
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

# Токен Telegram бота
TOKEN = '7810590914:AAH5TmZuFJ_0AF7X7WbcaVJkGJfHCelCAEQ'
bot = telebot.TeleBot(TOKEN)

# Данные для SMTP
EMAIL = 'mega.tamu@yandex.ru'
PWD = 'xkdxdidokeiktfby'
TO_EMAIL = 'mega.tamu@yandex.ru'

# Путь к PDF файлу
PDF_FILE_PATH = 'D:/price.pdf'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_photo(message.chat.id, open('D:/gefestia.jpg', 'rb'))
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Оставить заявку", callback_data="take_request")
    button2 = types.InlineKeyboardButton(text="Наши цены", callback_data="send_pdf")
    button3 = types.InlineKeyboardButton(text="Наши работы", callback_data="send_link")
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Добрый день, {0.first_name}! Я бот для строительно-ремонтной компании Гефестия. Нажмите на кнопки ниже для большей информации.".format (message.from_user), reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "take_request":
        bot.send_message(call.message.chat.id, "Пожалуйста, отправьте ваше имя и контактную информацию.")
        bot.register_next_step_handler(call.message, send_request_to_email)
    elif call.data == "send_pdf":
        send_pdf(call.message)
    elif call.data == "send_link":
        send_link(call.message)

def send_request_to_email(message):
    user_name = message.from_user.first_name
    user_id = message.chat.id
    user_message = message.text
    send_email(user_name, user_id, user_message)
    bot.send_message(user_id, "Ваша заявка отправлена! Мы свяжемся с вами в ближайшее время.")

def send_email(user_name, user_id, user_message):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = f"Заявка от {user_name} (ID: {user_id})"
    msg.attach(MIMEText(user_message, 'plain'))
    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.starttls()
    server.login(EMAIL, PWD)
    server.sendmail(EMAIL, TO_EMAIL, msg.as_string())
    server.quit()

def send_pdf(message):
    with open(PDF_FILE_PATH, 'rb') as f:
        pdf_data = f.read()
    bot.send_document(message.chat.id, pdf_data, caption='Наш прайс-лист.')

def send_link(message):
    bot.send_message(message.chat.id, "Тут будет ссылка на статью или файл с примерами работ: https://example.com")

bot.polling(none_stop=True)