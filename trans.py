import telethon
from telethon import events
from googletrans import Translator, constants
from config import *
from help import *

tran = Translator()


@sython.on(events.NewMessage(pattern=r"\.ترجمة الى العربية", outgoing=True))
async def _(event):
    reply_message = await event.get_reply_message()
    mes = reply_message.text
    res = tran.translate(str(mes), dest="ar")
    await event.edit(res.text)


@sython.on(events.NewMessage(pattern=r"\.ترجمة الى الانجليزية", outgoing=True))
async def _(event):
    reply_message = await event.get_reply_message()
    mes = reply_message.text
    res = tran.translate(str(mes), dest="en")
    await event.edit(res.text)


@sython.on(events.NewMessage(pattern=r"\.ترجمة الى الفرنسية", outgoing=True))
async def _(event):
    reply_message = await event.get_reply_message()
    mes = reply_message.text
    res = tran.translate(str(mes), dest="fr")
    await event.edit(res.text)


@sython.on(events.NewMessage(pattern=r"\.ترجمة الى الروسية", outgoing=True))
async def _(event):
    reply_message = await event.get_reply_message()
    mes = reply_message.text
    res = tran.translate(str(mes), dest="ru")
    await event.edit(res.text)


@sython.on(events.NewMessage(pattern=r"\.ترجمة الى الاسبانية", outgoing=True))
async def _(event):
    reply_message = await event.get_reply_message()
    mes = reply_message.text
    res = tran.translate(str(mes), dest="es")
    await event.edit(res.text)


