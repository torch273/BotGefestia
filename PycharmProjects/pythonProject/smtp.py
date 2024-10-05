from telebot import TeleBot, types
import smtplib
from email.mime.text import MIMEText

# Токен вашего бота
API_TOKEN = '7810590914:AAH5TmZuFJ_0AF7X7WbcaVJkGJfHCelCAEQ'

# Настройки почты
SMTP_SERVER = 'smtp.yandex.ru'
SMTP_PORT = 587
FROM_EMAIL = 'mega.tamu@yandex.ru'
PASSWORD = 'xkdxdidokeiktfby'
TO_EMAIL = 'mega.tamu@yandex.ru'

bot = TeleBot(API_TOKEN)

@bot.message_handler(content_types=['text'])
    if (message.text == "Оставить заявку"):
        msg = MIMEText(message.text)
        msg['Subject'] = f"Новая заявка"
        msg['From'] = FROM_EMAIL
        msg['To'] = TO_EMAIL

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
        server.quit()

    # Ответ пользователю
    bot.send_message(message.chat.id, "Ваше сообщение отправлено на почту.")

bot.polling(none_stop=True)