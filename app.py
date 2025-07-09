import streamlit as st
import json

st.set_page_config(page_title="Books to Scrape Viewer", layout="wide")

st.title("📚 Books to Scrape Viewer")

try:
    with open("books.json") as f:
        books = json.load(f)
except FileNotFoundError:
    st.error("File books.json tidak ditemukan. Jalankan spider terlebih dahulu.")
    st.stop()

search = st.text_input("🔍 Cari Judul Buku:")

filtered_books = [b for b in books if search.lower() in b["title"].lower()]

st.write(f"📖 Menampilkan {len(filtered_books)} hasil")

for book in filtered_books:
    st.markdown(f"### {book['title']}")
    st.write(f"💰 Harga: {book['price']}")
    st.write(f"📦 Ketersediaan: {book['availability']}")
    st.write(f"⭐ Rating: {book['rating']}")
    st.markdown(f"[🔗 Lihat Buku]({book['link']})", unsafe_allow_html=True)
    st.markdown("---")
