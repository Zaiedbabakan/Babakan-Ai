import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="AI Gambar Kupang")
st.title("🎨 Gambar AI Gratis")
prompt = st.text_input("Ketik prompt gambar:")

if st.button("Buat Gambar"):
    if prompt:
        with st.spinner("Lagi bikin gambar..."):
            URL = f"https://image.pollinations.ai/prompt/{prompt}"
            response = requests.get(URL)
            
            if response.status_code == 200:
                try:
                    img = Image.open(BytesIO(response.content))
                    st.image(img, caption=prompt)
                except:
                    st.error("Gagal bikin gambar. API lagi ngaco, coba prompt lain ya 😅")
            else:
                st.error(f"API error kode: {response.status_code}. Coba lagi nanti")
    else:
        st.warning("Isi prompt dulu bang")
