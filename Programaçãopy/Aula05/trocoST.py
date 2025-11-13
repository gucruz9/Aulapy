import streamlit as st

#Problema Troco
TITULO = "Troco para um produto da Marcenaria do Matheus"
st.markdown("<h1 style='text-align: center;'> Troco para um produto da Marcenaria do Matheus </h1>", unsafe_allow_html=True)


#Entrada de dados
valor = st.number_input("Digite o valor do produto:", min_value=0.0)
quantidade_produtos = st.number_input("Digite a quantidade de produtos:", min_value=0, step=1)
st.write(f"O preço desse produto é R$ {valor * quantidade_produtos:.2f}.")
pago = st.number_input("Digite o valor pago pelo cliente:", min_value=0.0)

#Processamento de dados
troco = (pago - (valor * quantidade_produtos))
real = 100 // 100
centavo = 100
x = valor * quantidade_produtos
pago = quantidade_produtos * valor

#Saída de dados
st.write(f"O troco a ser dado ao cliente é de R$ {troco:.2f}.",)