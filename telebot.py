### telebot.py start ###
from cred import TOKEN, correct_chat_id
import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from selenium import webdriver
from single import single

### setting up the telegram bot with telepot ###
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    # pprint(msg)

    keyboard_person_amount = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Alleine', callback_data='alone')],
            [InlineKeyboardButton(text='Zu zweit', callback_data='group')],
        ])

    # checking for the correct username
    if chat_id != correct_chat_id:
        bot.sendMessage(chat_id, 'Bad chat_id')
        return

    ### hier werden generelle chat nachrichten ausgwertet ###
    # note: msg['text'] liesst nachricht aus
    if msg['text'] == 'Gib Tisch':
        bot.sendMessage(chat_id, 
            'Hallo Matthias, bist du alleine oder sollen zwei Plätze reserviert werden?',
            reply_markup=keyboard_person_amount)

    if len(msg['text']) == 4:
        # we are just gonna assume that its a code and that it is correct
        single(webdriver.Firefox(), msg['text'])

def on_callback_query(msg):
    print('hi')
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    ### hier kann die antwort mit Buttons ausgewertet werden ###
    bot.answerCallbackQuery(query_id, text='Ok')

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
    'callback_query': on_callback_query}).run_as_thread()

print('Listening...')

while 1:
    time.sleep(10)

### telebot.py end ###
