import os

BOT_OWNER = int(os.getenv("BOT_OWNER", "7039261734"))
API_ID = int(os.getenv("API_ID", "22532891"))
API_HASH = os.getenv("API_HASH", "f2b6b1f0570fe18c8213e64c477a81d2")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7636709703:AAHLlebiXdoIKqHEd3SDBfaAzp5JWxZujF8")
BOT_NAME = "Conversa Ai: Powered by Open-Ai"
AI_LOGS = int(os.getenv("AI_LOGS", "-1002331922167"))
DATABASE_URL = os.getenv("DATABASE_URL",  "mongodb+srv://starcinebot:mkooaa@werdeveloper.vxfam.mongodb.net/?retryWrites=true&w=majority&appName=werdeveloper")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002331922167"))
HELP_TEXT = """**Do you really need my help to use me?

Nothing; just send me your questions, and I will try to reply with your answers. I was made to solve your problems and questions.**"""

ABOUT_TEXT = """**My Details 

My Name : [Conversa Ai: Powered by Open-Ai](https://telegram.me/werdevelopers)
Language : Python
Library : Pyrogram
Server : [Seenode](https://www.seenode.com)
Bot Version : V1 (Beta)**"""

START_TEXT = """**Hey, {}
I am {}
What can I do?

Click on help for more details.**"""

UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "werdevelopers")

PROMPT = """You are a helpful assistant bot on Telegram named "Conversa AI", You are a Python-programmed Telegram AI chat bot. Your developer created you to solve problems in any field. Your developer is "Werdeveloper", who belongs to India, and his contact ID is his Telegram username @werdeveloper."""
