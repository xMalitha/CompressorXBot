

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.reply(
        f"Hi `{ok.user.first_name}`\nᴛʜɪs ɪs ᴀ ᴄᴏᴍᴘʀᴇssᴏʀʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ᴇɴᴄᴏᴅᴇ ᴠɪᴅᴇᴏs.\nʀᴇᴅᴜᴄᴇ sɪᴢᴇ ᴏғ ᴠɪᴅᴇᴏs ᴡɪᴛʜ ɴᴇɢʟɪɢɪʙʟᴇ ǫᴜᴀʟɪᴛʏ ᴄʜᴀɴɢᴇ\nᴜ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ sᴀᴍᴘʟᴇs/sᴄʀᴇᴇɴsʜᴏᴛs ᴛᴏᴏ. 🎉\n🚀 ʙᴏᴛ ʙʏ : @AlphaTm_Botz\n👨‍💻ᴅᴇᴠᴇʟᴏᴘᴇʀ : @xMalitha ",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="github.com/xMalitha/CompressorXBot"),
                Button.url("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/xMalitha"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**🐠 ᴀ ǫᴜᴀʟɪᴛʏ ᴄᴏᴍᴘʀᴇssᴏʀʙᴏᴛ**\n\n✨ ᴛʜɪs ʙᴏᴛ ᴄᴏᴍᴘʀᴇss ᴠɪᴅᴇᴏs ᴡɪᴛʜ ɴᴇɢʟɪɢɪʙʟᴇ ǫᴜᴀʟɪᴛʏ ᴄʜᴀɴɢᴇ.\n✨ ɢᴇɴᴇʀᴀᴛᴇ sᴀᴍᴘʟᴇ ᴄᴏᴍᴘʀᴇssᴇᴅ ᴠɪᴅᴇᴏ\n✨ ᴇᴀsʏ ᴛᴏ ᴜsᴇ\n🎊 ᴅᴜᴇ ᴛᴏ ǫᴜᴀʟɪᴛʏ sᴇᴛᴛɪɴɢs ʙᴏᴛ ᴛᴀᴋᴇs ᴛɪᴍᴇ ᴛᴏ ᴄᴏᴍᴘʀᴇss.\nsᴏ ʙᴇ ᴘᴀᴛɪᴇɴᴄᴇ ɴᴅ sᴇɴᴅ ᴠɪᴅᴇᴏs ᴏɴᴇ ʙʏ ᴏɴᴇ ᴀғᴛᴇʀ ᴄᴏᴍᴘʟᴇᴛɪɴɢ.\nᴅᴏɴᴛ sᴘᴀᴍ ʙᴏᴛ.\n\nᴊᴜsᴛ ғᴏʀᴡᴀʀᴅ ᴠɪᴅᴇᴏ ᴛᴏ ɢᴇᴛ ᴏᴘᴛɪᴏɴs"
    )


async def ihelp(event):
    await event.edit(
        "**🐠 ᴀ ǫᴜᴀʟɪᴛʏ ᴄᴏᴍᴘʀᴇssᴏʀʙᴏᴛ **\n\n✨ ᴛʜɪs ʙᴏᴛ ᴄᴏᴍᴘʀᴇss ᴠɪᴅᴇᴏs ᴡɪᴛʜ ɴᴇɢʟɪɢɪʙʟᴇ ǫᴜᴀʟɪᴛʏ ᴄʜᴀɴɢᴇ.\n✨ ɢᴇɴᴇʀᴀᴛᴇ sᴀᴍᴘʟᴇ ᴄᴏᴍᴘʀᴇssᴇᴅ ᴠɪᴅᴇᴏ\n✨ ᴇᴀsʏ ᴛᴏ ᴜsᴇ\n🎊 ᴅᴜᴇ ᴛᴏ ǫᴜᴀʟɪᴛʏ sᴇᴛᴛɪɴɢs ʙᴏᴛ ᴛᴀᴋᴇs ᴛɪᴍᴇ ᴛᴏ ᴄᴏᴍᴘʀᴇss. \nsᴏ ʙᴇ ᴘᴀᴛɪᴇɴᴄᴇ ɴᴅ sᴇɴᴅ ᴠɪᴅᴇᴏs ᴏɴᴇ ʙʏ ᴏɴᴇ ᴀғᴛᴇʀ ᴄᴏᴍᴘʟᴇᴛɪɴɢ.\nᴅᴏɴᴛ sᴘᴀᴍ ʙᴏᴛ\n\nᴊᴜsᴛ ғᴏʀᴡᴀʀᴅ ᴠɪᴅᴇᴏ ᴛᴏ ɢᴇᴛ ᴏᴘᴛɪᴏɴs",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.edit(
        f"ʜɪ `{ok.user.first_name}`\nᴛʜɪs ɪs ᴀ ᴄᴏᴍᴘʀᴇssᴏʀʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ᴇɴᴄᴏᴅᴇ ᴠɪᴅᴇᴏs.\nʀᴇᴅᴜᴄᴇ sɪᴢᴇ ᴏғ ᴠɪᴅᴇᴏs ᴡɪᴛʜ ɴᴇɢʟɪɢɪʙʟᴇ ǫᴜᴀʟɪᴛʏ ᴄʜᴀɴɢᴇ\nᴜ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ sᴀᴍᴘʟᴇs/sᴄʀᴇᴇɴsʜᴏᴛs ᴛᴏᴏ.",
        buttons=[
            [Button.inline("ʜᴇʟᴘ", data="ihelp")],
            [
                Button.url("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="github.com/xMalitha/CompressorXBot"),
                Button.url("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/xMalitha"),
            ],
        ],
    )


async def sencc(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "ᴄʜᴏᴏsᴇ ᴍᴏᴅᴇ",
        buttons=[
            [
                Button.inline("ᴅᴇғᴀᴜʟᴛ ᴄᴏᴍᴘʀᴇss", data=f"encc{key}"),
                Button.inline("ᴄᴜsᴛᴏᴍ ᴄᴏᴍᴘʀᴇss", data=f"ccom{key}"),
            ],
            [Button.inline("ʙᴀᴄᴋ", data=f"back{key}")],
        ],
    )


async def back(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "🐠  **ᴡʜᴀᴛ ᴛᴏ ᴅᴏ** 🐠",
        buttons=[
            [
                Button.inline("ɢᴇɴᴇʀᴀᴛᴇ sᴀᴍᴘʟᴇ", data=f"gsmpl{key}"),
                Button.inline("sᴄʀᴇᴇɴsʜᴏᴛs", data=f"sshot{key}"),
            ],
            [Button.inline("ᴄᴏᴍᴘʀᴇss", data=f"sencc{key}")],
        ],
    )


async def ccom(e):
    await e.edit("sᴇɴᴅ ᴜʀ ᴄᴜsᴛᴏᴍ ɴᴀᴍᴇ ғᴏʀ ᴛʜᴀᴛ ғɪʟᴇ")
    wah = e.pattern_match.group(1).decode("UTF-8")
    wh = decode(wah)
    out, dl, thum, dtime = wh.split(";")
    chat = e.sender_id
    async with e.client.conversation(chat) as cv:
        reply = cv.wait_event(events.NewMessage(from_users=chat))
        repl = await reply
        if "." in repl.text:
            q = repl.text.split(".")[-1]
            g = repl.text.replace(q, "mkv")
        else:
            g = repl.text + ".mkv"
        outt = f"encode/{chat}/{g}"
        x = await repl.reply(
            f"ᴄᴜsᴛᴏᴍ ғɪʟᴇ ɴᴀᴍᴇ : {g}\n\nsᴇɴᴅ ᴛʜᴜᴍʙɴᴀɪʟ ᴘɪᴄᴛᴜʀᴇ ғᴏʀ ɪᴛ."
        )
        replyy = cv.wait_event(events.NewMessage(from_users=chat))
        rep = await replyy
        if rep.media:
            tb = await e.client.download_media(rep.media, f"thumb/{chat}.jpg")
        elif rep.text and not (rep.text).startswith("/"):
            url = rep.text
            os.system(f"wget {url}")
            tb = url.replace("https://telegra.ph/file/", "")
        else:
            tb = thum
        omk = await rep.reply(f" ᴛʜᴜᴍʙɴᴀɪʟ  {tb} sᴇᴛᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ")
        hehe = f"{outt};{dl};{tb};{dtime}"
        key = code(hehe)
        await customenc(omk, key)
