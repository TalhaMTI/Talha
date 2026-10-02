from datetime import datetime
import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Talha Işıkcı | Kişisel Üs",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- GİRİŞ / ŞİFRE KONTROLÜ ---
# Doğum tarihin olan şifre: 20.02.2008
if "giris_yapildi" not in st.session_state:
    st.session_state.giris_yapildi = False

if not st.session_state.giris_yapildi:
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #09090b 0%, #18181b 100%);
            color: #f4f4f5;
        }
        .login-box {
            background: rgba(24, 24, 27, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            max-width: 400px;
            margin: 100px auto;
            box-shadow: 0 20px 40px rgba(0,0,0,0.8);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            '<div class="login-box">', unsafe_allow_html=True
        )
        st.markdown("### 🔒 Yetkili Girişi")
        st.markdown(
            "<p style='color: #a1a1aa; font-size: 13px;'>Bu alan sadece Talha Işıkcı'ya özeldir.</p>",
            unsafe_allow_html=True,
        )

        sifre_giris = st.text_input(
            "Güvenlik Anahtarı", type="password", placeholder="GG.AA.YYYY"
        )

        if st.button(
            "Sisteme Giriş Yap", use_container_width=True, type="primary"
        ):
            if sifre_giris == "20.02.2008":
                st.session_state.giris_yapildi = True
                st.rerun()
            else:
                st.error("Geçersiz Anahtar!")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()


# --- ANA PANEL (GİRİŞ BAŞARILI) ---
st.markdown(
    """
    <style>
    .stApp {
        background: #09090b;
        color: #f4f4f5;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .hero-card {
        background: linear-gradient(135deg, #18181b 0%, #27272a 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 30px;
        border-radius: 16px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .stat-card {
        background: #18181b;
        border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Üst Bilgi / Profil Özeti
st.markdown(
    """
    <div class="hero-card">
        <h1 style='margin:0; color: #f4f4f5; font-size: 28px;'>Hoş geldin, Talha Işıkcı 👑</h1>
        <p style='margin: 5px 0 0 0; color: #a1a1aa; font-size: 15px;'>Konya | Dijital Komuta Merkezi & Kişisel Ekosistem</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Sekmeler (İlgi Alanlarına Göre)
tab1, tab2, tab3, tab4 = st.tabs(
    ["🚗 Otomotiv & Garaj", "💻 Yazılım & Donanım", "🖨️ 3D Tasarım", "✨ Tarz & Koleksiyon"]
)

with tab1:
    st.markdown("###  Skoda Octavia 1.6 TDI (CAY Engine)")
    col1, col2 = st.columns(2)
    with col1:
        st.info(
            "**Araç Durumu:** Aktif / Bakımda\n\n"
            "- Motor: 1.6 TDI CAY\n"
            "- Modifiye & Stance: Takipte\n"
            "- Ses Sistemi: Pioneer TS-WX300A & Reiss Midrange planlaması"
        )
    with col2:
        st.success(
            "**Garaj Notları:**\n\n"
            "- W211 Mercedes ve Porsche 911 konsept tasarımları arşivde.\n"
            "- Araç içi detaylar ve ses sistemi entegrasyonu güncel."
        )

with tab2:
    st.markdown("### Donanım & Kod Evreni")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="stat-card">
                <h4>ASUS TUF F15</h4>
                <p style='font-size: 13px; color: #a1a1aa;'>i7-13620H | RTX 4060<br>1TB Kioxia SSD + SK Hynix DDR5</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="stat-card">
                <h4>Mikrodenetleyiciler</h4>
                <p style='font-size: 13px; color: #a1a1aa;'>Arduino Uno & ESP32<br>C++, Python, MicroPython</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="stat-card">
                <h4>Web & Yazılım</h4>
                <p style='font-size: 13px; color: #a1a1aa;'>HTML, CSS, JavaScript<br>Özel Etkileşimli Projeler</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

with tab3:
    st.markdown("### Anycubic Mega S & 3D Atölyesi")
    st.write(
        "SolidWorks ve Tinkercad üzerinden tasarlanan özgün modeller, siyah PETG filament baskıları ve kişisel projeler bu alanda şekilleniyor."
    )
    st.progress(100, text="Yazıcı Durumu: Hazır & Aktif")

with tab4:
    st.markdown("### Koleksiyon & Tarz")
    st.markdown(
        "- **Tesbih Koleksiyonu:** Yılan Ağacı (Mustafa Uysal usta işçiliği), Oltu taşı, Kuka ve Kehribar.\n"
        "- **Kişisel Stil:** Kral zincir aksesuarlar, siyah taş yüzükler ve altın detaylı gözlükler.\n"
        "- **Hobiler:** DJI Mini 2 SE drone uçuşları ve oyun dünyası (GTA V, ETS 2, Valorant)."
    )

# Oturumu Kapatma Butonu
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("Güvenli Çıkışı Yap / Kilitle"):
    st.session_state.giris_yapildi = False
    st.rerun()
