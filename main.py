import streamlit as st
from PIL import Image # Cuma import doang, gak dipake berat-berat

st.set_page_config(page_title="Babakan AI Pro Max", layout="centered")
st.title("🔥 Babakan AI V3.1 - Teks ke Image ON")

uploaded_file = st.file_uploader("📸 Upload gambar kamu", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.success("✅ Foto berhasil diupload!")
    
    # BAGIAN "TEKS KE IMAGE" YANG HILANG TADI
    image = Image.open(uploaded_file) 
    st.image(image, caption="Preview Foto Kamu", width=250) # Nah ini dia
    
    st.write("### 🚀 Copy 1 dari 3 Prompt di bawah ini:")
    
    tab1, tab2, tab3 = st.tabs(["🎌 Anime", "📷 Realistic", "🧸 3D Pixar"])
    
    with tab1:
        st.code("Ubahlah gambar ini menjadi anime 2D, gaya Makoto Shinkai, detail tinggi, 4K, studio lighting")
    with tab2:
        st.code("Jadikan foto ini potret sinematik 8K, lighting profesional, bokeh background, kulit sangat detail")
    with tab3:
        st.code("Ubah menjadi karakter 3D gaya Pixar, warna cerah, ekspresi bahagia, render sangat detail")
        
    st.info("💡 Download fotonya > Upload ke Meta AI Image > Tempel prompt")
