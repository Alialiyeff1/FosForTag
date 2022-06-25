import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)


anlik_calisan = []

tekli_calisan = []



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**🌀Rahid_Tag_Bot**\n ilə qrupunuzdakı bütün üzvləri tag edə bilərəm \nƏmrlər üçün =======> /help yazın**",
                    buttons=(
                   
		      [Button.url('Məni qrupa əlavə et ➕', 'https://t.me/Rahid_Tag_Bot?startgroup=a')],
                      [Button.url('Support🛠', 'https://t.me/Rahid_Support')],
                      [Button.url('Rəsmi Kanal📣', 'https://t.me/Rahid_44')],
		      [Button.url('İnkişaf etdirici👨🏻‍💻', 'https://t.me/yalvargelim')],
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**🌀 Rahid_Tag_Bot Əmrləri**\n\n**/tag - 5-li tag edər**\n\n**/etag - Emoji ilə tag edər**\n\n**/tektag - Tək-tək tag edər**\n\n**/admins - Adminləri tək-tək tag edər**\n\n**/start - Botu başladır**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('Məni qrupa əlavə et ➕', 'https://t.me/Rahid_Tag_Bot?startgroup=a')],
                      [Button.url('Support👨‍💻', 'https://t.me/Rahid_Support')],
                      [Button.url('Rəsmi Kanal🔖', 'https://t.me/Rahid_44')],
		      [Button.url('İnkişaf etdirici🧑‍🔧', 'https://t.me/yalvargelim')],
                    ),
                    link_preview=False
                   )
	
@client.on(events.NewMessage(pattern="^/reklam$"))
async def help(event):
  helptext = "**Çox funksiyalı tag botunu tapmağa çalışan qrup sahibləri @Rahid_Tag_Bot Sizə Görə:\n\n📌 5-li tag\n📌 Emoji tag\n📌 Təkli tag\n📌 Yalnız adminləri tag etmək\n📌\n\n Belə çox funksiyalı @Rahid_Tag_Bot-u Qrupunuza əlavə edib bota idarəçilik verərək asanlıqla tag prosesi başlada bilərsiniz.**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('Botu qrupa əlavə et ➕', 'https://t.me/Rahid_Tag_Bot?startgroup=a')],
                    ),
                    link_preview=False
                   )
	
	

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar və kanallar üçün etibarlıdır.❗**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmri sadəcə qrup adminləri istifadə edə bilər〽️**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Keçmiş mesajlar üçün tag edə bilmirəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Tag etmək üçün səbəb yazın❗️")
  else:
    return await event.respond("**Tag başlamaq üçün səbəb yazın...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tag əməliyyatı uğurla dayandırıldı ❌**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Əməliyyat uğurla dayandırıldı\n\n**Burda sizin reklamınız ola bilər @Rahid_44**❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar və kanallar üçün etibarlıdır.❗️**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmri sadəcə qrup adminləri istifadə edə bilər〽️**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Əvvəlki mesajlara cavab verməyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Başlamaq üçün səbəb yazın❗️")
  else:
    return await event.respond("Əməliyyata başlamaq üçün səbəb yazın")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Əməliyyat uğurla dayandırıldı\n\n**Burda sizin reklamınız ola bilər @Rahid_44**❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Proses uğurla dayandırıldı ❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar və kanallar üçün etibarlıdır.❗️**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız adminlər istifadə edə bilər〽**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki mesajı tag edə bilmirəm*")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Başlamaq üçün səbəb yazın❗️")
  else:
    return await event.respond("**Əməliyyata başlamağın səbəbini yazın...**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**👤 - [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Əməliyyat uğurla dayandırıldı\n\n**Burda sizin reklamınız ola bilər @Rahid_44**❌****")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👤 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("Əməliyyat uğurla dayandırıldı\n\n**Burda sizin reklamınız ola bilər @Rahid_44**❌**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	


@client.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def mentionall(tagadmin):

	if tagadmin.pattern_match.group(1):
		seasons = tagadmin.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tagadmin.get_input_chat()
	a_=0
	await tagadmin.delete()
	async for i in client.iter_participants(chat, filter=cp):
		if a_ == 500:
			break
		a_+=5
		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(0.5)


print(">> Bot əla işləyir 🚀 Sual və təklif üçün @yalvargelim yaza bilərsiniz <<")
client.run_until_disconnected()
