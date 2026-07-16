"""
Data deskriptif untuk setiap kelas penyakit daun tomat:
nama tampilan, ikon, tipe (sehat/sakit), deskripsi, dan rekomendasi penanganan.
"""

CLASS_INFO = {
    "Tomato___Bacterial_spot": {
        "nama": "Bacterial Spot (Bercak Bakteri)",
        "icon": "🦠",
        "tipe": "sakit",
        "deskripsi": "Disebabkan oleh bakteri Xanthomonas. Muncul bercak kecil "
                     "kehitaman/kecoklatan dengan tepi kekuningan pada daun, "
                     "batang, dan buah.",
        "penanganan": [
            "Gunakan benih/bibit bersertifikat bebas patogen.",
            "Hindari penyiraman dari atas (overhead) agar daun tidak lembab lama.",
            "Aplikasikan bakterisida berbahan tembaga sesuai anjuran.",
            "Buang dan musnahkan bagian tanaman yang terinfeksi berat.",
        ],
    },
    "Tomato___Early_blight": {
        "nama": "Early Blight (Bercak Daun Awal)",
        "icon": "🍂",
        "tipe": "sakit",
        "deskripsi": "Disebabkan jamur Alternaria solani. Bercak coklat "
                     "melingkar menyerupai cincin target (target spot) pada "
                     "daun tua terlebih dahulu.",
        "penanganan": [
            "Rotasi tanaman, hindari menanam tomat di lahan yang sama berturut-turut.",
            "Pangkas daun bagian bawah yang terinfeksi.",
            "Semprot fungisida berbahan aktif klorotalonil atau mankozeb.",
            "Jaga jarak tanam agar sirkulasi udara baik.",
        ],
    },
    "Tomato___Late_blight": {
        "nama": "Late Blight (Busuk Daun)",
        "icon": "💧",
        "tipe": "sakit",
        "deskripsi": "Disebabkan oleh Phytophthora infestans, penyakit paling "
                     "merusak pada tomat. Bercak coklat kehitaman basah yang "
                     "menyebar cepat, terutama saat cuaca lembap.",
        "penanganan": [
            "Segera cabut dan musnahkan tanaman yang terinfeksi berat.",
            "Gunakan fungisida sistemik (mis. berbahan metalaksil).",
            "Hindari kelembapan berlebih dan genangan air di sekitar tanaman.",
            "Tanam varietas tomat yang tahan late blight bila memungkinkan.",
        ],
    },
    "Tomato___Leaf_Mold": {
        "nama": "Leaf Mold (Jamur Daun)",
        "icon": "🌫️",
        "tipe": "sakit",
        "deskripsi": "Disebabkan jamur Passalora fulva, umum di rumah kaca. "
                     "Bercak kuning di permukaan atas daun dengan lapisan "
                     "beludru hijau-zaitun di bagian bawah daun.",
        "penanganan": [
            "Kurangi kelembapan dengan ventilasi/sirkulasi udara yang baik.",
            "Hindari kepadatan tanaman berlebih.",
            "Gunakan fungisida yang sesuai bila serangan meluas.",
            "Siram di pagi hari agar daun cepat kering.",
        ],
    },
    "Tomato___Septoria_leaf_spot": {
        "nama": "Septoria Leaf Spot (Bercak Septoria)",
        "icon": "🔘",
        "tipe": "sakit",
        "deskripsi": "Disebabkan jamur Septoria lycopersici. Bercak kecil "
                     "bulat berwarna abu-abu dengan tepi gelap, biasanya "
                     "muncul pertama di daun bawah.",
        "penanganan": [
            "Buang daun bawah yang terinfeksi sejak dini.",
            "Hindari menyiram langsung ke daun.",
            "Aplikasikan fungisida protektif secara berkala.",
            "Bersihkan sisa tanaman sakit dari lahan setelah panen.",
        ],
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "nama": "Spider Mites (Tungau Laba-laba)",
        "icon": "🕷️",
        "tipe": "sakit",
        "deskripsi": "Serangan hama tungau Tetranychus urticae. Daun tampak "
                     "berbintik kuning pucat (stippling) disertai jaring "
                     "halus di bawah daun.",
        "penanganan": [
            "Semprot air bertekanan untuk merontokkan tungau.",
            "Gunakan akarisida/miticide bila serangan parah.",
            "Manfaatkan predator alami seperti kumbang Phytoseiulus.",
            "Jaga kelembapan udara karena tungau menyukai kondisi kering.",
        ],
    },
    "Tomato___Target_Spot": {
        "nama": "Target Spot (Bercak Target)",
        "icon": "🎯",
        "tipe": "sakit",
        "deskripsi": "Disebabkan jamur Corynespora cassiicola. Bercak coklat "
                     "dengan pola cincin konsentris mirip papan target, dapat "
                     "menyerang daun, batang, dan buah.",
        "penanganan": [
            "Rotasi tanaman dan sanitasi lahan secara rutin.",
            "Kurangi kelembapan kanopi dengan pemangkasan.",
            "Aplikasikan fungisida berbahan aktif azoksistrobin/klorotalonil.",
            "Hindari irigasi dari atas tanaman.",
        ],
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "nama": "Yellow Leaf Curl Virus (Virus Keriting Kuning)",
        "icon": "🦟",
        "tipe": "sakit",
        "deskripsi": "Disebabkan virus TYLCV yang ditularkan oleh kutu kebul "
                     "(whitefly). Daun menguning, mengeriting ke atas, dan "
                     "pertumbuhan tanaman terhambat.",
        "penanganan": [
            "Kendalikan populasi kutu kebul (whitefly) dengan insektisida/perangkap kuning.",
            "Gunakan mulsa plastik reflektif untuk mengusir whitefly.",
            "Cabut dan musnahkan tanaman yang terinfeksi agar tidak menular.",
            "Tanam varietas tomat tahan TYLCV jika tersedia.",
        ],
    },
    "Tomato___Tomato_mosaic_virus": {
        "nama": "Mosaic Virus (Virus Mosaik)",
        "icon": "🧩",
        "tipe": "sakit",
        "deskripsi": "Disebabkan Tobacco/Tomato Mosaic Virus. Daun menunjukkan "
                     "pola belang hijau muda-tua (mosaik), daun mengerut dan "
                     "pertumbuhan terhambat.",
        "penanganan": [
            "Cuci tangan dan sterilkan alat sebelum menyentuh tanaman lain.",
            "Cabut tanaman yang terinfeksi untuk mencegah penyebaran.",
            "Hindari merokok di sekitar tanaman (virus dapat menular lewat tembakau).",
            "Gunakan benih bersertifikat bebas virus.",
        ],
    },
    "Tomato___healthy": {
        "nama": "Sehat",
        "icon": "✅",
        "tipe": "sehat",
        "deskripsi": "Daun tomat tidak menunjukkan gejala penyakit maupun "
                     "serangan hama. Kondisi tanaman baik.",
        "penanganan": [
            "Pertahankan penyiraman dan pemupukan yang teratur.",
            "Lakukan pemantauan rutin untuk deteksi dini penyakit.",
            "Jaga kebersihan lahan dari gulma dan sisa tanaman sakit.",
        ],
    },
}