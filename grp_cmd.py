import requests
from Mangandi import ImageUploader
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from vars import *

@Client.on_message(filters.command("scan_img"))
async def scan_ph(client, message):
    if message.chat.type == "private":
        return await message.reply_text("❗ You don't need to use this command here. Send me your query directly!")

    reply = message.reply_to_message    
    if not reply:
        return await message.reply_text("📸 Please reply to a photo to use this command!")
    if not reply.photo:
        return await message.reply_text("📸 The replied message is not a photo!")
    
    query = message.text.split(" ", 1)[1] if len(message.text.split(" ")) > 1 else ""    
    if not query:
        return await message.reply_text("❗ Please provide a query! For example: `/scan_img tell me about this image`")

    k = await message.reply_text(f"🔍 {message.from_user.mention}, Please wait while I check...")
    try:
        media = await reply.download()
        await k.edit("✅ Successfully downloaded the image, now checking your query...")
        mag = ImageUploader(media)
        img_url = mag.upload()
        api_url = "https://horridapi.onrender.com/search"
        response = requests.get(f"{api_url}?img={img_url}&query={query}")
        if response.status_code == 200:
            result = response.json()
            await k.edit(f"👤 {message.from_user.mention}, here's what I found: {result.get('response', 'No details found.')}")
        else:
            await k.edit("⚠️ There was an error processing your request. Please try again later.")
    except Exception as e:
        await k.edit("❌ **An error occurred while processing your request.**")
        print(f"Error: {e}")

@Client.on_message(filters.command("gpt"))
async def group_ai_reply(client, message):
    if message.chat.type == "private":
        return await message.reply_text("No need to use this here, send me your query directly!")
    
    input_text = message.text.split(" ", 1)[1] if len(message.text.split(" ")) > 1 else ""
    if not input_text:
        return await message.reply_text("❗ Please provide a query! For example: `/gpt your question`")

    searching_message = await message.reply_text("🔍 Searching...")
    query = f"{PROMPT}, so my question is ({input_text})"
    url = f"https://darkness.ashlynn.workers.dev/chat/?prompt={query}"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("successful") == "success" and data.get("status") == 200:
            response_text = data.get("response")
            await client.send_message(
                chat_id=AI_LOGS,
                text=f"👤 {message.from_user.mention} (`{message.from_user.id}`)\n\n**Query:** `{input_text}`\n\n**AI Generated Response:**\n`{response_text}`",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Close', callback_data='close')]])
            )
            await searching_message.edit_text(
                f"**{message.from_user.mention},** {response_text}",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Close', callback_data='close')]])
            )
        else:
            await searching_message.edit_text("**⚠️ Sorry, could not fetch a valid response. Please try again later.**")
    except Exception as e:
        await searching_message.edit_text("**⚠️ Sorry, an error occurred while fetching the response. Please try again later.**")
        print(f"Error: {e}")
      
