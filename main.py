import Streamlit as st
import permintaan
from PIL import Gambar
from io import BytesIO

st.set_page_config(judul_halaman="AI Gambar Kupang")
st.judul("🎨 Gambar AI Gratis")
mengingatkan = st.input_teks("Ketik prompt gambar:")

jika st.tombol("Buat Gambar"):
    jika mengingatkan:
        dengan st.pemintal("Lagi bikin gambar..."):
            URL = f"https://image.pollinations.ai/prompt/{mengingatkan}"
            respons = permintaan.mendapatkan(URL)
            
            jika respons.status_code == 200:
                coba:
                    gambar = Gambar.membuka(BytesIO(respons.isi))
                    st.gambar(gambar, keterangan=mengingatkan)
                kecuali:
                    st.kesalahan("Gagal bikin gambar. API lagi ngaco, coba prompt lain ya 😅")
            kalau tidak:
                st.kesalahan(f"API error kode: {respons.status_code}. Coba lagi nanti")
    kalau tidak:
        st.peringatan("Isi prompt dulu bang")
