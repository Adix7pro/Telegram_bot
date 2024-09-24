import telebot
from telebot import types
from forward import API_TOKEN_U

bot = telebot.TeleBot(API_TOKEN_U,parse_mode="HTML") #API Token bot


keyboard = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard.row("Photo","Video")
keyboard.row("Audio","Xabar")
keyboard.row("Document")


keyboard1 = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard1.row("1","2")
keyboard1.row("3","4")
keyboard1.row("Bosh Menu")


@bot.message_handler(commands=['start']) #start komandasiga javob qaytaradi
def startcom(message):
    bot.send_message(message.chat.id, "Hi There", reply_markup=keyboard)


@bot.message_handler(content_types=['text']) #tugma bosilganda tekshirib javob qaytarish
def xabarfunc(message):
    if message.text == "Photo":
        bot.send_photo(message.chat.id,"https://t.me/adix7pro/102",caption="<b>Rasm</b>",reply_markup=keyboard1) #silkani kanaldan olish kerak
    elif message.text == "Video":
        bot.send_video(message.chat.id,"https://t.me/adix7pro/86",caption="<u>Video</u>")#Textni tagiga chizib beradi
    if message.text == "Audio":
        bot.send_audio(message.chat.id,"https://t.me/adix7pro/103",caption="<i>Audio</i>")# matnni 45 gradusda burib yozadi
    if message.text == "Document":
        bot.send_document(message.chat.id,"https://t.me/adix7pro/100",caption="<code>Document</code>")# Textdan nusxa olish imkonini beradi
    if message.text == "Xabar":
        bot.send_message(message.chat.id,"Xabar")
    elif message.text == "1":
        bot.send_photo(message.chat.id,"https://t.me/adix7pro/96",caption="Rasm",reply_markup = keyboard1)
    elif message.text == "2":
        bot.send_video(message.chat.id,"https://t.me/adix7pro/86",caption="Video")
    elif message.text == "3":
        bot.send_audio(message.chat.id,"https://t.me/adix7pro/103",caption="Audio")
    elif message.text == "4":
        bot.send_document(message.chat.id,"https://t.me/adix7pro/100",caption="Document")
    elif message.text == "Bosh Menu":
        bot.send_message(message.chat.id,"Bosh menuga qaytdingiz",reply_markup = keyboard)


bot.polling()


