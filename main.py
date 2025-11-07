# pip install pandas streamlit
import pandas as pd
import streamlit as st
import time

with st.sidebar:
    arquivo = st.file_uploader("Carregue seu arquivo CSV:")

if arquivo:
    if arquivo.name.endswith(".csv"):
        arquivo_lido = pd.read_csv(arquivo)
        time.sleep(1)
        st.write(arquivo_lido)

        if st.button("Gerar tabelas e gráficos"):
            st.write("### Preços Unitarios:")
            st.bar_chart(arquivo_lido["preco_unitario"])

            st.write("### Custos:")
            st.line_chart(arquivo_lido["custo"])

            ## Coloque mais coisas, do jeito que preferir
    else:
        st.error("Erro, seu arquivo tem que ser .csv")
elif not None:
    st.caption("Salve sua planilha excel como .csv, e depois carregue ela aqui")
