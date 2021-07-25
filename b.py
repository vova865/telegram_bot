import telebot

bot = telebot.TeleBot('1938846595:AAGungBrhrHpmGAzH-Tq72sCa1kEWyOeYsc')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


keyboard1 = telebot.types.ReplyKeyboardMarkup()  # функция вызывает клавиатуру
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Premier League', 'LaLiga', 'Bundesliga', 'Serie A', 'Ligue1')

bot.polling()