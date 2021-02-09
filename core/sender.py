import telebot
import datetime
from core.config import Config


def send_alert(message=str(datetime.datetime.now())):
    """
    This method send an alert notification to the telegram channel
    :return:
    """
    bot = telebot.TeleBot(Config.bot_key)
    bot.send_message(Config.bot_id, message, parse_mode="Markdown")
