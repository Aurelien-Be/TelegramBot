import Constants as keys
import telegram
import random
from time import sleep
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Updater, Filters
import responses as R 

#the bot react when someone post: "/help"
def help_command(update, context):
    context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=telegram.ChatAction.TYPING, timeout=10)
    sleep(3)
    update.message.reply_text("XXX")

#reaction to the bot when messages triggers him    
def handle_message(update, context):
    text = str(update.message.text)
    response = R.sample_responses(text) #words that trigger him in the file responses.py
    if response:  #we add a simulating typing
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=telegram.ChatAction.TYPING)
        sleep(5)
        update.message.reply_text(response) #the bot posts 
        if "XX" in text:
            context.bot.send_sticker(chat_id=update.message.chat_id, sticker="idofthesticker")
    if "XX" in text:
            context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=telegram.ChatAction.TYPING)
            context.bot.send_sticker(chat_id=update.message.chat_id, sticker="idofthesticker")
    elif "XX" in text:
            context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=telegram.ChatAction.TYPING)
            context.bot.send_sticker(chat_id=update.message.chat_id, sticker="idofthesticker")
           

    
rand = random.randint(5,15)

def main():
    updater = Updater(keys.TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("help",help_command))
 
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    updater.start_polling(rand) #the bot checks new messages randomly in order to not be too much robotic
    
    
    updater.idle()
    
main()
