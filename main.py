import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="AI Gambar Kupang")
st.title("🎨 AI Gambar Gratis")
prompt = st.text_input("Ketik prompt gambar:") 

if st.button("Buat Gambar"):
    if prompt:
        with st.spinner("Lagi bikin gambar..."):
            url = f"https://image.pollinations.ai/prompt/{prompt}"
            img = Image.open(BytesIO(requests.get(url).content))
            st.image(img)
    else:
        st.warning("Isi prompt dulu bang")
