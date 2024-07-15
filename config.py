import os
import logging

api_id = int(os.environ.get("API_ID", "23138248"))
api_hash = os.environ.get("API_HASH", "fb765fe307cf28e295da71ac2c3d17f2")
bot_token = os.environ.get("BOT_TOKEN", "7421669727:AAFPbb3vKVU9elO0EcqMC5ecL_V-aE1k7hU")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://muhamadfaiz:muhamadfaiz@cluster0.mpwspud.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "telegram")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001953908892"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001959200512"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1002229550163"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "6350981043"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "2"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "25"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#kowkwk #nyetsa #atgirl #atboy #atask #atrandom #atmutualan #atcurhat").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph/file/b2f62b0642bf0fd5849a8.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph/file/c9d103073f89b0568e38f.jpg")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "BOT TIDAK BISA DI GUNAKAN SILAHKAN JOIN KE CHANNEL ATAU GRUP DI BAWAH")
start_msg = os.environ.get("START_MSG", """Halo {mention} 🔥\n\n<b>MENFESS RESFAMS</b> adalah Bot Auto Post, Semua Pesan Yang Kamu Kirim Akan Masuk Ke Channel @menfes_resfams. Silahkan kirim pesan anda menggunakan hastag dibawah ini:

#atboy (Untuk Identitas Laki-Laki)
#atgirl (Untuk Identitas perempuan)
#atrandom (Untuk hal random)
#atmutualan (Untuk mutualan)
#atask (Untuk membagikan hal bodoh)
#atcurhat (Untuk curhat masalah)
""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, Pesan Mu Gagal Terkirim Silahkan Gunakan Hashtag Berikut:

#atboy (Untuk Identitas Laki-Laki)
#atgirl (Untuk Identitas perempuan)
#atrandom (Untuk hal random)
#atmutualan (Untuk mutualan)
#atask (Untuk membagikan hal bodoh)
#atcurhat (Untuk curhat masalah)
""")
