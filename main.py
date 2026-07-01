import streamlit as st
from PIL import Image 
import urllib.parse

st.set_page_config(page_title="Babakan AI Pro Max", layout="centered")
st.title("🔥 Babakan AI V3.2 - 1 Klik Generate")

uploaded_file = st.file_uploader("📸 Upload gambar kamu", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.success("✅ Foto berhasil diupload!")
    image = Image.open(uploaded_file) 
    st.image(image, caption="Preview Foto Kamu", width=250)
    
    st.write("### 🚀 Pilih Gaya > Tap Tombolnya:")
    
    tab1, tab2, tab3 = st.tabs(["🎌 Anime", "📷 Realistic", "🧸 3D Pixar"])
    
    prompts = {
        "anime": "Ubahlah foto ini menjadi karakter anime 2D, gaya Makoto Shinkai, detail tinggi 4K, studio lighting, mata besar ekspresif, background bunga sakura blur",
        "realistic": "Jadikan foto ini potret sinematik 8K, lighting profesional, bokeh background, kulit sangat detail, ekspresi percaya diri, seperti foto studio fashion",
        "pixar": "Ubah foto ini menjadi karakter 3D gaya Pixar, warna cerah, ekspresi bahagia, render sangat detail, kulit halus, background studio putih"
    }
    
    with tab1:
        st.code(prompts["anime"])
        wa_text = urllib.parse.quote(f"Bang tolong generate gambar ini. Prompt: {prompts['anime']}")
        st.link_button("🎌 Generate Anime Sekarang", f"https://wa.me/?text={wa_text}")
        
    with tab2:
        st.code(prompts["realistic"])
        wa_text = urllib.parse.quote(f"Bang tolong generate gambar ini. Prompt: {prompts['realistic']}")
        st.link_button("📷 Generate Realistic Sekarang", f"https://wa.me/?text={wa_text}")
        
    with tab3:
        st.code(prompts["pixar"])
        wa_text = urllib.parse.quote(f"Bang tolong generate gambar ini. Prompt: {prompts['pixar']}")
        st.link_button("🧸 Generate 3D Pixar Sekarang", f"https://wa.me/?text={wa_text}")
        
    st.warning("⚠️ Catatan: Tetep upload foto kamu lagi di chat WhatsApp ya bang. HP gak bisa kirim foto otomatis.")
