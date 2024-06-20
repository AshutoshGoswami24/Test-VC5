import os
import time
import re

id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "29917436")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "4a926822b076a086a167fe8f2701d3e9")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7226766470:AAEpx_0WhehNcUKu_8sBfiYmbb5tpZteU50")  # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002116868480')  # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(FORCE_SUB) else None
    AUTH_USERS = [7226766470, 7062828064, 6537859]
    # database config
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://botzashu:LjkXI1JoztDQiQlr@cluster0.38ague0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME = os.environ.get("DB_NAME", "Cluster0") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "7062828064"))  # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002185040924'))  # ⚠️ Required
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/765e3b04ea6aa9ae4f7e6.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8085"))

    caption = """
    **File Name**: {0}
    
    **Original File Size:** {1}
    **Encoded File Size:** {2}
    **Compression Percentage:** {3}
    
    __Downloaded in {4}__
    __Encoded in {5}__
    __Uploaded in {6}__
    """
