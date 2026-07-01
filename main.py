import streamlit as st
from PIL import Image
import io
import base64

st.set_page_config(page_title="Babakan AI Pro Max", layout="centered")
st.title("🔥 Babakan AI Pro Max - Zaied Edition")
st.write("Upload fotomu. Nanti aku kasih kode buat dijadiin AI di Meta WA ini.")

uploaded_file = st.file_uploader("Upload gambar kamu di sini...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Foto Asli Kamu", use_column_width=True)
    
    # Encode gambar jadi base64
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()
    
    prompt = "Ubahlah gambar ini menjadi gaya anime 2D, detail tinggi, kualitas 4k, background studio"
    
    st.success("✅ Selesai Upload!")
    st.write("**1. Copy Prompt ini:**")
    st.code(prompt)
    st.write("**2. Copy Base64 ini ke Meta AI:**")
    st.text_area("Base64 Image", img_base64, height=150)
