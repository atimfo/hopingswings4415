import telebot

token = '6660308697:AAGy_JFVVv9wk7qzuM4-_lz6TuD3SpvbPDI'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Привет! Я твой новый бот')


bot.infinity_polling()
