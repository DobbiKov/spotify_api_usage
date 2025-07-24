from time import sleep
from pyrogram.client import Client
from config import api_id, api_hash, finder_music_id

from main import App as SpotiApp
from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler
from pyrogram.types import User, Message, Update 
from pyrogram import filters
import main as spoti

import asyncio

app = Client("my_account", api_id, api_hash)
curr_idx = 0 
tracks = [''] # insert your tracklist here, you can obtain it using `main.py`



async def inline_keyboard_handler(client: User, message: Message):
    # message.reply_inline_bot_result
    # markup = message.reply_markup
    # keyboard = markup.inline_keyboard
    print("Clicking on the first button")
    await message.click(0)

async def music_handler(client: User, message: Message):
    print("Downloading track")
    await app.download_media(message)
    print("Downloaded successfully")
    await ask_for_next_track()

def remove_sub_list_from_list(main_list: list[str], sub_list: list[str]) -> list[str]:
    res = []
    for elem in main_list:
        if elem in sub_list:
            continue
        else:
            res.append(elem)
    return res


async def ask_for_next_track():
    global curr_idx
    global tracks
    if curr_idx == -1 or curr_idx >= len(tracks or []):
        print("The downloading process has been finished successfully")
        exit(0)

    print(f"track_id: {curr_idx} | track: {tracks[curr_idx]}")
    await app.send_message("@LosslessRobot", tracks[curr_idx])
    curr_idx += 1

if __name__ == "__main__":
    print("Welcome to the music downloader!")
    print("To start downloading, send the first track name to the @LosslessRobot")
    app.add_handler(MessageHandler(inline_keyboard_handler, filters.inline_keyboard))
    app.add_handler(MessageHandler(music_handler, filters.audio))
    app.run()


