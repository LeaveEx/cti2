import os
import logging

api_id = int(os.environ.get("API_ID", "WAJIB DIISI"))
api_hash = os.environ.get("API_HASH", "WAJIB DIISI")
bot_token = os.environ.get("BOT_TOKEN", "WAJIB DIISI")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://username:password@cluster0.d9fwl.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "telegram")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "WAJIB DIISI"))
channel_2 = int(os.environ.get("CHANNEL_2", "WAJIB DIISI"))
channel_log = int(os.environ.get("CHANNEL_LOG", "WAJIB DIISI"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "5069042518"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "5"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#Girl #Boy #Ask #Find #Spill #Story").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph/file/b2f62b0642bf0fd5849a8.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph/file/c9d103073f89b0568e38f.jpg")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", "Hai {fullname} 🌱\n\nIni adalah bot menfess, semua pesan yang kamu kirim akan masuk ke channel secara anonymous. ketik /help")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, Silahkan ketik /help untuk menggunakan bot ini
""")
