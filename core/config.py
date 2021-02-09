import os


class Config():
    refresh_url = os.getenv('URL_REFRESH')
    message_url = os.getenv('URL_MESSAGE')
    user_id = os.getenv('USER_ID')
    bot_id = os.getenv('BOT_ID')
    bot_key = os.getenv('BOT_KEY')
