from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
from config import *
import asyncio
from telethon import events
from help import *
c = requests.session()
bot_username = '@t06bot'


@sython.on(events.NewMessage(outgoing=True, pattern=r".تجميع المليار"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython.get_entity(bot_username)
        await sython.send_message('@t06bot', '/start')
        await asyncio.sleep(0)
        msg0 = await sython.get_messages('@t06bot', limit=1)
        await msg0[0].click(0)
        await asyncio.sleep(0)
        msg1 = await sython.get_messages('@t06bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if ispay[0] == 'no':
                break
            await asyncio.sleep(0)

            list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython.send_message(event.chat_id, f"مافي قنوات بلبوت")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython(ImportChatInviteRequest(bott))
                msg2 = await sython.get_messages('@t06bot', limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await sython.send_message(event.chat_id, f"تم الاشتراك في {chs} قناة")
            except:
                await sython.send_message(event.chat_id, f"خطأ , ممكن تبندت")
                break
        await sython.send_message(event.chat_id, "تم الانتهاء من التجميع !")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
