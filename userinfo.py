import telebot
from telebot import types
from forward import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)#API Token

@bot.message_handler(commands=['start'])
def startcommand(message):
    user_id = message.from_user.id
    first_name=message.from_user.first_name
    username = message.from_user.username
    bot.send_message(message.chat.id,f"Your ID: {user_id}\n Your Name: {first_name}\n Your Username: @{username}")

    user_profile = bot.get_user_profile_photos(user_id)

    if user_profile.total_count>0:
        file_id = user_profile.photos[0][0].file_id
        bot.send_message(user_id,"Sizda rasm mavjud")
        bot.send_photo(user_id,file_id)

    else:
        bot.send_message(user_id,"Sizda rasm mavjud emas")





bot.polling()# bot tinimsiz ishlab turishi uchun
