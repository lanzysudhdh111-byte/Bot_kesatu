import telebot

# 🔑 DATA BOT UTAMA
TOKEN_UTAMA = "8626401164:AAGwVYpcgd0Hacr1_HNoPzIqQa-tig2Vgkc"
# 🔑 TOKEN & ID BOT KONFIRMASI (SC KE-2)
TOKEN_KONFIRMASI = "ISI_TOKEN_SC_KEDUA_DI_SINI"
ID_ADMIN_KONFIRMASI = "ISI_ID_TELEGRAM_KAMU_DI_SINI"  # ID kamu sendiri

bot_utama = telebot.TeleBot(TOKEN_UTAMA)
bot_kedua = telebot.TeleBot(TOKEN_KONFIRMASI)

# ✅ /start
@bot_utama.message_handler(commands=['start'])
def start(msg):
    nama = msg.from_user.first_name
    bot_utama.send_message(msg.chat.id, f"""
🎉 SELAMAT DATANG, {nama}! 🎉
Senang kamu bergabung! Semoga betah ya.

💸 TUTORIAL BY LANZ💸
🤖 BOT: @Lala729
    """)

# ✅ /harga_lutbotz
@bot_utama.message_handler(commands=['harga_lutbotz'])
def harga1(msg):
    bot_utama.send_message(msg.chat.id, """
HARGA APK LUTBOTZ ✅
https://whatsapp.com/channel/0029VbCNa8EISTkC3UQnwe0f/683
INI GACOR NIH
    """)

# ✅ /harga_ppl
@bot_utama.message_handler(commands=['harga_ppl'])
def harga2(msg):
    bot_utama.send_message(msg.chat.id, """
HARGA LUTBOZT
https://whatsapp.com/channel/0029VbCNa8EISTkC3UQnwe0f/757
    """)

# ✅ /qr
@bot_utama.message_handler(commands=['qr'])
def kirim_qr(msg):
    bot_utama.send_message(msg.chat.id, """
📸 QRIS AL PAYMENT⬇️
https://drive.google.com/file/d/1RKBXR407s3sT2CUR1oI-fC45vsSn9dev/view?usp=drivesdk
SS BUKTI TF YA
NAMA QRIS: LANZ RAR
    """)

# ✅ /ig
@bot_utama.message_handler(commands=['ig'])
def ig(msg):
    bot_utama.send_message(msg.chat.id, """
📸 HUBUNGI VIA IG: @sukmin
Jika hubungi IG: WAJIB KONFIRMASI dulu.
Nanti saya kirim aplikasinya lewat sini.
    """)

# ✅ /suk_min → LANGSUNG KIRIM KE SC KE-2
@bot_utama.message_handler(commands=['suk_min'])
def sukmin(msg):
    pengirim = f"Dari: {msg.from_user.first_name} | ID: {msg.from_user.id}"
    pesan = "📩 ADA YANG KIRIM /suk_min! Mohon cek bukti transfernya."
    # Kirim notif ke SC ke-2
    bot_kedua.send_message(ID_ADMIN_KONFIRMASI, f"{pesan}\n{pengirim}")
    # Balas ke pembeli
    bot_utama.send_message(msg.chat.id, """
📌 BUKTI SEDANG DIPERIKSA
Terima kasih! Pesan & bukti kamu sudah saya terima.
Segera saya konfirmasi, nanti aplikasi langsung dikirim.
Mohon tunggu sebentar ya!
    """)

# ✅ KIRIM FOTO BUKTI TF LANGSUNG KE SC KE-2
@bot_utama.message_handler(content_types=['photo'])
def terima_foto(msg):
    pengirim = f"Dari: {msg.from_user.first_name} | ID: {msg.from_user.id}"
    caption = msg.caption if msg.caption else "Tidak ada keterangan"
    # Teruskan foto ke SC ke-2
    bot_kedua.send_photo(
        ID_ADMIN_KONFIRMASI,
        msg.photo[-1].file_id,
        caption=f"📸 BUKTI TRANSFER DITERIMA!\n{pengirim}\nKeterangan: {caption}"
    )
    bot_utama.send_message(msg.chat.id, "✅ Foto bukti sudah diterima & dikirim ke saya untuk dicek. Tunggu konfirmasi ya!")

# ✅ Sambutan anggota baru
@bot_utama.message_handler(content_types=['new_chat_members'])
def anggota_baru(msg):
    for orang in msg.new_chat_members:
        bot_utama.send_message(msg.chat.id, f"👋 HALO {orang.first_name}, SELAMAT DATANG! 🎉")

print("✅ BOT UTAMA: Pesan & Foto otomatis dikirim ke SC KE-2!")
bot_utama.polling()
