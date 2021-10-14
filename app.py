from telegram import *
from telegram.ext import *
from telegram.ext import updater
from telegram.ext import dispatcher
from telegram.ext import callbackcontext
from requests import Request, Session
import json
import time
import os
PORT = int(os.environ.get('PORT', 5000))

def getInfo (coin,a): # Function to get the info

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest' # Coinmarketcap API url
    parameters = { 'slug': 'coinname', 'convert': 'USD' }
    parameters['slug'] = coin
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '072c4ab9-c08d-4d6b-8c1e-dbd623c5ef10'
    } # Replace 'YOUR_API_KEY' with the API key you have recieved in the previous step

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)

    info = json.loads(response.text)
    #print(info)
    return(info['data'][a]['quote']['USD']['price'] )

bot = Bot("2041688226:AAG1-i1t0Sd2-ylOR6YKU93KsgT8fqXln14")
print(bot.getMe())
updater=Updater("2041688226:AAG1-i1t0Sd2-ylOR6YKU93KsgT8fqXln14",use_context="true")
dispatcher=updater.dispatcher
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.\nPlease press or type /help to see the commands available.")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /BTCprice - To get current price of bitcoin
    /ETHprice - To get current price of ethereum
    /SOLprice - To get current price of solana
    /ADAprice - To get current price of cardano
    /DOGEprice - To get current price of Doge coin""")

def btcprice(update: Update, context: CallbackContext):
    t = getInfo('bitcoin','1')
    update.message.reply_text("current price of bitcoin BTC is "+"%.3f" % t)
    time.sleep(2)
    update.message.reply_text("press /help for available commands")

def ethprice(update: Update, context: CallbackContext):
    t = getInfo('ethereum','1027')
    update.message.reply_text("current price of ethereum ETH is "+"%.3f" % t)
    time.sleep(2)
    update.message.reply_text("press /help for available commands")

def solprice(update: Update, context: CallbackContext):
    t = getInfo('solana','5426')
    update.message.reply_text("current price of solana SOL is "+"%.3f" % t)
    time.sleep(2)
    update.message.reply_text("press /help for available commands")

def adaprice(update: Update, context: CallbackContext):
    t = getInfo('cardano','2010')
    update.message.reply_text("current price of cardano ADA is "+"%.3f" % t)
    time.sleep(2)
    update.message.reply_text("press /help for available commands")

def dogeprice(update: Update, context: CallbackContext):
    t = getInfo('dogecoin','74')
    update.message.reply_text("current price of dogecoin DOGE is "+"%.3f" % t)
    time.sleep(2)
    update.message.reply_text("press /help for available commands")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('BTCprice', btcprice))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('ETHprice', ethprice))
updater.dispatcher.add_handler(CommandHandler('SOLprice', solprice))
updater.dispatcher.add_handler(CommandHandler('ADAprice', adaprice))
updater.dispatcher.add_handler(CommandHandler('DOGEprice', dogeprice))
updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path="2041688226:AAG1-i1t0Sd2-ylOR6YKU93KsgT8fqXln14")
updater.bot.setWebhook('https://yourherokuappname.herokuapp.com/' + "2041688226:AAG1-i1t0Sd2-ylOR6YKU93KsgT8fqXln14")
