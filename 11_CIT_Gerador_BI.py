import streamlit as st
import matplotlib.pyplot as plt
import io

# Título da página
st.title("Gerador de Gráficos com Matplotlib")

# Instruções
st.write("Cole o código Matplotlib abaixo e clique em 'Gerar Gráfico' para visualizar.")

# Área de texto para inserir o código Matplotlib
code = st.text_area("Código Matplotlib", height=300, value="""
Cole aqui seu código gerado no CitCashflow IA...
""")

# Botão para gerar o gráfico
if st.button("Gerar Gráfico"):
    # Buffer para salvar o gráfico como imagem
    buffer = io.BytesIO()

    # Executa o código colado pelo usuário
    try:
        # Redefine plt para garantir um gráfico limpo
        plt.clf()

        # Executa o código inserido
        exec(code)

        # Salva o gráfico no buffer
        plt.savefig(buffer, format="png")
        buffer.seek(0)

        # Exibe o gráfico
        st.image(buffer)
    except Exception as e:
        st.error(f"Ocorreu um erro ao executar o código:\n{e}")

with st.sidebar:
    st.image("dashboard.png",
             use_column_width=True)
