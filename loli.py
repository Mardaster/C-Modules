# ---------------------------------------------------------------------------------
# Name: Loli Hentai!
# Description: words superfluous?
# Author: @codrago_m
# ---------------------------------------------------------------------------------
# 🔒    Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ---------------------------------------------------------------------------------
# Author: @codrago
# Commands: loli, lolic
# scope: hikka_only
# meta developer: @codrago_m
# ---------------------------------------------------------------------------------

__version__ = (1, 5, 3)
import os
import logging
from .. import loader, utils
import random
import time
import datetime
from telethon import functions
from telethon.tl.custom import Message

logger = logging.getLogger("LoliHentai")

@loader.tds
class lolihentai(loader.Module):
    """Your the best friend in loli hentai"""
    strings = {
        "name": "LoliHentai",
        "loading_photo": "<emoji document_id=5215327832040811010>⏳</emoji> <b>loading your loli photo...</b>",
        "error_loading": "<b>Failed to get photos. Please unblock @ferganteusbot</b>",
        "search": "<emoji document_id=5328311576736833844>🔴</emoji> loading your photo..."
    }
    
    async def lolicmd(self, message):
        """-> random loli photo"""

        await utils.answer(message, self.strings("loading_photo"))
        
        async with self._client.conversation("@ferganteusbot") as conv:
            
            await conv.send_message("/lh")
        
            otvet = await conv.get_response()
          
            if otvet.photo:
                phota = await self._client.download_media(otvet.photo, "loli_hentai")
                await message.client.send_message(
                    message.peer_id,
                    file=phota,
                    reply_to=getattr(message, "reply_to_msg_id", None),
                    )

                os.remove(phota)
                
                await message.delete()
                
    async def loliccmd(self, message: Message):
         """-> to get your loli"""
         await message.edit(self.strings("search"))
         time.sleep(0.5)
         chat = "hdjrkdjrkdkd"
         result = await message.client(
             functions.messages.GetHistoryRequest(
                 peer=chat,
                 offset_id=0,
                 offset_date=datetime.datetime.now(),
                 add_offset=random.choice(range(1, 851, 2)),
                 limit=1,
                 max_id=0,
                 min_id=0,
                 hash=0,
             ),
         )
         await message.delete()
         await message.client.send_file(
             message.to_id, 
             result.messages[0].media, 
             reply_to=getattr(message, "reply_to_msg_id", None),
             )
