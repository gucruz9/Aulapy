import streamlit as st
#Problema Retangulo
st.title ("Problema Retângulo")
#Entrada de dados
base = st.number_input("Digite a base do retângulo:")
altura = st.number_input("Digite a altura do retângulo:"
#Processamento de dados
area = base * altura)
perimetro = 2 * base + altura * 2
diagonal = (base**2 + altura**2)**0.5
#Saída de dados
st.writr  f"A área do retângulo é de {area}.")
st.write(f"O perímetro do retângulo é de {perimetro}.")
st.write(f"A diagonal do retângulo é de {diagonal}.")
