import os
import telebot


BOT_TOKEN = '6545024038:AAEfRG5P87XD-5HKvN3vCMZeJbeQmE5Sf5s'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    name = message.from_user.first_name
    # photo_url = 'https://3fc4ed44-3fbc-419a-97a1-a29742511391.selcdn.net/coub_storage/coub/simple/cw_image/5e002eb3ea5/43207e7d0a19d7facf286/1511433846_00032.jpg'
    # bot.send_message(message.chat.id, f'who is LOH: , {name}')
    # bot.send_photo(message.chat.id, photo= photo_url, caption= f'СЕГОДНЯ ЛОХ:, {name}')
    bot.send_video(message.chat.id, video=open('laugh.mp4', 'rb'), caption= f'СЕГОДНЯ ЛОХ:, {name}')



bot.infinity_polling()

