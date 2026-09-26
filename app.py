"Gözlerin aklımdan çıkmıyor...",
],
"sarki_listesi": [
            (
            [
"Kıraç - Endamın Yeter",
"Ruhumuza kazınan o eşsiz parça 🎸",
"spotify:search:Kıraç%20Endamın%20Yeter",
            ),
            (
            ],
            [
"Duman - Senden Daha Güzel",
"Senden daha güzel kim var ki... ✨",
"spotify:search:Duman%20Senden%20Daha%20Güzel",
            ),
            (
            ],
            [
"Yalın - Ki Sen",
"Kalbe dokunan en tatlı his 💞",
"spotify:search:Yalın%20Ki%20Sen",
            ),
            ],
],
    ]
    }


def verileri_kaydet():
@@ -406,7 +406,7 @@ def verileri_kaydet():
else:
st.info("📷 Klasöre 'fotograf2.jpg' ekle")

    # --- 5. BÖLÜM: ORTAK YAPILACAKLAR LİSTESİ (Kalıcı ve Veritabanı Destekli) ---
    # --- 5. BÖLÜM: ORTAK YAPILACAKLAR LİSTESİ ---
st.markdown("---")
st.header("🎯 Birlikte Yapacaklarımız")
st.write(
@@ -491,11 +491,11 @@ def verileri_kaydet():
if yeni_sarki:
s_url = f"spotify:search:{yeni_sarki.replace(' ', '%20')}"
st.session_state.sarki_listesi.append(
                (
                [
yeni_sarki,
yeni_not if yeni_not else "Bizim Şarkımız",
s_url,
                )
                ]
)
verileri_kaydet()
st.success(
