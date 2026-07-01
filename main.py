import streamlit as st

st.set_page_config(page_title="Babakan AI", layout="centered")
st.title("🔥 Babakan AI V2")
st.write("Upload foto untuk jadiin AI. 100% jalan.")

uploaded_file = st.file_uploader("Upload gambar kamu", type=["png", "jpg"])

if uploaded_file:
    st.success("✅ Foto masuk!")
    st.write("Nama file:", uploaded_file.name)
    st.write("Sekarang tinggal tempel foto ke Meta AI pake prompt di bawah:")
    st.code("Ubahlah gambar ini menjadi anime 2D detail tinggi, 4K, studio lighting")
