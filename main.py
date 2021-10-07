import telebot
from telebot import types

bot = telebot.TeleBot('1994419215:AAGDQiKTaYk2biFT_5_smPMJ_WRbKs82xRw')

startMarkup = types.ReplyKeyboardMarkup()
startMarkup.row("Ish Beruvchi")
startMarkup.row("Ishchi")

countMarkup = types.ReplyKeyboardMarkup()
countMarkup.row("Bir", "Ikki", "Uch")
countMarkup.row("Ishchi guruh")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Assalomu aleykum\n"
                                           "Testbot ga xush kellibsiz\n"
                                           "Tanlang:\n", reply_markup=startMarkup)
    bot.register_next_step_handler(message, callback=employer)


@bot.message_handler(content_types=['text'])
def employer(message):
    if message.text == "Ish Beruvchi":
        bot.send_message(message.from_user.id, "Ishchilar sonini tanlang:")
        bot.register_next_step_handler(message, employerCountStep)

def employerCountStep(message):
    if message.text == "Bir" or "Ikki" or "Uch":
        bot.send_message(message.from_user.id, "Qaysi soxa mutaxassislarini izlamoqdasiz?")




bot.polling()
