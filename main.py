import streamlit as st
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
import torch

st.set_page_config(page_title="Babakan AI Pro", layout="centered")
st.title("🔥 Babakan AI Pro Max - Zaied Edition")

@st.cache_resource
def load_model():
    st.info("Lagi load model AI... tunggu 30 detik pertama kali ya")
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16,
        safety_checker=None
    ).to("cpu")
    return pipe

pipe = load_model()

prompt = st.text_input("1. Ketik prompt Zaied kamu:", "Zaied Dark Fall, black armor, red glowing eyes, lava background")

uploaded_file = st.file_uploader("2. Upload foto muka kamu disini 👇", type=["jpg", "png", "jpeg"])

strength = st.slider("3. Kemiripan Muka: 0.3=Mirip AI, 0.9=Mirip Kamu", 0.3, 0.9, 0.7)

if uploaded_file and st.button("🚀 GAS BIKIN ZAIED KAMU"):
    init_image = Image.open(uploaded_file).convert("RGB").resize((512, 512))
    st.image(init_image, caption="Foto Asli Kamu", width=200)

    with st.spinner("Lagi bikin Zaied versi kamu... sabar 1-2 menit"):
        result_image = pipe(
            prompt=prompt,
            image=init_image,
            strength=strength,
            guidance_scale=7.5
        ).images[0]
        st.image(result_image, caption="Hasil Zaied Kamu 🔥💀")
        st.download_button("Download Gambar", result_image, "zaied_kamu.png", "image/png")
