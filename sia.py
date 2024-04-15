import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from youtube_search import YoutubeSearch
import youtube_dl
from instaloader import Instaloader, Post, TwoFactorAuthRequiredException

# Bot token'ını buraya ekleyin
BOT_TOKEN = "6548800964:AAFhA1eIs335BFHn5KAiRij-vBjVb7mxEHI"

# API bilgilerini ve diğer gizli bilgileri config dosyasından veya ortam değişkenlerinden alın
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
username_ig = os.getenv("INSTA_USERNAME")
password_ig = os.getenv("INSTA_PASSWORD")

# Telegram istemcisini başlat
app = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=BOT_TOKEN
)

# Botun başlangıç komutunu işleyen fonksiyon
@app.on_message(filters.command('start'))
async def start_msg(client, message):
    name = message.from_user.first_name
    await message.reply(
        f"Merhaba {name}! Ben Siaah. Nasıl yardımcı olabilirim?\n\n"
        "Örnek komutlar:\n"
        "/play Şarkı Adı - YouTube'dan şarkı indir\n"
        "YouTube veya Instagram linki göndererek medya indirme"
    )

# YouTube'dan şarkı indirme komutunu işleyen fonksiyon
@app.on_message(filters.command('play'))
async def play_song(client, message):
    query = " ".join(message.command[1:])
    await message.reply_chat_action("typing")  # Yazıyor gibi göster
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        if results:
            video_url = f"https://youtube.com{results[0]['url_suffix']}"
            await message.reply(f"İndirme bağlantısı: {video_url}")
        else:
            await message.reply("Şarkı bulunamadı.")
    except Exception as e:
        await message.reply(f"Hata: {str(e)}")

# Instagram reel indirme komutunu işleyen fonksiyon
@app.on_message(filters.regex(r"(?i)^(https?\:\/\/)?(www\.instagram\.com)\/reel\/.+$"))
async def download_instagram_reel(client, message):
    reel_link = message.text
    # İndirme işlemlerini burada gerçekleştirin

# Instagram post indirme komutunu işleyen fonksiyon
@app.on_message(filters.regex(r"(?i)^(https?\:\/\/)?(www\.instagram\.com)\/p\/.+$"))
async def download_instagram_post(client, message):
    post_link = message.text
    # İndirme işlemlerini burada gerçekleştirin

# Botu çalıştır
app.run()
