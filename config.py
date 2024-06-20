import os
import time
import re

id_pattern = re.compile(r'^.\d+$')

class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "29917436")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "4a926822b076a086a167fe8f2701d3e9")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7096368570:AAHLrz3TRK_Qv3UXIz4ai4ZrjlgJDzs8n2M")  # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002134585222')  # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(FORCE_SUB) else None
   
    # database config
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://VideoCompresserV02:Video-Compresser_V02@cluster0.fpkayq6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME = os.environ.get("DB_NAME", "Cluster0") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6141937812"))  # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001869105126'))  # ⚠️ Required
    SAVE_CHANNEL = int(os.environ.get('SAVE_CHANNEL', '-1002135731047'))  # ⚠️ Required
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/1272c08f3d634823dc9ad.jpg")

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
