import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "5831631494"))
    API_HASH = os.environ.get("API_HASH", "Api hash :  da10f83ffb7b2dc7a2770aade70c4627")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5831631494:AAGpDjl-hPVJW5ym18wMlkAHPvR4E3ug6j8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQBy6lq-LolIlL6S97bom6UPNftbRWtbh_kkCFRw4WSsPXbPnewkKArU5gadbTf4sb9sMyoTHBQXw8DMBDm9Ja9lJUqskC7lWZVpDFg7Q8kCDj0gWxhHepS5BLh_tBQwgp9sQ9A5c4sUxA1KAEAzifN0SWLI1OfiGZfOGMpoa0U0JebWAi7-65C_PfWGZ2c_vum0DLnaa2fdWLAGdZojjIPVJ8vKGZ1D3DTbUdHY0tyqy6Jbk3q9SET3Gh5WxY_SZ8CPReK8oDj7542lnw4zEy_Jjpp1tNsqyACouWjoxQv3io9UfPF90NeNr1_ZuI7Kz65HCUpLJ5Rsg2iUDoyHx_q7AAAAAWHeojgA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@PugsMusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5936947768")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
