#electro Project 
#Ur Motherfucker If U Kang And Don't Give Creadits 🥴

from os import path

from pyrogram import Client, filters
from pyrogram.types import Message

from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command, other_filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command(["alive", f"alive@{RiCHA_X_NiTiNBOT}"]))
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"https://telegra.ph/file/24711daafd422d2cba969.png",
        caption=f"""**➮� ʜɪɪ ɪ ᴍ [{RiCHA_X_NiTiNBOT}](https://t.me/{RiCHA_X_NiTiNBOT})**

➮ **electro Sყʂƚҽɱ Wσɾƙιɳɠ Fιɳҽ**

➮ **electro ᴠᴇʀꜱɪᴏɴ : 5.0 Lҽƚҽʂƚ**

➮ **ᴍʏ ᴏᴡɴᴇʀ : [{its_devil_xd}](https://t.me/{its_devil_xd})**

➮ **ꜱᴇʀᴠɪᴄᴇ ᴜᴘᴛɪᴍᴇ : `{uptime}`**

**𝚃𝚑𝚊𝚗𝚔𝚜 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 electro 𝙱𝚘𝚝𝚜 ♥️**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫 ɢʀᴏᴜᴘ", url=f"https://t.me/electro_udates"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ ☑️", url=f"https://t.me/electro_updates"
                    )
                ]
            ]
        )
    )
