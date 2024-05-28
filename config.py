from os import environ 

class Config:
    API_ID = environ.get("API_ID", "24709391")
    API_HASH = environ.get("API_HASH", "cb1ba6bba27a3c68d219e5e34419cb5e")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7048485481:AAGpzNWV-hSxkmpXhfEIpVnL2CE-ztuIWC4") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://24x7repairsericecenter:CKHPNQA8IaEiVGpt@saveee.cbx213c.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "24x7repairsericecenter")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1923238241').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
