import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# Dados para o fluxo de caixa
data = {
    'Mês': ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'],
    'Entradas': [34745541.22, 33745300.16, 65997279.44, 30926683.55, 49047789.55, 16456987.55,
                 111205433.99, 34085452.68, 105246115.00, 15171392.65, 55648173.99, 44465958.22],
    'Saídas': [5274943.70, 3156041.25, 3259387.61, 3004834.17, 3015000.86, 2670299.24,
               2954409.71, 2794067.40, 2915401.57, 2704581.75, 3082383.06, 2830905.29],
    'Saldo Acumulado': [29470597.52, 30589258.91, 62737891.83, 27921849.38, 46032788.69,
                        13789688.31, 108251024.28, 31291385.28, 102330713.43, 12466810.90,
                        52565790.93, 41635052.93]
}
df = pd.DataFrame(data)

# Calcula os valores totais
total_entradas = df['Entradas'].sum()
total_saidas = df['Saídas'].sum()
saldo_acumulado = df['Saldo Acumulado'].iloc[-1]

# Configuração do layout do app
st.set_page_config(page_title="Fluxo de Caixa", layout="wide")

# Estilo CSS para bordas arredondadas e sombras
st.markdown("""
    <style>
        .metric-box {
            padding: 20px;
            border-radius: 5px;
            /*background-color: #1f2c56;*/
            background-color: #6A0DAD;/**/
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            color: white;
            text-align: center;
            margin-bottom: 20px;
        }
        .chart-box {
            padding: 15px;
            border-radius: 5px;
            background-color: #1f2c56;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("Fluxo de Caixa")

# Indicadores de KPIs com estilo personalizado
st.subheader("Indicadores")
col1, col2, col3 = st.columns(3)
col1.markdown(f"<div class='metric-box'><h4>Total de Entradas</h4><h2>R$ {total_entradas:,.2f}</h2></div>", unsafe_allow_html=True)
col2.markdown(f"<div class='metric-box'><h4>Total de Saídas</h4><h2>R$ {total_saidas:,.2f}</h2></div>", unsafe_allow_html=True)
col3.markdown(f"<div class='metric-box'><h4>Saldo Acumulado</h4><h2>R$ {saldo_acumulado:,.2f}</h2></div>", unsafe_allow_html=True)

# Primeira linha de gráficos
st.subheader("Gráficos")
col1, col2, col3 = st.columns(3)

# Gráfico de Entradas e Saídas por Mês
fig1 = go.Figure()
fig1.add_trace(go.Bar(name='Entradas',x=df['Mês'], y=df['Entradas'], marker=dict(color='#19AAE1'), text=df['Entradas'], textposition='outside',textfont_size=30))
fig1.add_trace(go.Bar(name='Saídas', x=df['Mês'], y=df['Saídas'], marker=dict(color='orange'), text=df['Saídas'], textposition='outside',textfont_size=20))
fig1.update_layout(title="Entradas e Saídas por Mês",barmode='group', paper_bgcolor='#1f2c56',plot_bgcolor='#1f2c56',font=dict(color='white'))
#col1.plotly_chart(fig1, use_container_width=True)
with st.container():
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    col1.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# Gráfico de Evolução do Saldo Acumulado
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df['Mês'], y=df['Saldo Acumulado'], mode='lines+markers',
                          line=dict(color='orange', width=3), marker=dict(size=8, color='#19AAE1')))
fig2.update_layout(
    title="Evolução do Saldo Acumulado",
    paper_bgcolor='#1f2c56',
    plot_bgcolor='#1f2c56',
    font=dict(color='white')
)
col2.plotly_chart(fig2, use_container_width=True)

# Gráfico de Donut para Distribuição de Entradas e Saídas
fig3 = go.Figure(data=[go.Pie(labels=['Entradas Totais', 'Saídas Totais'],
                              values=[total_entradas, total_saidas],
                              hole=0.5,
                              marker=dict(colors=['purple', 'orange']))])
fig3.update_layout(
    title="Distribuição de Entradas e Saídas Totais",
    paper_bgcolor='#1f2c56',
    font=dict(color='white')
)
col3.plotly_chart(fig3, use_container_width=True)

# Segunda linha de gráficos
col4, col5, col6 = st.columns(3)

# Gráfico de Saídas por Mês com Linha
fig4 = go.Figure()
fig4.add_trace(go.Bar(name='Saídas', x=df['Mês'], y=df['Saídas'], marker=dict(
    color='orange'), width=0.3))
fig4.add_trace(go.Scatter(x=df['Mês'], y=df['Saídas'], mode='lines+markers',
                          line=dict(color='white', width=2), marker=dict(size=6, color='white')))
fig4.update_layout(
    title="Saídas por Mês com Linha",
    paper_bgcolor='#1f2c56',
    plot_bgcolor='#1f2c56',
    font=dict(color='white')
)
col4.plotly_chart(fig4, use_container_width=True)

# Gráfico de Entradas por Mês com Linha
fig5 = go.Figure()
fig5.add_trace(go.Bar(name='Entradas', x=df['Mês'], y=df['Entradas'], marker=dict(
    color='#19AAE1'), width=0.3))
fig5.add_trace(go.Scatter(x=df['Mês'], y=df['Entradas'], mode='lines+markers',
                          line=dict(color='white', width=2), marker=dict(size=6, color='white')))
fig5.update_layout(
    title="Entradas por Mês",
    paper_bgcolor='#1f2c56',
    plot_bgcolor='#1f2c56',
    font=dict(color='white')
)
col5.plotly_chart(fig5, use_container_width=True)

# Gráfico de Bolhas Representando Entradas, Saídas e Saldo
fig6 = go.Figure(data=[go.Scatter(
    x=df['Mês'], y=df['Saldo Acumulado'], mode='markers',
    marker=dict(size=df['Entradas'] / 1000000,
                color=df['Saldo Acumulado'], colorscale='Viridis', showscale=True)
)])
fig6.update_layout(
    title="Bolhas Representando Entradas, Saídas e Saldo",
    paper_bgcolor='#1f2c56',
    plot_bgcolor='#1f2c56',
    font=dict(color='white')
)
col6.plotly_chart(fig6, use_container_width=True)

# Tabela de Transações
st.subheader("Tabela de Transações")
st.dataframe(df)
# Elementos na sidebar que não serão afetados pelo fundo de vídeo
with st.sidebar:
    st.image("dashboard.png",
             use_column_width=True)
