import streamlit as st

#Problema experiências com cobaias
st.title("Laboratório de Cobaias")

#Declaração de variáveis de controle
total_cobaias  = 0
total_ratos = 0
total_sapos = 0
total_coelhos = 0

#Entrada de dados
n = st.number_input("Digite o número de experimentos:", min_value=0, step=1)

#Estrutura de controle - PARA - Loop determinado em python
for i in range(n):
    quantidade = st.number_input(f"Experimento {i+1} - Quantidade de cobaias utilizadas",
                                                   min_value=1, step=1)
    tipo = st.selectbox(f"Experimento {i+1} - Tipo de cobaia (C:Coelho,R:Rato,S:Sapo):", options = ['C', 'R', 'S'])

#Processamento de dados
    total_cobaias += quantidade 
    if tipo == 'C':
        total_coelhos += quantidade
    elif tipo == 'R':
        total_ratos += quantidade
    elif tipo == 'S':
        total_sapos += quantidade


if total_cobaias > 0:
    percentutal_coelhos = (total_coelhos / total_cobaias) * 100
    percentutal_ratos = (total_ratos / total_cobaias) * 100
    percentutal_sapos = (total_sapos / total_cobaias) * 100
else:
    percentutal_coelhos = percentutal_ratos = percentutal_sapos = 0

    #Saída de dados
st.subheader("Resultados:")
st.write("Total de cobaias utilizadas: ", total_cobaias)
st.write("Total de coelhos utilizados: ", total_coelhos)
st.write("Total de ratos utilizados: ", total_ratos)
st.write("Total de sapos utilizados: ", total_sapos)

#Percentual
st.write (f"Percentual de coelhos: {percentutal_coelhos:.2f} %")
st.write (f"Percentual de ratos: {percentutal_ratos:.2f} %")
st.write (f"Percentual de sapos: {percentutal_sapos:.2f} %")