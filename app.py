from datetime import datetime
import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Talha Işıkcı | Komuta Merkezi",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- GİRİŞ / ŞİFRE KONTROLÜ ---
if "giris_yapildi" not in st.session_state:
    st.session_state.giris_yapildi = False

if not st.session_state.giris_yapildi:
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #030712 0%, #0f172a 100%);
            color: #f8fafc;
        }
        .login-box {
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(56, 189, 248, 0.2);
            padding: 45px;
            border-radius: 24px;
            text-align: center;
            max-width: 420px;
            margin: 100px auto;
            box-shadow: 0 25px 50px rgba(0,0,0,0.9);
            backdrop-filter: blur(10px);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown(
            "<h2 style='color: #38bdf8; margin-bottom: 5px;'>🛡️ GÜVENLİ ÜS</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='color: #94a3b8; font-size: 13px; margin-bottom: 25px;'>Bu dijital alan yalnızca Talha Işıkcı'ya aittir.</p>",
            unsafe_allow_html=True,
        )

        sifre_giris = st.text_input(
            "Güvenlik Anahtarı",
            type="password",
            placeholder="Doğum Tarihi (GG.AA.YYYY)",
        )

        if st.button(
            "Sisteme Bağlan", use_container_width=True, type="primary"
        ):
            if sifre_giris == "20.02.2008":
                st.session_state.giris_yapildi = True
                st.rerun()
            else:
                st.error("⚠️ Erişim Reddedildi: Geçersiz Anahtar!")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()


# --- ANA PANEL (GİRİŞ BAŞARILI) ---
st.markdown(
    """
    <style>
    .stApp {
        background: #030712;
        color: #f8fafc;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .hero-card {
        background: linear-gradient(135deg, #0f172a 100%, #1e293b 0%);
        border: 1px solid rgba(56, 189, 248, 0.25);
        padding: 35px;
        border-radius: 20px;
        margin-bottom: 30px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.6);
    }
    .metric-card {
        background: #0f172a;
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 22px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        transition: transform 0.2s;
    }
    .metric-card:hover {
        border-color: rgba(56, 189, 248, 0.5);
    }
    h3 {
        color: #38bdf8 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Üst Bilgi / Profil Özeti
st.markdown(
    """
    <div class="hero-card">
        <h1 style='margin:0; color: #f8fafc; font-size: 32px; font-weight: 700;'>Hoş geldin, Komutan Talha Işıkcı 👑</h1>
        <p style='margin: 8px 0 0 0; color: #38bdf8; font-size: 16px; font-weight: 500;'>Konya | Kişisel Dijital Komuta Merkezi & Arşiv Üssü</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Sekmeler (Zenginleştirilmiş İçerik)
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🚗 Garaj & Otomotiv",
        "💻 Donanım & Kod",
        "🖨️ 3D & Donanım Atölyesi",
        "✨ Tarz & Koleksiyon",
        "🎯 Özel Alan",
    ]
)

with tab1:
    st.markdown("### 🚙 Skoda Octavia 1.6 TDI (CAY Engine)")
    col1, col2 = st.columns(2)
    with col1:
        st.info(
            "**🛠️ Aktif Araç Durumu & Bakım:**\n\n"
            "- **Motor:** 1.6 TDI CAY (Optimizasyon & Takipte)\n"
            "- **Stance & Modifiye:** Basıklık, jant ve dış detaylar planlaması\n"
            "- **Ses Sistemi Projesi:** Pioneer TS-WX300A Aktif Subwoofer + Reiss Midrange entegrasyonu"
        )
    with col2:
        st.success(
            "**🏎️ Konsept & Arşiv Garajı:**\n\n"
            "- Mercedes-Benz W211 & W124 / W140 dönemsel araştırmalar\n"
            "- Porsche 911 hatları ve Fast & Furious efsane araç konseptleri\n"
            "- Volkswagen Caddy modifiye tasarım fikirleri"
        )

with tab2:
    st.markdown("### ⚡ ASUS TUF F15 & Kod Evreni")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="metric-card">
                <h4 style='color: #38bdf8; margin-bottom: 8px;'>Sistem Donanımı</h4>
                <p style='font-size: 13px; color: #94a3b8; line-height: 1.5;'>ASUS TUF Gaming F15<br>Intel Core i7-13620H<br>NVIDIA RTX 4060<br>1TB Kioxia SSD + SK Hynix DDR5</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="metric-card">
                <h4 style='color: #38bdf8; margin-bottom: 8px;'>Gömülü Sistemler</h4>
                <p style='font-size: 13px; color: #94a3b8; line-height: 1.5;'>Arduino Uno & ESP32<br>C++, Python, MicroPython<br>Sensör & Devre Projeleri</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="metric-card">
                <h4 style='color: #38bdf8; margin-bottom: 8px;'>Yazılım Dilleri</h4>
                <p style='font-size: 13px; color: #94a3b8; line-height: 1.5;'>HTML, CSS, JavaScript<br>Streamlit Altyapısı<br>Özel Etkileşimli Arayüzler</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

with tab3:
    st.markdown("### 🖨️ Anycubic Mega S & Tasarım Atölyesi")
    st.write(
        "SolidWorks ve Tinkercad üzerinde tasarlanan özgün modeller, siyah PETG filament projeleri ve kişisel üretim hattı."
    )
    col_a, col_b = st.columns(2)
    with col_a:
        st.warning(
            "**Yazıcı Durumu:** Anycubic Mega S / Aktif\n- Malzeme: Siyah PETG\n- Tasarım Programları: SolidWorks & Tinkercad"
        )
    with col_b:
        st.info(
            "**Uçuş & Medya:**\n- DJI Mini 2 SE Drone operasyonları ve Konya/Sivas hava çekim arşivleri."
        )

with tab4:
    st.markdown("### 💎 Koleksiyon & Tarz")
    st.markdown(
        "- **Tesbih Koleksiyonu:** Snakewood (Yılan Ağacı - usta Mustafa Uysal işçiliği), Oltu taşı, Kuka ve Kehribar.\n"
        "- **Kişisel Stil:** Kral zincir aksesuarlar, siyah taş yüzükler, altın detaylı güneş gözlükleri, mat wax saç şekillendirme.\n"
        "- **Oyun Dünyası:** Grand Theft Auto V (7 yıllık serüven), Valorant, Euro Truck Simulator 2, Watch Dogs 2 ve Resident Evil 2."
    )

with tab5:
    st.markdown("### 🌌 Özel Bağlantılar & Yaşam Alanı")
    st.write(
        "Hayatının içindeki değerli bağlar, aile ve unutulmaz anıların yansıması:"
    )
    st.success(
        "❤️ **Değerli Bağlar:** Yeğenler (Ecrin, Selçuk, Furkan), aile bağları, Sivas/Şarkışla tatil hatıraları ve geleceğe yönelik güçlü adımlar."
    )

# Oturumu Kapatma / Kilitleme Butonu
st.markdown("<br><br>", unsafe_allow_html=True)
col_bos1, col_orta, col_bos2 = st.columns([2, 1, 2])
with col_orta:
    if st.button("🔒 Üssü Kilitle & Çıkış Yap", use_container_width=True):
        st.session_state.giris_yapildi = False
        st.rerun()
