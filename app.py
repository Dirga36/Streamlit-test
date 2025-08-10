# Mengimpor library yang diperlukan
import streamlit as st  # Library untuk membuat aplikasi web
import time  # Untuk mengatur waktu (delay)
from langchain_core.prompts import ChatPromptTemplate  # Template untuk prompt chat
from langchain_core.output_parsers import StrOutputParser  # Parser untuk output string
from langchain_community.chat_models import ChatOpenAI  # Model chat dari OpenAI/kompatibel

# Konfigurasi API untuk DeepSeek (digunakan melalui OpenRouter)
DEEPSEEK_API_KEY = "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"
DEEPSEEK_API_BASE = "https://openrouter.ai/api/v1"

# Fungsi untuk menginisialisasi model bahasa (LLM)
def initialize_llm():
    return ChatOpenAI(
        model_name="deepseek/deepseek-chat-v3-0324:free",  # Model DeepSeek yang digunakan
        openai_api_key=DEEPSEEK_API_KEY,  # API key untuk autentikasi
        openai_api_base=DEEPSEEK_API_BASE,  # Base URL API
        temperature=0.7,  # Kreativitas respons (0-1, semakin tinggi semakin kreatif)
        max_tokens=4000  # Jumlah token maksimal dalam respons
    )

# Fungsi untuk merespons input pengguna
def respond_to_user(problem):
    llm = initialize_llm()  # Menginisialisasi model
    
    # Membuat template prompt dengan sistem dan pesan pengguna
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """Kamu adalah CurhatIn AI, seorang pendengar yang baik dan penuh empati yang dibuat oleh Rafli Damara. 
        Tugasmu adalah mendengarkan keluh kesah pengguna dan memberikan respons yang:
        1. Menunjukkan pemahaman dan empati
        2. Tidak menghakimi
        3. Memberikan dukungan emosional
        4. Jika diperlukan, memberikan saran yang bijak (tapi jangan memaksa)
        5. Menggunakan bahasa yang santai dan akrab seperti teman baik
        
        Gunakan kata ganti "aku" untuk dirimu dan "kamu" untuk pengguna.
        Jangan berpura-pura tahu solusi untuk semua masalah.
        Jika masalah sangat serius, sarankan untuk mencari bantuan profesional.
        
        Contoh:
        User: Aku merasa sangat kesepian akhir-akhir ini
        Jawab: Aku bisa mengerti perasaan kesepian itu pasti berat. Kamu tidak sendirian, banyak orang juga merasakan hal yang sama. Mau cerita lebih banyak tentang apa yang membuat kamu merasa begitu?
        
        User: Pacarku baru putus denganku
        Jawab: Aduh, pasti sakit banget ya perasaan kamu sekarang. Putus hubungan itu memang tidak mudah. Aku di sini untuk mendengarkan kalau kamu ingin berbagi lebih banyak."""),
        ("user", "{problem}")  # Tempat untuk input pengguna
    ])
    
    # Membuat chain (alur pemrosesan): prompt -> model -> parser
    chain = prompt_template | llm | StrOutputParser()
    return chain.invoke({"problem": problem})  # Memproses input pengguna

# Fungsi untuk mereset percakapan
def reset_conversation():
    st.session_state.chat_history = [{  # Mengatur ulang riwayat chat
        "role": "assistant", 
        "content": "Hai! Aku CurhatIn, Kamu ada masalah apa nihhh?"  # Pesan pembuka
    }]
    st.rerun()  # Me-refresh halaman

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="CurhatIn: Temen Curhat Terbaik",  # Judul halaman
    page_icon="❤️‍🩹",  # Ikon halaman
    layout="wide"  # Layout lebar
)

# Antarmuka utama
st.title("Mau Cerita Apa Hari ini?")  # Judul utama
st.markdown("")  # Spasi kosong

# Sidebar (panel samping)
st.sidebar.title("❤️‍🩹 CurhatIn AI - (Beta)")  # Judul sidebar
option = st.sidebar.selectbox(  # Dropdown untuk pilihan mode
    "",
    ("CurhatIn AI - (Teman Dekat v1.0)", "CurhatIn AI - (Bestie v2.1)", "CurhatIn AI - (Psikolog v1.1)"),
)
st.sidebar.markdown("")  # Spasi kosong
st.sidebar.markdown("")  # Spasi kosong
# Deskripsi aplikasi
st.sidebar.markdown("CurhatIn AI adalah platform berbasis kecerdasan buatan yang menyediakan layanan untuk curhat dan siap menjadi teman bercerita kamu 24/7.")
st.sidebar.markdown("")  # Spasi kosong
# Link eksternal
st.sidebar.markdown("[Pelajari Selengkapnya](https://github.com/Rfldmr/vokabot-ai-customer-service-for-sv-ipb)")

st.sidebar.markdown("---")  # Garis pemisah

# Informasi privasi
st.sidebar.info("CurhatIn AI **tidak dirancang** untuk menyimpan data yang diinput oleh pengguna, menjamin sistem bebas dari kemungkinan pencurian data.")
st.sidebar.markdown("")  # Spasi kosong

# Tombol reset percakapan
if st.sidebar.button("Reset Percakapan"):
    reset_conversation()

# Inisialisasi riwayat chat jika belum ada
if "chat_history" not in st.session_state:
    reset_conversation()
    
# Kontainer untuk menampilkan chat
chat_container = st.container()
            
# Menampilkan riwayat chat
with chat_container:
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):  # Bubble chat sesuai role (user/assistant)
            st.markdown(message["content"])  # Menampilkan isi pesan
            
# Input chat dari pengguna
if prompt := st.chat_input("Tuliskan apa yang ingin kamu ceritakan..."):
    # Menambahkan pesan pengguna ke riwayat
    st.session_state.chat_history.append({"role": "user", "content": prompt})
                
    # Menampilkan pesan pengguna
    with chat_container:
        with st.chat_message("user"):
            st.markdown(prompt)
                
    # Menampilkan respons AI
    with chat_container:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()  # Tempat penampung pesan
            with st.spinner("Aku mendengarkan dengan seksama..."):  # Animasi loading
                time.sleep(1)  # Delay untuk efek realistis
                response = respond_to_user(prompt)  # Mendapatkan respons dari AI
                message_placeholder.markdown(response)  # Menampilkan respons
                

    # Menambahkan respons AI ke riwayat
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    st.rerun()  # Me-refresh untuk update tampilan
