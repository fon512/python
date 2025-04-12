import telebot
import  config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id,'сволочь не пеши суда')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'зачем ты мне это пишешь? даун! '+ message.text)

@bot.message_handler(content_types=['sticker'])
def message_sticker(message):
    stiker_id = message.sticker.file_id
    print(stiker_id)
    bot.send_sticker(message.chat.id, stiker_id)


bot.polling(none_stop=True, interval=0)