import telebot
import  config
import datetime


bot = telebot.TeleBot(config.token)

now= datetime.datetime.now()
# @bot.message_handler(commands=['start'])
# def start(m):
#     bot.send_message(m.chat.id,'сволочь не пеши суда')

# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'зачем ты мне это пишешь? даун! '+ message.text)

@bot.message_handler(content_types=['sticker'])
def message_sticker(message):
    stiker_id = message.sticker.file_id
    print(stiker_id)
    bot.send_sticker(message.chat.id, stiker_id)

@bot.message_handler(content_types=['text'])
def dialog(message):
    if message.text== 'Привет' or message.text == 'привет':
        bot.send_message(message.chat.id, 'привет чмо')
    elif message.text== 'Как дела':
        bot.send_message(message.chat.id, 'ТЫ ТИПО ХОЧЕШЬ ПООБЩАТЬСЯ ИДИКА ТЫ НАФИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИГ')
    elif message.text== 'Че ты такой агрессивный':
        bot.send_message(message.chat.id, 'ПОШОЛ НА**Й')

    elif message.text == 'Здравствуйте':
        bot.send_message(message.chat.id, 'ТЫ ЧЕ ТИПО КУРТУРНЫЙ ПОШОЛ ТЫ Я С ТАКИМИ НЕ ОБЩАЮСЬ')
    else:
        bot.send_message(message.chat.id, 'Я НЕ МОГУ НА ЭТО ОТВЕТИТЬ ПОТОМУ ЧТО ТЫ В ЭТОМ ВИНОВАТ ДЕБИЛ ПИШИ ЛИБО НА ТО ЧТО Я МОГУ ОТВЕТИТЬ ЛИБО С БОЛЬШОЙ БУКВЫ ДЕГИНЕРАТ')

@bot.message_handler(content_types=['text'])
def dialog(message):
    today = now.day
    hour = now.hour
    if message.text == 'Привет':
        if today == now.day and 6 <= hour<12:
            bot.send_message(message.chat.id, 'привет')



bot.polling(none_stop=True, interval=0)

bot.infinity_polling()