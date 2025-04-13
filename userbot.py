from time import sleep
from pyrogram.client import Client
from config import api_id, api_hash, finder_music_id

from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler
from pyrogram.types import User, Message, Update 
from pyrogram import filters
import main as spoti

import asyncio

app = Client("my_account", api_id, api_hash)
curr_idx = -1 
tracks = None



async def inline_keyboard_handler(client: User, message: Message):
    # message.reply_inline_bot_result
    # markup = message.reply_markup
    # keyboard = markup.inline_keyboard
    await message.click(0)

async def music_handler(client: User, message: Message):
    await app.download_media(message)
    await ask_for_next_track()



async def get_track_list():
    global tracks, curr_idx
    spot_app = spoti.App()
    temp_tracks = spot_app.get_playlist_tracks('23cMVZslIc26puFc10KjcH')
    tracks_str = spoti.track_to_arr_str(temp_tracks)
    tracks = tracks_str
    print("Downloaded tracks:")
    print(tracks)
    curr_idx = 0

async def ask_for_next_track():
    global curr_idx
    if curr_idx == -1 or curr_idx > len(tracks or []):
        return

    print(f"track_id: {curr_idx} | track: {tracks[curr_idx]}")
    await app.send_message("@fmusbot", tracks[curr_idx])
    curr_idx += 1

async def main():
    await app.start()  
    await asyncio.sleep(2)
    await get_track_list()
    await asyncio.sleep(2)
    await ask_for_next_track()
    await asyncio.sleep(2)
    # await app.send_message("@fmusbot", "test hello")
    await app.stop()  

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    app.add_handler(MessageHandler(inline_keyboard_handler, filters.inline_keyboard))
    app.add_handler(MessageHandler(music_handler, filters.audio))
    app.run()

