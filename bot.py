import os, logging, asyncio
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

emj = ['😇','🥰','😎','🤩','😍','👾','🤡','🥳','😻','😼','😽','💋','👸','🤴','🎅🏻','🤶','🧞‍♀️','🧞','🧞‍♂️','🧜‍♀️','🧜','🧚‍♀️','🧚','👑','💍','🕶','🐶','🐱','🐭','🐹','🐰','🦊','🐻','🐼','🐨','🐯','🦁','🐮','🐷','🐽','🐸','🐵','🙈','🙉','🙊','🐒','🐣','🐥','🦅','🐝','🦋','🐞','💐','🌹','🥀','🌺','🌸','🌼','🌻','⭐️','🌟','✨','⚡️','🔥','🌈','☃️','🍫','💅','🐺','🍫','🍕','☕','🧸','🦅','👩‍🦰','🎮','☄️','🌙','🦕','👨🏻‍✈️','🥶','🍿','👀','💀','💟','♥️','💘','💝','💗','💙','💛','🖤','🤑','⚡','😈','🤡','🎊','🔥','😼','💤','✊','👩‍🎨','🧕','🌼','💐','🌹','🥀','🌷','🌺','🌸','🏵️','🌻','🍂','🍁','🌾','🌱','🌿','🍃','☘️','🍀','🌵','🌴','🌳','🌲','🏞️','🌪️','☃️','⛄','❄️','🏔️','🌋','🙋','🤶','👩‍💼','🧓','🧔','💃','🕺','👩‍🦰','🪐','🦄','🐢','🐁','🐤','🐣','🐥','🦉','🐓','🕊️','🦢','🦩','🦈','🐬','🐋','🐳','🐟','🐠','🦚','🐡','🦐','🦞','🦀','🦑','🐙','🦂','🕷️','🕸️','🐜','🦗','🦟','🐝','🐞','🐾','🍓','🍒','🍎','🍉','🍊','🥭','🍍','🍋','🍇','🥝','🍐','🥥','🌶️','🍄','🍔','🧆','🥙','🦞','🍧','🍨','🍦','🥧','🍰','🍮','🎂','🧁','🍭','🍬','🍩','🍺','🍻','🥂','🍾','🍷']

@client.on(events.NewMessage(pattern='^(?i)/durdur'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**@ZionTaggerBot** Grubunuzdakı Üyeleri Etiketler \n ==========> /help \n Basarak Yardım Menüsunu Göre Bilirsiz\n\n@ZionBots",
                    buttons=(
                      [Button.url('➕ Beni Gruba Ekle ➕', 'https://t.me/ziontaggerbot?startgroup=a'),
                      Button.url('👨‍💻Creator👨‍💻', 'https://t.me/ZionBey'),
                      ],
                      [
                      Button.url('🔖Resmi Kanal', 'https://t.me/ZionBots')]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**@ZionTaggerBot Yardım Menüsu \n \n Komutlar : /all Komutu ile Grubunuzdakı üyeleri basit bi şekilde çağıra bilirsiz\n\n /durdur Komutu ile üye Etiketleme işlemini durdura bilirsjz"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('➕ Beni Gruba Ekle ➕', 'https://t.me/ziontaggerbot?startgroup=a'),
                      Button.url('👨‍💻Creator👨‍💻', 'https://t.me/ZionBey'),
                      ],
                      [
                      Button.url('🔖Resmi Kanal', 'https://t.me/ZionBots')]
                    ),
                    link_preview=False
                   )


@client.on(events.NewMessage(pattern="^/all ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Etiketleme işlemini Sadace Yöneticiler Yapa bilir!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__Etiketleme işlemini Sadace Yöneticiler Yapa bilir!__") 
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Önceki mesajlar için Kullanıcı Çağıramam🌀! (Gruba Ekledikten Sonra Yazılan Mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Bana bir argüman ver!__")
  else:
    return await event.respond("__Bir mesaja yanıt verin ve ya Mesaj Yazın🌀__")
    
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiket işlemi başarıyla durduruldu 🌀")
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
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiket işlemi başarıyla durduruldu ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
#Emoji Yakında
@client.on(events.NewMessage(pattern="^/emoji ?(.*)"))
async def etag(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanılabilir.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__Yalnızca yöneticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajlar için üyelerden bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Bana bir argüman ver!__")
  else:
    return await event.respond("__Bir mesajı yanıtlayın veya başkalarından bahsetmem için bana bir metin verin!__")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emj)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("İşlem Başarılı Bir Şekilde Durduruldu ❌")
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
      usrtxt += f"[{random.choice(emj)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("İşlem Başarılı Bir Şekilde Durduruldu ❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


print(">> Frozen Tagger BoT Çalışıyor 🚀 @FrozenBots Gelerek Yeniliklerden Haberdar Ola bilirsiz<<")
client.run_until_disconnected()
