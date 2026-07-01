import streamlit as st
import replicate

REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]

st.set_page_config(page_title="Babakan AI")
st.title("🎨 Babakan AI Image Generator")

prompt = st.text_input("Mau generate gambar apa?", "a cat wearing a wizard hat")

if st.button("GENERATE"):
    with st.spinner("Lagi bikin gambar... tunggu 10 detik"):
        output = replicate.run(
            "black-forest-labs/flux-schnell", # Model AI gratis paling cepet
            input={"prompt": prompt}
        )
        st.image(output[0])
        st.success("Jadi!")
