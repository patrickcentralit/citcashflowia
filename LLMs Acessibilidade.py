import streamlit as st
import base64

# Configurando a página
st.set_page_config(page_title="Landing Page", layout="wide")

# Adicionar controle deslizante para ajustar o tamanho do texto
font_size = st.sidebar.slider(
    "Tamanho do texto - Acessibilidade ♿", min_value=10, max_value=40, value=20)

# Definindo o estado de reprodução do áudio
audio_play = st.sidebar.button("🔊 Play Áudio")

# Carregar o arquivo de áudio e codificar em base64


def load_audio(file_path):
    with open(file_path, "rb") as audio_file:
        encoded_audio = base64.b64encode(audio_file.read()).decode()
    return encoded_audio


# Verifica se o arquivo de áudio existe e codifica
audio_file_path = "pages/LLMs.mp3"  # Atualizado para o nome correto
encoded_audio = load_audio(audio_file_path)

# HTML e CSS para o vídeo de fundo no corpo principal
background_video_html = """
    <style>
    /* Estiliza o vídeo para cobrir todo o fundo do corpo */
    .stApp {
        background-color: rgba(0, 0, 0, 0);
    }

    /* Video styling para ajustar ao fundo */
    #bg-video {
        position: fixed;
        top: 0;
        left: 0;
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        z-index: -1;
        background-size: cover;
        opacity: 0.7;
    }
    </style>

    <video autoplay muted loop id="bg-video">
        <source src="https://cdn.pixabay.com/video/2019/02/11/21287-316701391_large.mp4" type="video/mp4">
    </video>
"""

# HTML para a imagem e o texto
html_content = f"""
    <div style="text-align: center; margin-top: 50px; color: white;">
        <h1 style="font-size: {font_size + 12}px;color: white;">LLMs</h1>
        <p style="font-size: {font_size}px;color: white;">(Large Language Models) Grandes Modelos de Linguagem.</p>
        <img src="https://raw.githubusercontent.com/pasilva1/cashflow/refs/heads/main/robot.png" alt="Exemplo de Imagem" width="500" height="450" style="border-radius: 10px;">
        <p style="font-size: {font_size}px; color: white; margin-top: 20px; ">
            Os LLMs são treinados com grandes quantidades de dados e usam um tipo de rede neural chamada de modelo transformador. Eles podem ser usados para:
            Gerar conteúdo escrito, como artigos de notícias e scripts de marketing.
            Automação e eficiência, como suporte ao cliente, análise de dados e geração de conteúdo.
            Geração de insights, como estudar tendências do mercado e analisar o feedback dos clientes.
            Aperfeiçoamento da experiência do cliente, como implementar chatbots e personalizar mensagens de marketing.
            Segurança cibernética, como identificar padrões em dados de segurança e contribuir na prevenção de ataques.
            Geração de código, como auxiliar os desenvolvedores na construção de aplicativos.
        </p>
    </div>
"""

# Renderizando o HTML no Streamlit para aplicar o background e o conteúdo
st.markdown(background_video_html, unsafe_allow_html=True)
st.markdown(html_content, unsafe_allow_html=True)

# Adicionando a tag de áudio embutido no HTML caso o botão seja pressionado
if audio_play:
    audio_html = f"""
    <audio controls autoplay>
        <source src="data:audio/mp3;base64,{encoded_audio}" type="audio/mpeg">
        Seu navegador não suporta a reprodução de áudio.
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# Adicionando uma imagem na barra lateral
with st.sidebar:
    st.image("ai-head-android-robot-artist.gif", use_column_width=True)
