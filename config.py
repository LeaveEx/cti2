import os
import logging

api_id = int(os.environ.get("API_ID", "2857053"))
api_hash = os.environ.get("API_HASH", "4a01e3596661ba4bf609d15c1f9e129b")
bot_token = os.environ.get("BOT_TOKEN", "6057365695:AAGLG5qu7Xa3QgrDOO91ARkZzFRbxaH6gEE")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://muhamadfaiz:muhamadfaiz@cluster0.mpwspud.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "telegram")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001439465967"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001215547362"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1002003868172"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "2100705176"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "2"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "25"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#kowkwk #nyetsa #ctngirl #ctnboy #ctnask #ctnrandom #ctnmutualan #ctncurhat").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph/file/b2f62b0642bf0fd5849a8.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph/file/c9d103073f89b0568e38f.jpg")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", """Halo {mention} ⭐\n\n<b>CHANNEL CTN</b> adalah Bot Auto Post, Semua Pesan Yang Kamu Kirim Akan Masuk Ke Channel @SIARANCTN. Silahkan kirim pesan anda menggunakan hastag dibawah ini:

#ctnboy (Untuk Identitas Laki-Laki)
#ctngirl (Untuk Identitas perempuan)
#ctnrandom (Untuk hal random)
#ctnmutualan (Untuk mutualan)
#ctnask (Untuk membagikan hal bodoh)
#ctncurhat (Untuk curhat masalah)
""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, Pesan Mu Gagal Terkirim Silahkan Gunakan Hashtag Berikut:

#ctnboy (Untuk Identitas Laki-Laki)
#ctngirl (Untuk Identitas perempuan)
#ctnrandom (Untuk hal random)
#ctnmutualan (Untuk mutualan)
#ctnask (Untuk membagikan hal bodoh)
#ctncurhat (Untuk curhat masalah)
""")
