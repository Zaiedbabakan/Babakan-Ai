import streamlit as st
import replicate
import os

st.set_page_config(page_title="Babakan AI V4.1", layout="centered")
st.title("🔥 Babakan AI V4.1 - Teks ke Image")

os.environ["REPLICATE_API_TOKEN"] = st.secrets["REPLICATE_API_TOKEN"]

prompt = st.text_area("📝 Tulis prompt kamu:", "seorang samurai cyberpunk, neon, 8k")

style = st.selectbox("🎨 Gaya", ["Cinematic 8K", "Anime 4K", "3D Pixar", "Digital Art"])

if st.button("🚀 GENERATE SEKARANG"):
    with st.spinner("AI lagi ngelukis... 15 detik"):
        full_prompt = f"{prompt}, {style.lower()}, ultra detailed, masterpiece"
        output = replicate.run("black-forest-labs/flux-schnell", input={"prompt": full_prompt})
        st.success("✅ Jadi!")
        st.image(output[0])
        st.download_button("📥 Download", output[0], "hasil_ai.png")
