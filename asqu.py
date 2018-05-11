from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineQueryResultArticle, InputTextMessageContent, ParseMode

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler

import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot,update):
    commandstr="/packages - To receive a document regarding our various packges and its complete details\nFor registration--- \nNote - Enter /command {answer} \nExample: /name akshay\n /name - Enter your name\n /email - Enter your E-mail Id\n /phone Enter your phone number\n /submit - Final submit"
    bot.sendMessage(chat_id=update.message.chat_id, text=commandstr)

def packages(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Please go through this document")
    bot.sendDocument(chat_id=update.message.chat_id, document=open('A2.pdf', 'rb'))

def getname(bot, update):
    get_name = update.message.text.replace('/name','')
    get_name = get_name.replace(' ','')
    global s
    s="Name : "+git_name+'\n'
    bot.sendMessage(chat_id=update.message.chat_id, text="Entered name")

def emailfunc(bot, update):
    email = update.message.text.replace('/email','')
    email = email.replace(' ','')
    if(len(email) < 3):
        update.message.reply_text('🙌 Invalid email, try again.')
    else:
        global s
        s=s+"Email : "+email+'\n'
        bot.sendMessage(chat_id=update.message.chat_id, text="Entered E-Mail ID")

def phonefunc(bot, update):
    user = update.message.from_user
    phone = update.message.text.replace('/phone','')
    phone = phone.replace(' ','')
    if(len(phone) < 10):
        bot.sendMessage(chat_id=update.message.chat_id, text='🙌 Invalid number, try again.')

    else:
        global s
        s=s+"Phone number : "+phone
        bot.sendMessage(chat_id=update.message.chat_id, text="Entered phone number")

def submit(bot, update):
    bot.sendMessage(chat_id=417034564, text=s)  #417034564
    bot.send_photo(chat_id=update.message.chat_id, photo=open('asquareimg.png', 'rb'))
    bot.sendMessage(chat_id=update.message.chat_id, text="Thank you for registering!!! You can expect a call from us anytime soon!!")


updater = Updater(token='') #enter token
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
package_handler = CommandHandler('packages', packages)
name_handler = CommandHandler('name', getname)
email_handler = CommandHandler('email', emailfunc)
phone_handler = CommandHandler('phone', phonefunc)
submit_handler = CommandHandler('submit', submit)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(submit_handler)
dispatcher.add_handler(phone_handler)
dispatcher.add_handler(package_handler)
dispatcher.add_handler(name_handler)
dispatcher.add_handler(email_handler)
updater.start_polling()



