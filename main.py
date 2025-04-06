import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я бот - кнопки для расписания, вот команды, которые можно использовать: /mon, /tue, /wen, /thu, /fri, /sut, /dev, /school\
""")
    
@bot.message_handler(commands=['dev'])
def send_welcome(message):
    bot.reply_to(message, """\
Я Влад, я увлекаюсь пайтоном уже 3 года, мне 16, я делал бот - портфолио, бот - выбор фильмов\
""")
    
@bot.message_handler(commands=['school'])
def send_welcome(message):
    bot.reply_to(message, """\
Я учусь в школе №12, у меня каждый день по 7-8 уроков, я учусь в 10 классе, наша школа трехэтажная, у нас две большие перемены по 20 минут, остальные по 5, у нас спортзала, один в начальной школе, другой в старшей.\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()