def verileri_yukle():
    if os.path.exists(VERITABANI_DOSYASI):
        try:
            with open(VERITABANI_DOSYASI, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "bucket_list": {},
        "notlar": [
            "Bugün yine iyi ki varsın sevgilim. ❤️",
            "Gözlerin aklımdan çıkmıyor...",
        ],
        "sarki_listesi": [
            [
                "Kıraç - Endamın Yeter",
                "Ruhumuza kazınan o eşsiz parça 🎸",
                "https://open.spotify.com/search/Kıraç%20Endamın%20Yeter",
            ],
            [
                "Duman - Senden Daha Güzel",
                "Senden daha güzel kim var ki... ✨",
                "https://open.spotify.com/search/Duman%20Senden%20Daha%20Güzel",
            ],
            [
                "Yalın - Ki Sen",
                "Kalbe dokunan en tatlı his 💞",
                "https://open.spotify.com/search/Yalın%20Ki%20Sen",
            ],
        ],
        "ask_testi_secim": "Seçiniz...",  # Yeni eklenen kalıcı alan
    }
