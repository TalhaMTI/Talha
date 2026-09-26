import json
import os
import streamlit as st

VERITABANI_DOSYASI = "veritabani.json"


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
        "ask_testi_secim": "Seçiniz...",
    }


# Verileri yükleyelim
kayitli_veri = verileri_yukle()

if "bucket_list_state" not in st.session_state:
    st.session_state.bucket_list_state = kayitli_veri.get("bucket_list", {})
if "notlar" not in st.session_state:
    st.session_state.notlar = kayitli_veri.get("notlar", [])
if "sarki_listesi" not in st.session_state:
    st.session_state.sarki_listesi = kayitli_veri.get("sarki_listesi", [])
if "ask_testi_secim" not in st.session_state:
    st.session_state.ask_testi_secim = kayitli_veri.get(
        "ask_testi_secim", "Seçiniz..."
    )


def verileri_kaydet():
    veri = {
        "bucket_list": st.session_state.bucket_list_state,
        "notlar": st.session_state.notlar,
        "sarki_listesi": st.session_state.sarki_listesi,
        "ask_testi_secim": st.session_state.ask_testi_secim,
    }
    with open(VERITABANI_DOSYASI, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)
