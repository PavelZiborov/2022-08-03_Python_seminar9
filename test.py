from isOdd import *
import easygui

# print(isOdd(1)) 
# print(isOdd(4))

# easygui.ynbox('Shall I continue?', 'Title', ('Yes', 'No'))
# easygui.msgbox('This is a basic message box.', 'Title Goes Here')
# easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry'))



from telegram import *
from telegram.ext import *
import sys


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'{update.effective_user.first_name}, Я готов к работе.')

def stop(update: Update, context: CallbackContext) -> None:
    sys.exit()

def UserMessage(update: Update, context: CallbackContext):
    if(update.message.text == "Кто ты?"):
        update.message.reply_text("Бот")
    else:
        try:
            update.message.reply_text(eval(update.message.text)) # калькулятор
        except:
            update.message.reply_text("Не понятно")


def coding(update: Update, context: CallbackContext):
    text = update.message.text
    count = 1
    A = ''
    for i in range(0,len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            A = A + str(count) + text[i]
            count = 1
    A = A + str(count) + text[-1]
    update.message.reply_text(f'{A}')



updater = Updater('5489651106:AAFJJZ6fP2GqzgVPv64NrtDy9NGH9wxQKmk')

updater.dispatcher.add_handler(CommandHandler('hello', hello)) # добавляем команду hello 
updater.dispatcher.add_handler(CommandHandler('start', start)) # добавляем команду start 
updater.dispatcher.add_handler(CommandHandler('stop', stop)) # добавляем команду stop 

updater.dispatcher.add_handler(MessageHandler(Filters.text, UserMessage)) # калькулятор eval
# updater.dispatcher.add_handler(MessageHandler(Filters.text, coding)) # алгоритм RLE 


print('server start')
updater.start_polling()
updater.idle()

