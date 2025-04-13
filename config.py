import configparser

config = configparser.ConfigParser()
config.read("config.ini")
api_id = config.get("pyrogram", "api_id")
api_hash = config.get("pyrogram", "api_hash")
finder_music_id = 515120928
