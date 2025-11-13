import streamlit as st


def grafico(datsu1, datsu2, datsu3):
    #Apresentação de gráfico exibindo lançamento

    st.area_chart([0, datsu1],
                  use_container_width=True, height=200, color="#eaff00")
    st.area_chart([0, datsu2],
                  use_container_width=True, height=200, color="#f65200")
    st.area_chart([0, datsu3],
                  use_container_width=True, height=200, color= "#5100ff")
    




st.title("🎯Simulação de Lançamento de Dardo🎯")

""" Simulação de lançamento de tres dardos. O objetivo do aplicativo e mostrar o dado com a maior distancia"""

#Entrada de dados
st.header("Inserir as tres distâncias dos dardos lançados pelo jogador")
coluna1, coluna2, coluna3 =st.columns(3)
with coluna1:
    dardo1 = st.number_input("Distancia do 1º Dardo:",min_value=0)
with coluna2:
    dardo2 = st.number_input("Distancia do 2º Dardo:",min_value=0)
with coluna3:
    dardo3 = st.number_input("Distancia do 3º Dardo:",min_value=0)
maior_distancia= max(dardo1,dardo2,dardo3)
#Estrutura de controle de decisão
if (dardo1 > dardo2) and (dardo1 > dardo3):
    dardo_vencedor = "Dardo1"
elif (dardo2 > dardo1) and (dardo2 > dardo3):
    dardo_vencedor = "Dardo2"
elif dardo1 == dardo2 and dardo1 == dardo3 or dardo2 == dardo3:
    dardo_vencedor = "Empate"
else:
    dardo_vencedor = "Dardo3"

    #Saída de dados
if st.button("Apresentar resultados de lançamento dos dardos"):
    if dardo_vencedor == "Empate":
        st.write("Houve um empate sem vencedores.")
    else:
        st.write(f"O dado com a maior distancia foi: {dardo_vencedor} com {maior_distancia}")
        grafico(dardo1, dardo2, dardo3)