from datetime import datetime, timedelta
import os
import streamlit as st
import streamlit.components.v1 as components

# Sayfa Ayarları
st.set_page_config(
    page_title="Bir Aranın Hikayesi...", page_icon="💔", layout="centered"
)

# Tema ve Stil Ayarları
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #090d16 0%, #161f37 40%, #2a1b3d 100%);
        color: #f8fafc;
    }
    .break-container {
        background: rgba(255, 255, 255, 0.04);
        padding: 45px 30px;
        border-radius: 28px;
        border: 1px solid rgba(148, 163, 184, 0.3);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(15px);
        text-align: center;
        max-width: 500px;
        margin: 60px auto;
        animation: fadeIn 0.8s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .broken-heart-icon {
        font-size: 55px;
        color: #94a3b8;
        margin-bottom: 12px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); text-shadow: 0 0 10px rgba(148,163,184,0.4); }
        50% { transform: scale(1.08); text-shadow: 0 0 20px rgba(148,163,184,0.7); }
        100% { transform: scale(1); text-shadow: 0 0 10px rgba(148,163,184,0.4); }
    }
    h1, h2, h3 {
        color: #e2e8f0 !important;
        font-family: 'Helvetica Neue', sans-serif;
        letter-spacing: 0.5px;
    }
    .break-note {
        color: #cbd5e1;
        font-size: 15px;
        line-height: 1.7;
        margin-top: 20px;
        margin-bottom: 25px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #475569, #334155);
        color: white;
        border: none;
        border-radius: 14px;
        padding: 12px 24px;
        font-weight: bold;
        font-size: 15px;
        width: 100%;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #334155, #1e293b);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Oturum Durumu Kontrolü
if "erisim_onay" not in st.session_state:
    st.session_state.erisim_onay = False

# Giriş / Bakım Ekranı
if not st.session_state.erisim_onay:
    st.markdown(
        """
        <div class="break-container">
            <div class="broken-heart-icon">🥀</div>
            <h2 style="margin-bottom: 5px;">Sistem Bakımda... ya da Askıda</h2>
            <p style="color: #94a3b8; font-size: 14px; margin-bottom: 10px;">Her hikaye bazen sessiz bir molaya ihtiyaç duyar.</p>
            <div class="break-note">
                Bu dijital komuta merkezi şu an karşılıklı alınan bir karar / yaşanan bir ayrılık nedeniyle askıya alınmıştır. 
                Hatıralar silinmedi, sadece üzerlerine biraz toz konmasına izin verildi.<br><br>
                <i>Belki bir gün yollar yeniden kesiştiğinde, bu sistem tekrar aktif olur...</i>
            </div>
    """,
        unsafe_allow_html=True,
    )

    if st.button("Yine de arşivi ve eski hatıraları incele..."):
        st.session_state.erisim_onay = True
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# İçerik Ekranı (Eğer kullanıcı ısrarla görmek isterse açılan arşiv/eski anılar kısmı)
if st.session_state.erisim_onay:
    st.markdown(
        '<div style="text-align: center; color: #94a3b8; padding: 10px;"><i>[ Arşiv Modu Görüntüleniyor ]</i></div>',
        unsafe_allow_html=True,
    )

    # Türkiye Saati Baz Alınarak Ortak Zaman
    simdi = datetime.utcnow() + timedelta(hours=3)

    # --- 1. BÖLÜM: GEÇMİŞ ZAMAN SAYAÇI ---
    st.markdown("---")
    st.header("⏳ 💞 Yaşanan Güzel Anların Hatırası 💞")

    baslangic_tarihi = datetime(2026, 9, 19, 15, 11, 0)
    fark = simdi - baslangic_tarihi

    toplam_saniye = int(fark.total_seconds())
    if toplam_saniye < 0:
        toplam_saniye = 0

    gun = toplam_saniye // 86400
    saat = (toplam_saniye % 86400) // 3600
    dakika = (toplam_saniye % 3600) // 60

    st.markdown(
        f"""
    <div style="text-align: center; background: rgba(255,255,255,0.03); border: 1px solid rgba(148,163,184,0.2); padding: 25px; border-radius: 22px; margin-bottom: 25px;">
        <h3 style="color: #cbd5e1; margin: 0; font-size: 20px;">Geride Kalan Zaman</h3>
        <p style="font-size: 32px; font-weight: bold; color: #ffffff; margin: 12px 0;">{gun} Gün, {saat} Saat, {dakika} Dakika</p>
        <p style="color: #94a3b8; font-size: 14px; margin: 0; font-weight: 500;">19 Eylül 2026 Cuma, 15:11'de başlayan...</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # --- 2. BÖLÜM: MÜZİK ÇALAR ---
    st.markdown("---")
    st.header("🎶 Kıraç - Endamın Yeter")
    st.write("O günlerin hatırına...")

    audio_path = "endaminyeter.mp3"
    if os.path.exists(audio_path):
        st.audio(audio_path, format="audio/mp3")
    else:
        st.info("🎵 Şarkı dosyası ('endaminyeter.mp3') bulunamadı.")

    # --- 3. BÖLÜM: NOTLAR VE ANILAR ---
    st.markdown("---")
    st.header("🌌 Eski Notlar")
    st.markdown(
        """
    <div style="background: rgba(255, 255, 255, 0.03); padding: 25px; border-radius: 20px; border-left: 6px solid #64748b; margin-bottom: 25px; line-height: 1.7;">
    Zamanın akıp gittiği bu evrende, yaşanan her güzel anın başımın üstünde yeri oldu. Yollarımız ayrılmış olsa da, paylaşılan gülüşlerin, edilen sohbetlerin hatırası burada saklı kalacak.<br><br>
    Her şeyin hayırlısı...
    </div>
    """,
        unsafe_allow_html=True,
    )

    if st.button("🔒 Bakım Ekranına Geri Dön"):
        st.session_state.erisim_onay = False
        st.rerun()
