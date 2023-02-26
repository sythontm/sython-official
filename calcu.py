import telethon
from telethon import events
from config import *


def calc(num1, num2, fun):
    if fun == "+":
        return num1 + num2
    elif fun == "-":
        return num1 - num2
    elif fun == "*":
        return num1 * num2
    elif fun == "X":
        return num1 * num2
    elif fun == "x":
        return num1 * num2
    elif fun == "/":
        return num1 / num2
    elif fun == "÷":
        return num1 / num2
    else:
        return "خطأ"


@sython.on(events.NewMessage(outgoing=True, pattern=".احسب (.*)"))
async def _(event):
    try:
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        num1 = int(msg[0])
        num2 = int(msg[2])
        fun = str(msg[1])
        await event.edit(f''' الناتج = `{calc(num1, num2, fun)}`''')
    except:
        await event.edit('''خطأ, يرجى ادخال الرقم مثل :
7 + 7
7 - 7
7 x 7
7 ÷ 7''')