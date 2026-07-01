import streamlit as st
import replicate

# Ambil token dari Secrets. Aman.
REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]

st.set_page_config(page_title="Babakan AI Test")
st.title("✅ Babakan AI Udah Jalan")
st.success("Token kebaca! App udah gak blank lagi.")

prompt = st.text_input("Mau generate apa?")
if st.button("GENERATE"):
    st.write(f"Kamu ngetik: {prompt}")
