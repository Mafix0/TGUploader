import os
class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = "c2348abe-1048-4da0-915c-75e9f30b60ec"
    # get a token from @BotFather
    TG_BOT_TOKEN = "6396672577:AAFZlY6Gi17e_AlqnaRYmk3YS5gYsFLYa68"
    # The Telegram API things
    APP_ID = 26489380
    API_HASH = "4167d8b8779aab33b73810feb3c77021"
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = "932420516"
    # Banned Unwanted Members..
    BANNED_USERS = []
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 1572864000
    TG_MAX_FILE_SIZE = 1572864000
    FREE_USER_MAX_FILE_SIZE = 1572864000
    # chunk size that should be used with requests
    CHUNK_SIZE = 128
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
