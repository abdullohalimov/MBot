import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('1994419215:AAGDQiKTaYk2biFT_5_smPMJ_WRbKs82xRw')

# variables
lang = 'ru'


# markups
def lang_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton('Russ', callback_data='lang_ru'),
               InlineKeyboardButton('O\'zbekcha', callback_data='lang_uz'))
    return markup


def type_markup_uz():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton('Ish Beruvchi', callback_data='type_emple'),
               InlineKeyboardButton('Ishchi', callback_data='type_emplr'))
    return markup
def type_markup_ru():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton('Работодатель', callback_data='type_emple'),
               InlineKeyboardButton('Работник', callback_data='type_emplr'))
    return markup


# bot
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Assalomu aleykum\nFoydalanish tilini tanlang:\n'
                                      '\nRus...:', reply_markup=lang_markup())




@bot.message_handler(content_types=['text'])
def start_type(message):
    if lang == 'uz':
        bot.send_message(message.chat.id, 'Ish bervchimisiz yoki ishchi?', reply_markup=type_markup_uz())
    elif lang == 'ru':
        bot.send_message(message.chat.id, 'Вы работодатель или работник?', reply_markup=type_markup_ru())

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global lang
    if call.data == 'lang_ru':
        bot.answer_callback_query(call.id, text='Selected Russian')
        lang = "ru"
        bot.register_next_step_handler(call.message, callback=start_type)
    elif call.data == "lang_uz":
        bot.answer_callback_query(call.id, 'Selected Uzbekisch')
        lang = 'uz'
        bot.register_next_step_handler(call.message, callback=start_type)





bot.infinity_polling()
