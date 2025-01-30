import yt_dlp
import streamlit as st
import hashlib


# Função para baixar vídeo usando yt-dlp
def download_video(url, output_path):
    ydl_opts = {
        'format': 'best',  # Baixa o melhor formato disponível
        'outtmpl': output_path,  # Define o caminho de saída para o vídeo
        'noplaylist': True,  # Garante que apenas um vídeo seja baixado, não uma playlist
        'nocheckcertificate': True,  # Evitar problemas com certificados SSL
        'no_cache_dir': True,  # Forçar o download sem usar o cache
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Função para gerar um nome único para o vídeo com base na URL
def generate_unique_filename(url):
    # Gerar um hash MD5 da URL para criar um nome único
    url_hash = hashlib.md5(url.encode()).hexdigest()
    return f"video_baixado_{url_hash}.mp4"

# Personalização do tema com cor verde para fundo e vermelho para botões
st.set_page_config(page_title="Vídeos downloader", page_icon="🎥")
st.markdown(
    """
    <style>
    /* Definir o fundo da página e cor da fonte */
    .main {
        background-color: #28a745 !important;  /* Cor verde para o fundo */
    }
    .css-1d391kg {
        color: white;  /* Cor do título em branco */
    }
    .stButton>button {
        background-color: #dc3545;  /* Cor vermelha para o botão */
        color: white;  /* Cor das letras do botão em branco */
    }
    .stTextInput input {
        background-color: white;  /* Cor de fundo da caixa de texto branca */
        color: black;  /* Cor do texto na caixa de texto em preto */
    }
    .stTextInput label {
        color: white;  /* Cor da label da caixa de texto em branco */
    }
    .stSuccess, .stError {
        color: #28a745;  /* Cor de sucesso e erro em verde */
    }
    .stAlert {
        background-color: #1e1e1e;  /* Cor de fundo das mensagens de alerta */
        color: #28a745;
    }
    </style>
    """, unsafe_allow_html=True
)

# Adicionando o script do Google AdSense para anúncios
st.markdown(
    """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3361766067874035"
     crossorigin="anonymous"></script>
    <!-- Anuncio do site Videos -->
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-pub-3361766067874035"
         data-ad-slot="9631220694"
         data-ad-format="auto"
         data-full-width-responsive="true"></ins>
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
    """, unsafe_allow_html=True
)

# Streamlit interface
st.title("Vídeos downloader: baixe vídeos do TikTok, YouTube, Instagram e Facebook!")

st.text("Insira URL do vídeo que deseja baixar abaixo:")

# Entrada de URL do vídeo
url = st.text_input("URL do vídeo (TikTok, YouTube, Instagram ou Facebook):")

# Botão para baixar o vídeo
if st.button('Baixar vídeo'):
    if url:
        output_video = generate_unique_filename(url)  # Gerar nome único para o vídeo
        
        # Informar o status
        st.write("Baixando o vídeo... Isso pode levar algum tempo.")
        
        try:
            # Baixar o vídeo
            download_video(url, output_video)
            
            # Exibir sucesso
            st.success(f"Vídeo baixado com sucesso! O arquivo está disponível como {output_video}.")
            
            # Permitir download do arquivo gerado
            with open(output_video, "rb") as file:
                st.download_button(
                    label="Baixar vídeo",
                    data=file,
                    file_name=output_video,
                    mime="video/mp4"
                )
        except Exception as e:
            st.error(f"Ocorreu um erro ao tentar baixar o vídeo: {e}")
    else:
        st.error("Por favor, insira uma URL válida para o vídeo.")




    





