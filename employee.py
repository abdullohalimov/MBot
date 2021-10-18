import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('1914786053:AAGZTrnkg4gh5lOYffVhYjvm5AFKIOR7hrw')

# variables
lang = 'ru'


# markups
lang_markup = ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
lang_markup.add("O'zbekcha", "Russian")
#
count_markup_uz = ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
count_markup_ru = ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
count_markup_uz.add("Bir dona", "Bir nechta", "Ishchi guruh")
count_markup_ru.add("ONE", "SOME", "WORKGROUP")


# bot
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Foydalanish tilini tanlang:\n'
                                      '\nВыберите язык:', reply_markup=lang_markup)
    bot.register_next_step_handler(message, callback=start2)

@bot.message_handler(content_types=['text'])
def start2(message):
    global lang
    if message.text == 'O\'zbekcha':
        bot.send_message(message.chat.id, 'Assalomu aleykum\nIshchilar sonini tanlang', reply_markup=count_markup_uz)

    elif message.text == 'Russian':
        bot.send_message(message.chat.id, 'Здравствуйте\nВыберите количество работников', reply_markup=count_markup_ru)





bot.infinity_polling()
