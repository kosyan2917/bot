import telebot

bot = telebot.TeleBot('6234145156:AAHENV4FfTBwzuO3Trv5UfhDr6jzk1UFK10')
savva = 275558219
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(savva, f'''
    Пользователь: {message.from_user.first_name} {message.from_user.last_name}, id: {message.from_user.id}
    Сообщение: {message.text}
''')
bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть

