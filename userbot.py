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
tracks = ['Omneum Finalfix Audio  Resonance (Audio Remix)', 'Neonlight Finalfix  Denunziant - Finalfix Remix', 'Prolix Black Sun Empire Finalfix Virus Syndicate  Savages - Finalfix Remix', 'Omneum  Deep Dive', 'Omneum Finalfix  Resonance', 'Finalfix  End Of Days', 'Finalfix  Apocalypse', 'Finalfix  Hope Is Lost', 'Finalfix  The Prophecy', 'Finalfix KRYOS  With You - Finalfix Remix', 'Silent Extent Finalfix  Falling Down - Finalfix Remix', 'Finalfix  Hypocrites', 'Finalfix  Under My Skin', 'Finalfix  Out of Place', 'Finalfix  Idle Hands', 'Neonlight Burr Oak  Triumph - Burr Oak Remix', 'Xylym  Black Hole Heavy', 'Sinister Souls Pythius Merikan  Ultimatum - Merikan Remix', 'Absu_NTQL Shmidoo IO  Ragnarok', 'Transforma  Quantum Leap - Original Mix', 'Absu_NTQL  Broken', 'Paperclip 3XIL3  Kernel - Original Mix', 'First Person  Disconnected Society', 'Meph Notequal  Ironforge', 'Meph Notequal  Dystopian', 'Ekwols  Drowning', 'Gydra 2Whales  Caravan', 'Paperclip 3xil3  Гагарин', 'OMNEUM  Avenoir', 'Skellytn  Breaking Point', 'Magnetude  Still There', 'Task Horizon  Wire Head', 'Mizo  Katana', 'Metanoia  The Edge', 'Sam Foxx  Nuke', 'Agressor Bunx  Vibrations', 'Mean Teeth TR Tactics  3 Minutes - TR TACTICS Remix', 'Sinister Souls Fragz Hallucinator  Alive', 'Redpill Magnetude  Air Strike', 'Neonlight Finalfix  Denunziant - Finalfix Remix', 'Dropset  Ignition', 'Mizo  Rage Out', 'Tobax  Heidelore', 'Absu_NTQL  Ritual Impulse', 'Prolix  Dynamite', 'Mob Tactics  Dirtgrub', 'Killbox  Ultimatum', 'Gydra  Solar Eclipse', 'Mean Teeth Myselor  Shut Them Down - Myselor Remix', 'Skellytn Coppa  Keys To The Rave (feat. Coppa)', 'Skrimor  Soul Splitters', 'Nuvertal  Nine', 'Skellytn  Oracle Protocol', 'Misanthrop  Alert', 'IHR  Kiku', 'Finalfix Receptor  Hydraulic', 'Nuvertal  The Cure', 'ABIS  Grains Of Suna', 'Paperclip 3XIL3  Misterio', 'Qo Symplex  Get Wild', 'RAIDO Absu_NTQL  Hold It Down', 'Finalfix Neolyth  Cerberus', 'Mizo  Dust Devil', 'Burr Oak NickBee  Life Is Lost', 'Audio AENYGMA  Blood On Our Hands', 'Burr Oak  All Alone', 'The Clamps  Snakes & Cowards', 'A-Cray Absu_NTQL  Anvil', 'State of Mind Coppa  Red Sky', 'Killbox  Epicentre', 'Punchman  Biceps Gun', 'Gancher & Ruin  Rituals', 'Pythius REEBZ Burr Oak  Erase Me - Burr Oak Remix', 'Cyntax The Fi5th  Machines', 'Audio  Bedlam Axis', 'Meph Gexan Vici  Hope - Vici Remix', 'Volatile Cycle Dropset Konquest  Alone', 'Audio Burr Oak  Rave Machine', 'TR Tactics  New Danger', 'Burr Oak TR Tactics  Washoku', 'Gancher & Ruin  Kickback', 'Nuvertal  Sharp', 'Mizo Nuvertal  Harder', 'Burr Oak  Strafe', 'RAIDO  Evil Eye', 'Gancher & Ruin  Where Are You', 'Nuvertal  Combat Sword', 'Gancher & Ruin  Flat Earth', 'Nuvertal  In My Head', 'Burr Oak  Symbolic', 'Burr Oak  Originate', 'Gancher & Ruin  Blood Money', 'The Clamps  Click Clack', 'Burr Oak  Time Has Come', 'Gancher & Ruin  Wake Up', 'Killbox  Bound to Others', 'Burr Oak  Save These Days', 'Gancher & Ruin  Courage', 'Task Horizon  Astroturf', 'Gancher & Ruin  Gangsta', 'Despersion  Offensive', 'Burr Oak  Reaper', 'Gancher & Ruin  ARRIVAL', 'Burr Oak  All I Dream', 'TRCD Binary  Deep Vision - Binary Remix', 'TR Tactics Symplex  Halloween VIP', 'Sindicate  Listen Up', "Burr Oak  J'laisse Des Traces (J'Pars En Vrille)", 'Gancher & Ruin  5G', 'Sindicate  Smack In The Face', 'The Clamps  From Dust To Dawn', 'Cyntax  Darkness Surrounding', 'Mizo Sindicate  Mechanical Paw - Sindicate Remix', 'Joe Ford  Tomb Raver', 'HighThere Kaizen Flow  Prisoner', 'Impex Konquest  Sin Sister', 'Omneum  Blade Dance', 'Redpill  Flesh & Blood', 'BADVOID PERSONA NON GRATA  KEEP IT HARDCORE', 'Celldweller Styles Of Beyond Zardonic Pythius  Shapeshifter (feat. Styles of Beyond) - Zardonic & Pythius Remix', 'Audio Black Sun Empire  Genesis Device - Black Sun Empire Remix', 'Overtune Audio  Nothing Will Survive - Audio Remix', 'Audio Black Sun Empire  Disruptive', 'Mr.Frenkie Audio  Bass Symptom - Audio Remix', 'Pythius Neonlight  Tarkin', 'Pythius Neonlight  Sovereign - Neonlight Remix', 'Emperor  I Was', 'TR Tactics  Sound Gun', 'TR Tactics HighThere  Shrouded', 'Pythius REEBZ Burr Oak  Erase Me - Burr Oak Remix', 'Dom & Roland  Tone Poem', 'Neonlight & Hedj  Hammerhead', 'X-Korp  Jurassa - Original Mix', 'Gexan  Time Tick', 'A.M.C  Bass', 'Task Horizon Tenkei SLWDWN  Mindfragger - SLWDWN Remix', 'Transforma  Well Oiled Machine', 'IRONTYPE  I Do', 'Redpill Metanoia  Flash Point - Metanoia Remix', 'Cyntax  Eat It', '3xil3  Outblow', 'Cyntax  Face Pound', 'Gydra  Noise Of The Machine', 'Gydra  Noise Of The Machine - VIP', 'Redpill Black Sun Empire Virus Syndicate  Executionist', 'Burr Oak  Somewhere We Belong', 'Burr Oak  Far From Home', 'Absu_NTQL  Conclusion VIP', 'The Clamps  Les Autres', 'A.M.C Junk Mail  Operator - Junk Mail Remix', 'Redpill Ed Rush  Interlinked', 'Gydra  Om', 'Redpill  Slap The Bassline', 'Merikan  Altered States', 'Despersion  Peace', 'Paperclip 3xil3  Vacuum', 'Sinister Souls TR Tactics  Never 2 Late', 'Eluun The Clamps  Glassy Star', 'Opsen  Décadence', 'Audio Black Sun Empire Burr Oak  Disruptive - Burr Oak Remix', 'AKOV  Snake Eater - AKOV Remix', 'Zigi SC  Dementor', 'TR Tactics  Against The Grain', 'Submonitor  The Light', 'Holotrope Karpa  Evacuation', 'Submonitor  Biologica', 'Holotrope  Corridor Pulse - VIP', 'Submonitor  Right Now', 'Zombie Cats  Hellcat', 'Omneum  Liminal Visions', 'Holotrope Karpa  Converted', 'Tayn  Nebula Groove', 'Finalfix  Melting Pot', 'Zigi SC Karpa  Childsplay', 'Kevala Phenom  Simulated Freedom', "Audio  Don't Play", 'Omneum  Cybernetic Modules', 'Omneum  Psi Reaver', 'Despersion  Show Me', 'Gancher & Ruin  PSYOP', 'Current Value  Triple', 'TR Tactics TRCD  Facebreaker', 'RAIDO  Breakdown', 'Noisia  Anomaly', 'Absu_NTQL  Urusai', 'Joe Ford Task Horizon Ekwols  Sunfall', 'HighThere MiRo  Depart The Ends', 'Absu_NTQL Tremr  Summon', 'Phenom & Discharge  Goblin']
# tracks = ['Omneum Finalfix Audio  Resonance (Audio Remix)', 'Neonlight Finalfix  Denunziant - Finalfix Remix', 'Prolix Black Sun Empire Finalfix Virus Syndicate  Savages - Finalfix Remix', 'Omneum  Deep Dive', 'Omneum Finalfix  Resonance', 'Finalfix  End Of Days', 'Finalfix  Apocalypse', 'Finalfix  Hope Is Lost', 'Finalfix  The Prophecy', 'Finalfix KRYOS  With You - Finalfix Remix', 'Silent Extent Finalfix  Falling Down - Finalfix Remix', 'Finalfix  Hypocrites', 'Finalfix  Under My Skin', 'Finalfix  Out of Place', 'Finalfix  Idle Hands', 'Neonlight Burr Oak  Triumph - Burr Oak Remix', 'Xylym  Black Hole Heavy', 'Sinister Souls Pythius Merikan  Ultimatum - Merikan Remix', 'Absu_NTQL Shmidoo IO  Ragnarok', 'Transforma  Quantum Leap - Original Mix', 'Absu_NTQL  Broken', 'Paperclip 3XIL3  Kernel - Original Mix', 'First Person  Disconnected Society', 'Meph Notequal  Ironforge', 'Meph Notequal  Dystopian', 'Ekwols  Drowning', 'Gydra 2Whales  Caravan', 'Paperclip 3xil3  Гагарин', 'OMNEUM  Avenoir', 'Skellytn  Breaking Point', 'Magnetude  Still There', 'Task Horizon  Wire Head', 'Mizo  Katana', 'Metanoia  The Edge', 'Sam Foxx  Nuke', 'Agressor Bunx  Vibrations', 'Mean Teeth TR Tactics  3 Minutes - TR TACTICS Remix', 'Sinister Souls Fragz Hallucinator  Alive', 'Redpill Magnetude  Air Strike', 'Neonlight Finalfix  Denunziant - Finalfix Remix', 'Dropset  Ignition', 'Mizo  Rage Out', 'Tobax  Heidelore', 'Absu_NTQL  Ritual Impulse', 'Prolix  Dynamite', 'Mob Tactics  Dirtgrub', 'Killbox  Ultimatum', 'Gydra  Solar Eclipse', 'Mean Teeth Myselor  Shut Them Down - Myselor Remix', 'Skellytn Coppa  Keys To The Rave (feat. Coppa)', 'Skrimor  Soul Splitters', 'Nuvertal  Nine', 'Skellytn  Oracle Protocol', 'Misanthrop  Alert', 'IHR  Kiku', 'Finalfix Receptor  Hydraulic', 'Nuvertal  The Cure', 'ABIS  Grains Of Suna', 'Paperclip 3XIL3  Misterio', 'Qo Symplex  Get Wild', 'RAIDO Absu_NTQL  Hold It Down', 'Finalfix Neolyth  Cerberus', 'Mizo  Dust Devil', 'Burr Oak NickBee  Life Is Lost', 'Audio AENYGMA  Blood On Our Hands', 'Burr Oak  All Alone', 'The Clamps  Snakes & Cowards', 'A-Cray Absu_NTQL  Anvil', 'State of Mind Coppa  Red Sky', 'Killbox  Epicentre', 'Punchman  Biceps Gun', 'Gancher & Ruin  Rituals', 'Pythius REEBZ Burr Oak  Erase Me - Burr Oak Remix', 'Cyntax The Fi5th  Machines', 'Audio  Bedlam Axis', 'Meph Gexan Vici  Hope - Vici Remix', 'Volatile Cycle Dropset Konquest  Alone', 'Audio Burr Oak  Rave Machine', 'TR Tactics  New Danger', 'Burr Oak TR Tactics  Washoku', 'Gancher & Ruin  Kickback', 'Nuvertal  Sharp', 'Mizo Nuvertal  Harder', 'Burr Oak  Strafe', 'RAIDO  Evil Eye', 'Gancher & Ruin  Where Are You', 'Nuvertal  Combat Sword', 'Gancher & Ruin  Flat Earth', 'Nuvertal  In My Head', 'Burr Oak  Symbolic', 'Burr Oak  Originate', 'Gancher & Ruin  Blood Money', 'The Clamps  Click Clack', 'Burr Oak  Time Has Come', 'Gancher & Ruin  Wake Up', 'Killbox  Bound to Others', 'Burr Oak  Save These Days', 'Gancher & Ruin  Courage', 'Task Horizon  Astroturf', 'Gancher & Ruin  Gangsta', 'Despersion  Offensive', 'Burr Oak  Reaper', 'Gancher & Ruin  ARRIVAL', 'Burr Oak  All I Dream', 'TRCD Binary  Deep Vision - Binary Remix', 'TR Tactics Symplex  Halloween VIP', 'Sindicate  Listen Up', "Burr Oak  J'laisse Des Traces (J'Pars En Vrille)", 'Gancher & Ruin  5G', 'Sindicate  Smack In The Face', 'The Clamps  From Dust To Dawn', 'Cyntax  Darkness Surrounding', 'Mizo Sindicate  Mechanical Paw - Sindicate Remix', 'Joe Ford  Tomb Raver', 'HighThere Kaizen Flow  Prisoner', 'Impex Konquest  Sin Sister', 'Omneum  Blade Dance', 'Redpill  Flesh & Blood', 'BADVOID PERSONA NON GRATA  KEEP IT HARDCORE', 'Celldweller Styles Of Beyond Zardonic Pythius  Shapeshifter (feat. Styles of Beyond) - Zardonic & Pythius Remix', 'Audio Black Sun Empire  Genesis Device - Black Sun Empire Remix', 'Overtune Audio  Nothing Will Survive - Audio Remix', 'Audio Black Sun Empire  Disruptive', 'Mr.Frenkie Audio  Bass Symptom - Audio Remix', 'Pythius Neonlight  Tarkin', 'Pythius Neonlight  Sovereign - Neonlight Remix', 'Emperor  I Was', 'TR Tactics  Sound Gun', 'TR Tactics HighThere  Shrouded', 'Pythius REEBZ Burr Oak  Erase Me - Burr Oak Remix', 'Dom & Roland  Tone Poem', 'Neonlight & Hedj  Hammerhead', 'X-Korp  Jurassa - Original Mix', 'Gexan  Time Tick', 'A.M.C  Bass', 'Task Horizon Tenkei SLWDWN  Mindfragger - SLWDWN Remix', 'Transforma  Well Oiled Machine', 'IRONTYPE  I Do', 'Redpill Metanoia  Flash Point - Metanoia Remix', 'Cyntax  Eat It', '3xil3  Outblow', 'Cyntax  Face Pound', 'Gydra  Noise Of The Machine', 'Gydra  Noise Of The Machine - VIP', 'Redpill Black Sun Empire Virus Syndicate  Executionist', 'Burr Oak  Somewhere We Belong', 'Burr Oak  Far From Home', 'Absu_NTQL  Conclusion VIP', 'The Clamps  Les Autres', 'A.M.C Junk Mail  Operator - Junk Mail Remix', 'Redpill Ed Rush  Interlinked', 'Gydra  Om', 'Redpill  Slap The Bassline', 'Merikan  Altered States', 'Despersion  Peace', 'Paperclip 3xil3  Vacuum', 'Sinister Souls TR Tactics  Never 2 Late', 'Eluun The Clamps  Glassy Star', 'Opsen  Décadence', 'Audio Black Sun Empire Burr Oak  Disruptive - Burr Oak Remix', 'AKOV  Snake Eater - AKOV Remix', 'Zigi SC  Dementor', 'TR Tactics  Against The Grain', 'Submonitor  The Light', 'Holotrope Karpa  Evacuation', 'Submonitor  Biologica', 'Holotrope  Corridor Pulse - VIP', 'Submonitor  Right Now', 'Zombie Cats  Hellcat', 'Omneum  Liminal Visions', 'Holotrope Karpa  Converted', 'Tayn  Nebula Groove', 'Finalfix  Melting Pot', 'Zigi SC Karpa  Childsplay', 'Kevala Phenom  Simulated Freedom', "Audio  Don't Play", 'Omneum  Cybernetic Modules', 'Omneum  Psi Reaver', 'Despersion  Show Me', 'Gancher & Ruin  PSYOP', 'Current Value  Triple', 'TR Tactics TRCD  Facebreaker', 'RAIDO  Breakdown', 'Noisia  Anomaly', 'Absu_NTQL  Urusai', 'Joe Ford Task Horizon Ekwols  Sunfall', 'HighThere MiRo  Depart The Ends', 'Absu_NTQL Tremr  Summon', 'Phenom & Discharge  Goblin']



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


async def get_track_list():
    global tracks, curr_idx
    spot_app = SpotiApp()
    temp_tracks = spot_app.get_playlist_tracks('3gHIyBVPhS1p1er6tYpXmQ')
    tracks_str = spoti.track_to_arr_str(temp_tracks)
    remove_tracks = ['Finalfix  The Forbidden Fruit', 'Absu_NTQL Zigi SC  Temple', 'Ekwols  Hyena', 'Finalfix  Forsaken', 'Magnetude Receptor  Goodbye', 'Cyntax  Pericardium', 'Gydra Jade Venom  Ikra - Jade Venom Remix', 'Cyntax  Your Time Is Now', 'Magnetude  Broken', 'Burr Oak  Criminal Romance', 'Ovtlier Zardonic Chris Motionless Ekwols  Warriors - Remix', 'Pythius REEBZ  In My Head', 'Gancher & Ruin  Interceptor', 'BADVOID  CAUTION', 'Manta  Home', 'Paperclip 3xil3  Velorok', 'Joe Ford  Into Black', 'Burr Oak  Ground & Pound', 'The Clamps  Faith', 'Gancher & Ruin  Watch Me', 'Gancher & Ruin  Chemtrail', 'Despersion Taras Umansky  Everything (VIP)', 'The Clamps  Where Secrets Lie', 'Burr Oak  Do Androids Dream', 'The Clamps  The Bill', 'Futura Boombox Zardonic Ekwols  This Is Our Future ( Control Machine )', 'Tokkobana Gancher & Ruin Julia Do  Wake Up - Gancher & Ruin Remix', 'Prolix Black Sun Empire  The Message VIP', 'TR Tactics 2Whales  Weak - VIP', 'Redpill Black Sun Empire Burr Oak Virus Syndicate  Executionist - Burr Oak Remix', 'A.M.C Teddy Killerz  Bass - Teddy Killerz Remix', 'Transforma  Ghouls', 'Transforma Xylym  It Came From The Dark', 'Gancher & Ruin Raizer  Meds (feat. Raizer)', 'Zigi SC Balron  Stepper - Balron Remix', 'Erb n Dub Disruption UK  Loud Mouth - Disruption UK Remix', 'Redpill  The Chase', 'Finalfix  Arrival', 'A.way Thez  Half Life 3', 'Opsen  Give Them Hell', 'Zombie Cats Sinister Souls  Hard Spin', 'Finalfix  Purgatory', 'Zombie Cats Tanukichi  Hellcat - Tanukichi Remix', 'Disphonia  Entropy', 'Absu_NTQL A-Cray  Shards', 'Submonitor  Let Go', 'Omneum  Correspondence', 'First Person  Take You Higher', 'Omneum  Thorns', 'Karpa  Serpent', 'Paperclip  Vitamin A - Original Mix', 'Magnetude  The Star', 'Diode  SKNK', 'SLWDWN Absu_NTQL  The Rift (Darkshire Festival Anthem 2025)', 'Eluun Burr Oak  Hysteria - Eluun & Burr Oak Cover', 'Black Sun Empire Burr Oak  Steppenwolf']
    tracks_str = remove_sub_list_from_list(tracks_str, remove_tracks)
    tracks = tracks_str
    print("Downloaded tracks:")
    print(tracks)
    curr_idx = 0

async def ask_for_next_track():
    global curr_idx
    global tracks
    if curr_idx == -1 or curr_idx > len(tracks or []):
        print("we're here somehow")
        return

    print(f"track_id: {curr_idx} | track: {tracks[curr_idx]}")
    await app.send_message("@LosslessRobot", tracks[curr_idx])
    curr_idx += 1

async def main():
    await app.start()  
    await asyncio.sleep(2)
    await get_track_list()
    await asyncio.sleep(2)
    await ask_for_next_track()
    await asyncio.sleep(2)
    # await app.send_message("@LosslessRobot", "test hello")
    await app.stop()  

if __name__ == "__main__":
    print("")
    app.add_handler(MessageHandler(inline_keyboard_handler, filters.inline_keyboard))
    app.add_handler(MessageHandler(music_handler, filters.audio))
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    app.run()

