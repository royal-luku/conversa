import os


# ==============================================
API_ID = int(os.getenv("API_ID", "22532891")) # TG API ID
API_HASH = os.getenv("API_HASH", "f2b6b1f0570fe18c8213e64c477a81d2") # TG API HASH
BOT_TOKEN = os.getenv("BOT_TOKEN", "7636709703:AAHLlebiXdoIKqHEd3SDBfaAzp5JWxZujF8") # TG BOT TOKOEN
# ================================================

# ===================================================
BOT_OWNER = int(os.getenv("BOT_OWNER", "7039261734")) # BOT OWNER TELEGRAM ID
AI_LOGS = int(os.getenv("AI_LOGS", "-1002331922167")) # AI REPLY LOGS CHANNEL ID
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002331922167")) # LOG CHANNEL ID
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "werdevelopers") # FOR FSUB CHANNEL USERNAME WITHOUT @
# ===================================================

# DATABASE SECTION
# =====================================================
DATABASE_URL = os.getenv("DATABASE_URL",  "mongodb+srv://starcinebot:mkooaa@werdeveloper.vxfam.mongodb.net/?retryWrites=true&w=majority&appName=werdeveloper")
DATABASE_NAME = os.getenv("DATABASE_NAME", "CONVERSA")
# =====================================================

TUTORIAL_VIDEO_LINK = os.getenv("TUTORIAL_VIDEO_LINK", "https://t.me/Hotstar_movies_online/119")

# SCRIPT SECTION
# =====================================================
START_TEXT = """**Hey, {}!

Welcome to Conversa Ai – your advanced AI chatbot.

I’m here to help you with anything you need.
__Click on "Help" for more details and discover what I can do for you!__**"""

HELP_TEXT = """**Here’s what you can do:

Direct Message: __Simply send me a message with your query, and I’ll respond instantly.__

Scan Image Feature: __You can send images for analysis or processing. Just send an image!__

Personalized Assistance: __This is your very own personal AI chatbot. It’s designed to assist you directly and privately.__

Note: It doesn’t work in groups – only one-on-one conversations.**"""

ABOUT_TEXT = """**My Name : [Conversa Ai](https://telegram.me/werdevelopers)
Language : Python
Library : Pyrogram
Server : [Seenode](https://www.seenode.com)
Bot Version : V1.2 (STABLE)**"""

PROMPT = """You are a helpful assistant bot on Telegram named "Conversa AI", You are a Python-programmed Telegram AI chat bot. Your developer created you to solve problems in any field. Your developer is "Werdeveloper", who belongs to India, and his contact ID is his Telegram username @werdeveloper. your all reply must be in hinglish"""
# =======================================================
