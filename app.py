"""
=====================================================================
 TOMATO LEAF DOCTOR — Aplikasi Deteksi Penyakit Daun Tomat
 Berbasis Transfer Learning MobileNetV2 (PyTorch) + Streamlit
=====================================================================
Cara menjalankan:
    streamlit run app.py

Struktur project:
    app.py              -> UI utama (file ini)
    config.py           -> konstanta & konfigurasi model
    class_info.py        -> data deskripsi & penanganan tiap kelas
    model_utils.py       -> load model, transform gambar, fungsi prediksi
    assets/style.css     -> semua styling (CSS)
    .streamlit/config.toml -> tema Streamlit (dipaksa light agar konsisten)

Pastikan file model hasil training sudah ada di:
    checkpoints/mobilenet_v2_tomato_leaf_disease_final.pt
(sesuaikan MODEL_PATH di config.py jika nama/lokasi file berbeda)
=====================================================================
"""

import io
import time
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

from class_info import CLASS_INFO
from config import CLASS_NAMES, IMG_SIZE, MODEL_PATH
from model_utils import load_model, predict

# =====================================================================
# 1. KONFIGURASI HALAMAN
# =====================================================================
st.set_page_config(
    page_title="Tomato Leaf Doctor",
    page_icon="🍅",
    layout="wide",
    initial_sidebar_state="expanded",
)


def load_css(path: str) -> None:
    """Membaca file CSS eksternal dan menyuntikkannya ke halaman."""
    css_path = Path(path)
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ File CSS tidak ditemukan di `{path}`. Tampilan mungkin tidak sesuai desain.")


load_css("assets/style.css")

# =====================================================================
# 2. SIDEBAR
# =====================================================================
with st.sidebar:
    st.markdown("## 🍅 Tomato Leaf Doctor")
    st.markdown(
        "Aplikasi deteksi penyakit daun tomat otomatis menggunakan "
        "**Transfer Learning MobileNetV2**."
    )
    st.markdown("---")
    st.markdown("### ⚙️ Tentang Model")
    st.markdown(
        f"""
- **Arsitektur:** MobileNetV2 (Transfer Learning)
- **Framework:** PyTorch
- **Ukuran input:** {IMG_SIZE}×{IMG_SIZE} px
- **Jumlah kelas:** {len(CLASS_NAMES)} kelas
- **Strategi training:** Fine-tuning 2 fase (head-only → partial backbone)
        """
    )
    st.markdown("---")
    st.markdown("### 📋 Cara Pakai")
    st.markdown(
        """
1. Tarik & lepas (drag and drop), unggah, atau ambil foto daun tomat.
2. Tunggu proses analisis model.
3. Lihat hasil prediksi & rekomendasi penanganan.
        """
    )
    st.markdown("---")
    st.caption("⚠️ Hasil prediksi bersifat pendukung keputusan, bukan pengganti "
                "diagnosis ahli pertanian/pertanian profesional.")

# =====================================================================
# 3. HERO HEADER
# =====================================================================
st.markdown(
    """
    <div class="hero">
        <span class="hero-emoji">🍅</span>
        <h1>🍅 Tomato Leaf Doctor</h1>
        <p>Tarik & lepas foto daun tomat ke kotak di bawah, dan biarkan AI
        mendeteksi penyakit secara instan beserta rekomendasi penanganannya.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# =====================================================================
# 4. UPLOAD & INFERENSI
# =====================================================================
col_upload, col_result = st.columns([1, 1], gap="large")

with col_upload:
    st.markdown('<div class="section-label">📤 Unggah Gambar Daun Tomat</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="uw-sub">Tarik &amp; lepas (drag &amp; drop) gambar ke kotak di bawah, '
        'atau klik untuk memilih file dari perangkat kamu.</div>',
        unsafe_allow_html=True,
    )

    tab_upload, tab_camera = st.tabs(["🖼️ Unggah / Drag & Drop", "📷 Kamera"])

    with tab_upload:
        uploaded_file = st.file_uploader(
            "Tarik & lepas gambar di sini, atau klik untuk memilih file",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed",
        )

    with tab_camera:
        camera_file = st.camera_input("Ambil foto daun tomat", label_visibility="collapsed")

    image_source = uploaded_file if uploaded_file is not None else camera_file

    if image_source is not None:
        image = Image.open(io.BytesIO(image_source.getvalue()))
        st.image(image, caption="Gambar yang akan dianalisis", use_column_width=True)

with col_result:
    if image_source is None:
        st.markdown('<div class="section-label">ℹ️ Menunggu Gambar</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="card info-card">
                Silakan unggah atau tarik &amp; lepas foto daun tomat di panel sebelah kiri
                untuk memulai analisis. Pastikan foto fokus, pencahayaan cukup, dan daun
                terlihat jelas untuk hasil terbaik.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="card tips-card">
                <b>💡 Tips mengambil foto yang baik</b>
                <ul>
                    <li>Ambil foto dari jarak dekat dengan daun mengisi sebagian besar frame.</li>
                    <li>Gunakan pencahayaan alami/merata, hindari bayangan tajam.</li>
                    <li>Pastikan gambar tidak buram (fokus jelas).</li>
                    <li>Latar belakang polos akan membantu akurasi model.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        probs = None
    else:
        try:
            with st.spinner("🔬 Menganalisis gambar dengan model MobileNetV2..."):
                model, device = load_model()
                t0 = time.time()
                probs = predict(image, model, device)
                elapsed = time.time() - t0

            pred_idx = int(np.argmax(probs))
            pred_class = CLASS_NAMES[pred_idx]
            pred_conf = float(probs[pred_idx])
            info = CLASS_INFO[pred_class]

            card_class = "result-card-sehat" if info["tipe"] == "sehat" else "result-card-sakit"
            badge_class = "badge-sehat" if info["tipe"] == "sehat" else "badge-sakit"
            badge_text = "SEHAT" if info["tipe"] == "sehat" else "TERDETEKSI PENYAKIT"

            st.markdown('<div class="section-label">🧪 Hasil Diagnosis</div>', unsafe_allow_html=True)
            st.markdown(
                f"""
                <div class="{card_class}">
                    <span class="badge {badge_class}">{badge_text}</span>
                    <div class="result-title">{info['icon']} {info['nama']}</div>
                    <div class="result-conf">Tingkat keyakinan model: <b>{pred_conf*100:.2f}%</b>
                    &nbsp;•&nbsp; waktu inferensi {elapsed*1000:.0f} ms</div>
                    <p style="margin-top:0.6rem; margin-bottom:0;">{info['deskripsi']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                f"""
                <div class="card">
                    <b>🩺 Rekomendasi Penanganan</b>
                    <ul class="steps">{''.join(f'<li>{s}</li>' for s in info['penanganan'])}</ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

        except FileNotFoundError:
            probs = None
            st.error(
                f"❌ File model tidak ditemukan di `{MODEL_PATH}`.\n\n"
                "Pastikan file checkpoint hasil training (`.pt`) sudah diletakkan "
                "di folder `checkpoints/` sesuai dengan path pada notebook, atau "
                "sesuaikan variabel `MODEL_PATH` di `config.py`."
            )
        except Exception as e:
            probs = None
            st.error(f"Terjadi kesalahan saat memproses gambar: {e}")

# =====================================================================
# 5. DETAIL PROBABILITAS SEMUA KELAS
# =====================================================================
if image_source is not None and probs is not None:
    st.markdown("---")
    st.markdown('<div class="section-label">📊 Probabilitas Seluruh Kelas</div>', unsafe_allow_html=True)

    df = pd.DataFrame(
        {
            "Kelas": [CLASS_INFO[c]["nama"] for c in CLASS_NAMES],
            "Probabilitas": probs,
        }
    ).sort_values("Probabilitas", ascending=False)

    chart_col, table_col = st.columns([1.4, 1], gap="large")

    with chart_col:
        st.bar_chart(
            df.set_index("Kelas")["Probabilitas"],
            color="#2e7d32",
            height=380,
        )

    with table_col:
        df_display = df.copy()
        df_display["Probabilitas"] = (df_display["Probabilitas"] * 100).round(2).astype(str) + " %"
        st.dataframe(df_display, hide_index=True, use_container_width=True, height=380)

