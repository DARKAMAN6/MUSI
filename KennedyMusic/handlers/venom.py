import os
import sys
from pyrogram import Client, filters
from KennedyMusic.helpers.decorators import sudo_users_only
from KennedyMusic.helpers.filters import command, other_filters
from pyrogram.types import Message
from KennedyMusic.config import (
    BOT_USERNAME,
    que,
)

@Client.on_message(command(["restart", f"restart@{BOT_USERNAME}"]) & other_filters)
@sudo_users_only

async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("𝟷")
    await loli.edit("𝟸")
    await loli.edit("𝟹")
    await loli.edit("𝟺")
    await loli.edit("𝟻")
    await loli.edit("𝟼")
    await loli.edit("𝟽")
    await loli.edit("𝟾")
    await loli.edit("𝟿")
    await loli.edit("**✨𝙼𝚄𝚂𝙸𝙲 𝙱𝙾𝚃 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳👻**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
