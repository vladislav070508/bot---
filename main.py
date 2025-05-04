import telebot
import config
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot(config.TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup()
    markup.add(KeyboardButton("/mon"))
    markup.add(KeyboardButton("/tue"))
    markup.add(KeyboardButton("/wen"))
    markup.add(KeyboardButton("/thu"))
    markup.add(KeyboardButton("/fri"))
    markup.add(KeyboardButton("/sat"))
    bot.reply_to(message, """\
Привет, я бот - кнопки для расписания, вот команды, которые можно использовать: /mon, /tue, /wen, /thu, /fri, /sat, /dev, /school\
""", reply_markup=markup)
    
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
    
@bot.message_handler(commands=['mon'])
def send_monday(message):
    markup = ReplyKeyboardMarkup()
    markup.add(KeyboardButton("/raz_o_vaz"))
    markup.add(KeyboardButton("/alg"))
    markup.add(KeyboardButton("/geogr"))
    markup.add(KeyboardButton("/ist"))
    markup.add(KeyboardButton("/rus"))
    markup.add(KeyboardButton("/angl"))
    markup.add(KeyboardButton("/fizra"))
    bot.reply_to(message, """ 1. Разговоры о важном - в 8:00
2. Алгебра - в 8:45
3. География - в 9:30
4. История - в 10:30
5. Русский - в 11:30
6. Английский - в 12:15
7. Физ-ра - в 13:00""", reply_markup=markup)
    bot.send_photo(message.chat.id, open("monday.jpg", "rb"))
@bot.message_handler(commands=['raz_o_vaz'])
def send_obj(message):
    bot.reply_to(message, "Разговоры о важном ведёт Татьяна Георгиевна")
@bot.message_handler(commands=['alg'])
def send_obj(message):
    bot.reply_to(message, "Алгебру ведёт Ольга Ивановна")
@bot.message_handler(commands=['geogr'])
def send_obj(message):
    bot.reply_to(message, "Географию ведёт Наталья Васильевна")
@bot.message_handler(commands=['ist'])
def send_obj(message):
    bot.reply_to(message, "Историю ведёт Татьяна Георгиевна")
@bot.message_handler(commands=['rus'])
def send_obj(message):
    bot.reply_to(message, "Русский ведёт Ольга Ивановна")
@bot.message_handler(commands=['angl'])
def send_obj(message):
    bot.reply_to(message, "Английский ведёт Евгений Владимирович")
@bot.message_handler(commands=['fizra'])
def send_obj(message):
    bot.reply_to(message, "Физкультуру ведёт Александр Юрьевич")

@bot.message_handler(commands=['tue'])
def send_tuesday(message):
    markup = ReplyKeyboardMarkup()
    markup.add(KeyboardButton("/fiz"))
    markup.add(KeyboardButton("/angl"))
    markup.add(KeyboardButton("/inf"))
    markup.add(KeyboardButton("/obsh"))
    markup.add(KeyboardButton("/geo"))
    markup.add(KeyboardButton("/litra"))
    markup.add(KeyboardButton("/fizra"))
    bot.reply_to(message, """ 1. Физика - в 8:00
2. Английский - в 8:45
3. Информатика - в 9:30
4. Общество - в 10:30
5. Геометрия - в 11:30
6. Лит-ра - в 12:15
7. Общество - в 13:00
8. Физ-ра - в 14:00""", reply_markup=markup)
    bot.send_photo(message.chat.id, open("tuesday.jpg", "rb"))
@bot.message_handler(commands=['fiz'])
def send_obj(message):
    bot.reply_to(message, "Физику ведёт Ольга Павловна")
@bot.message_handler(commands=['angl'])
def send_obj(message):
    bot.reply_to(message, "Английский ведёт Евгений Владимирович")
@bot.message_handler(commands=['inf'])
def send_obj(message):
    bot.reply_to(message, "Информатику ведёт Елена Михайловна")
@bot.message_handler(commands=['obsh'])
def send_obj(message):
    bot.reply_to(message, "Общество ведёт Татьяна Георгиевна")
@bot.message_handler(commands=['geo'])
def send_obj(message):
    bot.reply_to(message, "Геометрию ведёт Ольга Ивановна")
@bot.message_handler(commands=['litra'])
def send_obj(message):
    bot.reply_to(message, "Литературу ведёт Ольга Ивановна")
@bot.message_handler(commands=['fizra'])
def send_obj(message):
    bot.reply_to(message, "Физкультуру ведёт Александр Юрьевич")

@bot.message_handler(commands=['wen'])
def send_wensday(message):
    markup = ReplyKeyboardMarkup()
    markup.add(KeyboardButton("/chim"))
    markup.add(KeyboardButton("/biol"))
    markup.add(KeyboardButton("/alg"))
    markup.add(KeyboardButton("/inf"))
    markup.add(KeyboardButton("/geo"))
    bot.reply_to(message, """ 1. Химия - в 8:00
2. Биология - в 8:45
3. Алгебра - в 9:30
4. Информатика - в 10:30
5. Геометрия - в 11:30""", reply_markup=markup)
    bot.send_photo(message.chat.id, open("wensday.jpg", "rb"))
@bot.message_handler(commands=['chim'])
def send_obj(message):
    bot.reply_to(message, "Химию ведёт Константин Владимирович")
@bot.message_handler(commands=['biol'])
def send_obj(message):
    bot.reply_to(message, "Биологию ведёт Константин Владимирович")
@bot.message_handler(commands=['alg'])
def send_obj(message):
    bot.reply_to(message, "Алгебру ведёт Ольга Ивановна")
@bot.message_handler(commands=['inf'])
def send_obj(message):
    bot.reply_to(message, "Информатику ведёт Елена Михайловна")
@bot.message_handler(commands=['geo'])
def send_obj(message):
    bot.reply_to(message, "Геометрию ведёт Ольга Ивановна")

@bot.message_handler(commands=['thu'])
def send_thursday(message):
    markup = ReplyKeyboardMarkup()
    markup.add(KeyboardButton("/inf"))
    markup.add(KeyboardButton("/litra"))
    markup.add(KeyboardButton("/alg"))
    markup.add(KeyboardButton("/ist"))
    markup.add(KeyboardButton("/rus"))
    markup.add(KeyboardButton("/chim"))
    bot.reply_to(message, """ 1. Информатикам - в 8:00
2. Лит-ра - в 8:45
3. Алгебра - в 9:30
4. История - в 10:30
5. Геометрия - в 11:30
6. Русский - в 12:15
7. Химия - в 13:00""", reply_markup=markup)
    bot.send_photo(message.chat.id, open("thursday.jpg", "rb"))
@bot.message_handler(commands=['inf'])
def send_obj(message):
    bot.reply_to(message, "Информатику ведёт Елена Михайловна")
@bot.message_handler(commands=['alg'])
def send_obj(message):
    bot.reply_to(message, "Алгебру ведёт Ольга Ивановна")
@bot.message_handler(commands=['litra'])
def send_obj(message):
    bot.reply_to(message, "Литературу ведёт Ольга Ивановна")
@bot.message_handler(commands=['ist'])
def send_obj(message):
    bot.reply_to(message, "Историю ведёт Татьяна Георгиевна")
@bot.message_handler(commands=['rus'])
def send_obj(message):
    bot.reply_to(message, "Русский ведёт Ольга Ивановна")
@bot.message_handler(commands=['chim'])
def send_obj(message):
    bot.reply_to(message, "Химию ведёт Константин Владимирович")

@bot.message_handler(commands=['fri'])
def send_friday(message):
    markup = ReplyKeyboardMarkup()
    markup.add(KeyboardButton("/chim"))
    markup.add(KeyboardButton("/alg"))
    markup.add(KeyboardButton("/obsh"))
    markup.add(KeyboardButton("/geo"))
    markup.add(KeyboardButton("/angl"))
    markup.add(KeyboardButton("/fizra"))
    bot.reply_to(message, """ 1. Химия - в 8:00
2. Алгебра - в 8:45
3. Общество - в 9:30
4. Геометрия - в 10:30
5. Общество - в 11:30
6. Английский - в 12:15
7. Физ-ра - в 13:00""", reply_markup=markup)
    bot.send_photo(message.chat.id, open("friday.jpg", "rb"))
@bot.message_handler(commands=['chim'])
def send_obj(message):
    bot.reply_to(message, "Химию ведёт Константин Владимирович")
@bot.message_handler(commands=['alg'])
def send_obj(message):
    bot.reply_to(message, "Алгебру ведёт Ольга Ивановна")
@bot.message_handler(commands=['obsh'])
def send_obj(message):
    bot.reply_to(message, "Общество ведёт Татьяна Георгиевна")
@bot.message_handler(commands=['geo'])
def send_obj(message):
    bot.reply_to(message, "Геометрию ведёт Ольга Ивановна")
@bot.message_handler(commands=['angl'])
def send_obj(message):
    bot.reply_to(message, "Английский ведёт Евгений Владимирович")
@bot.message_handler(commands=['fizra'])
def send_obj(message):
    bot.reply_to(message, "Физкультуру ведёт Александр Юрьевич")
    
@bot.message_handler(commands=['sat'])
def send_saturday(message):
    markup = ReplyKeyboardMarkup()
    markup.add(KeyboardButton("/obj"))
    markup.add(KeyboardButton("/geogr"))
    bot.reply_to(message, """ 1. ОБЖ - в 8:00
2. География - в 8:45""", reply_markup=markup)
    bot.send_photo(message.chat.id, open("saturday.jpg", "rb"))
@bot.message_handler(commands=['obj'])
def send_obj(message):
    bot.reply_to(message, "ОБЖ ведёт Владимир Вячеславович")
@bot.message_handler(commands=['geogr'])
def send_obj(message):
    bot.reply_to(message, "Географию ведёт Наталья Васильевна")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()