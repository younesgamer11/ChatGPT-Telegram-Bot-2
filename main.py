import os
from telebot import TeleBot
from api import get_gpt_reply
from server import server

BOT_TOKEN = os.environ['5995932497:AAFS7HNHhjXboW2hoee5ibjqs09v-yDzt7E']

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def on_start(message):
  chat_id = message.chat.id
  text = 'Hello, this bot made by @ChatJpt How may i help you? '
  bot.send_message(chat_id,text)
  return

@bot.message_handler()
def on_message(message):
  chat_id = message.chat.id
  prompt = message.text[:250]
  bot.send_chat_action(chat_id,action='typing')
  text = get_gpt_reply(prompt,500)
  bot.send_message(chat_id,text)
  return

bot.infinity_polling()
