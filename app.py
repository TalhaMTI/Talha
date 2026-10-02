import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Talha Işıkcı | Elite Cyber Command",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- YÜKSEK KONTRASTLI CSS TASARIMI ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Inter:wght@400;600;700;800&display=swap');
    
    /* Ana Arka Plan - Derin Mat Siyah */
    .stApp {
        background-color: #08080c !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }
    
    header {visibility: hidden;}
    
    /* Login Form Kartı */
    [data-testid="stForm"] {
        background: #11121a !important;
        border: 2px solid #ffb703 !important;
        border-radius: 18px !important;
        padding: 35px 28px !important;
        box-shadow: 0 0 30px rgba(255, 183, 3, 0.25) !important;
    }
    
    /* Input (Metin Kutusu) */
    .stTextInput input {
        background-color: #000000 !important;
        border: 1.5px solid #ffb703 !important;
        color: #ffffff !important;
        border-radius: 10px !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        padding: 12px !important;
    }
    .stTextInput input::placeholder {
        color: #8a8f9e !important;
    }
    
    /* Form Gönder / Sistem Butonu (Yüksek Kontrast) */
    [data-testid="stFormSubmitButton"] button {
        background: #ffb703 !important;
        color: #000000 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        font-size: 16px !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 12px 0 !important;
        box-shadow: 0 4px 15px rgba(255, 183, 3, 0.4) !important;
        transition: all 0.2s ease-in-out !important;
    }
    [data-testid="stFormSubmitButton"] button:hover {
        background: #ffa200 !important;
        color: #000000 !important;
        box-shadow: 0 6px 22px rgba(255, 183, 3, 0.7) !important;
        transform: translateY(-2px);
    }

    /* Streamlit Standart Butonlar */
    .stButton button {
        background: #ffb703 !important;
        color: #000000 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        border-radius: 10px !important;
        border: none !important;
    }
    
    /* Sekmeler (Tabs) Kontrastı */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #11121a !important;
        border: 1px solid #2a2d3d !important;
        border-radius: 8px !important;
        color: #cbd5e1 !important;
        font-weight: 700 !important;
        padding: 10px 16px !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffb703 !important;
        color: #000000 !important;
        border-color: #ffb703 !important;
    }

    /* Genel Kart Stilleri */
    .metric-card {
        background: #11121a;
        border: 1px solid #ffb703;
        padding: 24px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 15px;
    }
    .metric-card h4 {
        color: #ffb703 !important;
        font-family: 'Orbitron', sans-serif;
        font-size: 18px !important;
        margin-bottom: 10px !important;
    }
    .metric-card p {
        color: #f1f5f9 !important;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- GİRİŞ / ŞİFRE KONTROLÜ ---
if "giris_yapildi" not in st.session_state:
    st.session_state.giris_yapildi = False

if not st.session_state.giris_yapildi:
    st.write("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.3, 1])

    with col2:
        with st.form("login_form", clear_on_submit=False):

            # Büyük Üst Kutu (MTI WEB TASARIM)
            st.markdown(
                """
                <div style="background: #1a1c29; border: 2px solid #ffb703; 
                            border-radius: 12px; padding: 16px; text-align: center; margin-bottom: 22px;">
                    <span style="font-family: 'Orbitron', sans-serif; color: #ffb703; font-weight: 900; 
                                 font-size: 18px; letter-spacing: 3px;">
                        ⚡ MTI WEB TASARIM ⚡
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Başlık ve Açıklama Metni
            st.markdown(
                """
                <div style="text-align: center; margin-bottom: 22px;">
                    <h2 style="font-family: 'Orbitron', sans-serif; color: #ffffff; font-weight: 900; 
                               font-size: 24px; letter-spacing: 1.5px; margin-bottom: 8px;">
                        👑 ELITE COMMAND
                    </h2>
                    <p style="color: #cbd5e1; font-size: 13.5px; font-weight: 600; margin: 0;">
                        Bu sistem yalnızca Komutan Talha Işıkcı'ya aittir.<br>Yetkisiz erişim yasaktır.
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Giriş Alanı ve Buton
            sifre_giris = st.text_input(
                "Güvenlik Anahtarı",
                type="password",
                placeholder="Güvenlik Anahtarını Girin",
                label_visibility="collapsed",
            )

            st.write("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

            submit_btn = st.form_submit_button(
                "SİSTEME BAĞLAN ➔", use_container_width=True
            )

            if submit_btn:
                if sifre_giris == "20.02.2008":
                    st.session_state.giris_yapildi = True
                    st.rerun()
                else:
                    st.error("⚠️️ KRİTİK HATA: Geçersiz Güvenlik Anahtarı!")

    st.stop()


# --- ANA PANEL (GİRİŞ BAŞARILI) ---
st.markdown(
    """
    <div style="background: #11121a; border: 2px solid #ffb703; padding: 30px; border-radius: 18px; margin-bottom: 25px;">
        <h1 style="font-family: 'Orbitron', sans-serif; font-size: 28px; color: #ffffff; margin: 0; font-weight: 900;">
            Hoş geldin, Komutan Talha Işıkcı 👑
        </h1>
        <p style="font-family: 'Orbitron', sans-serif; font-size: 14px; color: #ffb703; margin-top: 8px; font-weight: 800; letter-spacing: 2px;">
            KONYA | ELİT DİJİTAL KOMUTA MERKEZİ & ARŞİV ÜSSÜ
        </p>
    </div>
""",
    unsafe_allow_html=True,
)

# Sekmeler
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🚗 Garaj & Otomotiv",
        "💻 Donanım & Kod",
        "🖨️ 3D Atölyesi",
        "✨ Tarz & Koleksiyon",
        "🎯 Özel Alan",
    ]
)

with tab1:
    st.markdown(
        "<h3 style='color:#ffb703; font-family:Orbitron;'>🚙 Skoda Octavia 1.6 TDI (CAY Engine)</h3>",
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        st.info(
            "**🛠️ Aktif Araç Durumu & Bakım:**\n\n"
            "- **Motor:** 1.6 TDI CAY (Optimizasyon & Takipte)\n"
            "- **Stance & Modifiye:** Basıklık, agresif jant ve dış detaylar planlaması\n"
            "- **Ses Sistemi Projesi:** Pioneer TS-WX300A Subwoofer + Reiss Midrange"
        )
    with col2:
        st.success(
            "**🏎️ Konsept & Arşiv Garajı:**\n\n"
            "- Mercedes-Benz W211 & W124 / W140 araştırmaları\n"
            "- Porsche 911 & Fast & Furious efsane konseptler\n"
            "- Volkswagen Caddy modifiye fikirleri"
        )

with tab2:
    st.markdown(
        "<h3 style='color:#ffb703; font-family:Orbitron;'>⚡ ASUS TUF F15 & Kod Evreni</h3>",
        unsafe_allow_html=True,
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="metric-card">
                <h4>Sistem Donanımı</h4>
                <p>ASUS TUF Gaming F15<br>Intel Core i7-13620H<br>NVIDIA RTX 4060<br>1TB Kioxia SSD + DDR5</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="metric-card">
                <h4>Gömülü Sistemler</h4>
                <p>Arduino Uno & ESP32<br>C++, Python, MicroPython<br>Sensör & Devre Projeleri</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="metric-card">
                <h4>Yazılım Dilleri</h4>
                <p>HTML, CSS, JavaScript<br>Streamlit Altyapısı<br>Özel Etkileşimli Arayüzler</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

with tab3:
    st.markdown(
        "<h3 style='color:#ffb703; font-family:Orbitron;'>🖨️ Anycubic Mega S Atölyesi</h3>",
        unsafe_allow_html=True,
    )
    col_a, col_b = st.columns(2)
    with col_a:
        st.warning(
            "**Yazıcı Durumu:** Anycubic Mega S / Aktif\n- Malzeme: Siyah PETG\n- Tasarım: SolidWorks & Tinkercad"
        )
    with col_b:
        st.info(
            "**Uçuş & Medya:**\n- DJI Mini 2 SE Drone operasyonları ve hava çekim arşivleri."
        )

with tab4:
    st.markdown(
        "<h3 style='color:#ffb703; font-family:Orbitron;'>💎 Koleksiyon & Tarz</h3>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "- **Tesbih Koleksiyonu:** Snakewood, Oltu taşı, Kuka ve Kehribar.\n"
        "- **Kişisel Stil:** Kral zincir aksesuarlar, siyah taş yüzükler, altın detaylı güneş gözlükleri.\n"
        "- **Oyun Dünyası:** GTA V, Valorant, Euro Truck Simulator 2, Watch Dogs 2."
    )

with tab5:
    st.markdown(
        "<h3 style='color:#ffb703; font-family:Orbitron;'>🌌 Özel Bağlantılar</h3>",
        unsafe_allow_html=True,
    )
    st.success(
        "❤️ **Değerli Bağlar:** Yeğenler (Ecrin, Selçuk, Furkan), aile bağları, tatil hatıraları ve geleceğe yönelik güçlü adımlar."
    )

# Oturumu Kapatma Butonu
st.write("<br>", unsafe_allow_html=True)
col_bos1, col_orta, col_bos2 = st.columns([2, 1, 2])
with col_orta:
    if st.button("🔒 ÜSSÜ KİLİTLE & ÇIKIŞ YAP", use_container_width=True):
        st.session_state.giris_yapildi = False
        st.rerun()
