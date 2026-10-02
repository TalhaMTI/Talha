from datetime import datetime
import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Talha Işıkcı | Elite Cyber Command",
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
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
        
        .stApp {
            background: #030305;
            background-image: 
                radial-gradient(circle at 50% 20%, rgba(245, 158, 11, 0.15) 0%, transparent 40%),
                radial-gradient(circle at 10% 80%, rgba(220, 38, 38, 0.1) 0%, transparent 40%);
            color: #ffffff;
            font-family: 'Inter', sans-serif;
        }
        
        header {visibility: hidden;}
        
        /* Sayfayı tam ortalamak için esnek yapı */
        .main .block-container {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 85vh;
            padding-top: 0rem !important;
        }
        
        .login-box {
            background: rgba(18, 18, 24, 0.9);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(245, 158, 11, 0.5);
            padding: 45px 40px;
            border-radius: 24px;
            text-align: center;
            width: 100%;
            max-width: 480px;
            box-shadow: 0 0 50px rgba(245, 158, 11, 0.25), inset 0 0 20px rgba(245, 158, 11, 0.1);
            margin: auto;
            animation: pulse-border 3s infinite alternate;
        }
        @keyframes pulse-border {
            0% { border-color: rgba(245, 158, 11, 0.3); box-shadow: 0 0 30px rgba(245, 158, 11, 0.15); }
            100% { border-color: rgba(245, 158, 11, 0.8); box-shadow: 0 0 60px rgba(245, 158, 11, 0.4); }
        }
        
        .login-mti-badge {
            background: rgba(245, 158, 11, 0.12);
            border: 1px solid rgba(245, 158, 11, 0.5);
            padding: 8px 16px;
            border-radius: 12px;
            font-family: 'Orbitron', sans-serif;
            color: #f59e0b;
            font-weight: 900;
            font-size: 13px;
            letter-spacing: 3px;
            margin-bottom: 20px;
            display: inline-block;
            box-shadow: 0 0 15px rgba(245, 158, 11, 0.2);
            text-shadow: 0 0 8px rgba(245, 158, 11, 0.6);
        }
        .login-title {
            font-family: 'Orbitron', sans-serif;
            color: #ffffff;
            font-weight: 900;
            font-size: 24px;
            letter-spacing: 2px;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
            margin-bottom: 10px;
        }
        .login-box p {
            color: #e2e8f0 !important;
            font-size: 13px !important;
            font-weight: 600 !important;
        }
        .stTextInput input {
            background: #09090b !important;
            border: 1px solid rgba(245, 158, 11, 0.4) !important;
            color: #f59e0b !important;
            border-radius: 12px !important;
            font-weight: bold;
        }
        .stButton button {
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%) !important;
            color: #030305 !important;
            font-family: 'Orbitron', sans-serif !important;
            font-weight: 900 !important;
            border-radius: 12px !important;
            border: none !important;
            box-shadow: 0 0 20px rgba(245, 158, 11, 0.5);
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            transform: scale(1.03);
            box-shadow: 0 0 35px rgba(245, 158, 11, 0.8);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown(
        '<div class="login-mti-badge">⚡ MTI WEB TASARIM ⚡</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="login-title">👑 ELITE COMMAND</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='margin-bottom: 20px;'>Bu sistem yalnızca Komutan Talha Işıkcı'ya aittir. Yetkisiz erişim yasaktır.</p>",
        unsafe_allow_html=True,
    )

    sifre_giris = st.text_input(
        "Güvenlik Anahtarı", type="password", label_visibility="collapsed"
    )
    if not sifre_giris:
        st.markdown(
            "<p style='font-size: 11px; color: #94a3b8; margin-top:-5px; margin-bottom:15px;'>Güvenlik Anahtarını Girin</p>",
            unsafe_allow_html=True,
        )

    if st.button("SİSTEME BAĞLAN", use_container_width=True):
        if sifre_giris == "20.02.2008":
            st.session_state.giris_yapildi = True
            st.rerun()
        else:
            st.error("⚠️ KRİTİK HATA: Geçersiz Güvenlik Anahtarı!")
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()


# --- ANA PANEL (GİRİŞ BAŞARILI) ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');

    .stApp {
        background: #030305;
        background-image: 
            radial-gradient(circle at 20% 10%, rgba(245, 158, 11, 0.1) 0%, transparent 40%),
            radial-gradient(circle at 80% 90%, rgba(147, 51, 234, 0.08) 0%, transparent 40%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    header {visibility: hidden;}
    
    .hero-card {
        background: linear-gradient(135deg, rgba(18, 18, 24, 0.9) 0%, rgba(10, 10, 15, 0.95) 100%);
        border: 2px solid rgba(245, 158, 11, 0.4);
        padding: 40px;
        border-radius: 24px;
        margin-bottom: 30px;
        box-shadow: 0 0 40px rgba(245, 158, 11, 0.15), inset 0 0 20px rgba(245, 158, 11, 0.05);
        position: relative;
        overflow: hidden;
    }
    .hero-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; width: 4px; height: 100%;
        background: #f59e0b;
        box-shadow: 0 0 15px #f59e0b;
    }
    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 34px;
        font-weight: 900;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin: 0;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
    }
    .hero-subtitle {
        font-family: 'Orbitron', sans-serif;
        font-size: 15px;
        color: #f59e0b;
        font-weight: 700;
        margin-top: 10px;
        letter-spacing: 2px;
        text-shadow: 0 0 10px rgba(245, 158, 11, 0.5);
    }

    .mti-badge {
        background: rgba(245, 158, 11, 0.08);
        border: 1px solid rgba(245, 158, 11, 0.4);
        padding: 10px 20px;
        border-radius: 12px;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        color: #f59e0b;
        font-weight: 900;
        font-size: 14px;
        letter-spacing: 3px;
        margin-bottom: 25px;
        box-shadow: 0 0 20px rgba(245, 158, 11, 0.15);
        text-shadow: 0 0 10px rgba(245, 158, 11, 0.6);
    }

    .metric-card {
        background: rgba(18, 18, 24, 0.8);
        border: 1px solid rgba(245, 158, 11, 0.25);
        padding: 28px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    }
    .metric-card:hover {
        border-color: #f59e0b;
        transform: translateY(-6px) scale(1.02);
        box-shadow: 0 0 30px rgba(245, 158, 11, 0.3), inset 0 0 15px rgba(245, 158, 11, 0.1);
    }
    .metric-card h4 {
        font-family: 'Orbitron', sans-serif;
        color: #f59e0b !important;
        font-size: 18px !important;
        font-weight: 900 !important;
        margin-bottom: 15px !important;
        letter-spacing: 1px;
    }

    h3 {
        font-family: 'Orbitron', sans-serif !important;
        color: #f59e0b !important;
        font-weight: 900 !important;
        letter-spacing: 1px;
        text-shadow: 0 0 10px rgba(245, 158, 11, 0.3);
    }
    p, span, li, label, div {
        color: #f8fafc !important;
        font-size: 14px;
    }
    
    .stButton button {
        background: linear-gradient(135deg, #f59e0b 0%, #b45309 100%) !important;
        color: #030305 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 0 20px rgba(245, 158, 11, 0.4);
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 35px rgba(245, 158, 11, 0.7);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Üst Bilgi / Profil Özeti
st.markdown(
    """
    <div class="hero-card">
        <div class="mti-badge">⚡ MTI WEB TASARIM ⚡</div>
        <h1 class="hero-title">Hoş geldin, Komutan Talha Işıkcı 👑</h1>
        <div class="hero-subtitle">KONYA | ELİT DİJİTAL KOMUTA MERKEZİ & ARŞİV ÜSSÜ</div>
    </div>
""",
    unsafe_allow_html=True,
)

# Sekmeler
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
            "- **Stance & Modifiye:** Basıklık, agresif jant ve dış detaylar planlaması\n"
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
                <h4>Sistem Donanımı</h4>
                <p style='font-size: 13px; color: #f8fafc; line-height: 1.6;'>ASUS TUF Gaming F15<br>Intel Core i7-13620H<br>NVIDIA RTX 4060<br>1TB Kioxia SSD + SK Hynix DDR5</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="metric-card">
                <h4>Gömülü Sistemler</h4>
                <p style='font-size: 13px; color: #f8fafc; line-height: 1.6;'>Arduino Uno & ESP32<br>C++, Python, MicroPython<br>Sensör & Devre Projeleri</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="metric-card">
                <h4>Yazılım Dilleri</h4>
                <p style='font-size: 13px; color: #f8fafc; line-height: 1.6;'>HTML, CSS, JavaScript<br>Streamlit Altyapısı<br>Özel Etkileşimli Arayüzler</p>
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
    if st.button("🔒 ÜSSÜ KİLİTLE & ÇIKIŞ YAP", use_container_width=True):
        st.session_state.giris_yapildi = False
        st.rerun()
