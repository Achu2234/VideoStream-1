from pyrogram.types import Message
from pyrogram import Client, filters

from lib.config import USERNAME_BOT


@Client.on_message(filters.command(["start", "start@{USERNAME_BOT}"]))
async def start(client, message):
    await message.reply("**👋 I'm alive**")
