# --- 5. BÖLÜM: ORTAK YAPILACAKLAR LİSTESİ ---
    st.markdown("---")
    st.header("🎯 Birlikte Yapacaklarımız")
    st.write(
        "Gelecekte hayalini kurduğumuz ve birlikte gerçekleştireceğimiz"
        " anlar..."
    )

    # İşaretlenenleri hafızada tutmak için session_state kontrolü
    if "bucket_list_state" not in st.session_state:
        st.session_state.bucket_list_state = {}

    bucket_list = [
        (
            "Karatay Şehir Parkı'nda gölet kenarındaki kamelyalarda oturup baş"
            " başa çay içmek 🌳"
        ),
        (
            "Mevlana Meydanı çevresindeki tarihi sokaklarda ve çarşılarda el ele"
            " yürümek ✨"
        ),
        (
            "Karatay'da yöresel lezzetlerin yapıldığı nezih bir esnaf"
            " lokantasında veya restoranda baş başa yemek yemek 🍽️"
        ),
        (
            "Yüksek bir tepede gün batımına karşı kahve içip manzarayı"
            " izlemek 🏰"
        ),
        ("Sahilde dalga sesleri eşliğinde akşam yürüyüşü yapmak 🌊"),
        ("Doğanın kalbinde baş başa huzurlu vakit geçirmek 🌿"),
    ]

    for i, item in enumerate(bucket_list):
        # Her bir checkbox için unique bir anahtar (key) oluşturuyoruz ve durumunu kaydediyoruz
        mevcut_durum = st.session_state.bucket_list_state.get(i, False)
        yeni_durum = st.checkbox(item, value=mevcut_durum, key=f"bucket_{i}")
        st.session_state.bucket_list_state[i] = yeni_durum
