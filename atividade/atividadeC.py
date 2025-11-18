import streamlit as st

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

#Problema idade
st.title("Comparação de Idades")

#Entrada de dados
st.header("Dados da Pessoa 1")
nome1 = st.text_input("Nome da Pessoa 1")
idade1 = st.number_input("Idade da Pessoa 1", min_value=0, value=0)

st.header("Dados da Pessoa 2")
nome2 = st.text_input("Nome da Pessoa 2")
idade2 = st.number_input("Idade da Pessoa 2", min_value=0, value=0)

#Saída de dados
if st.button("Comparar"):
    pessoa1 = Pessoa(nome1, idade1)
    pessoa2 = Pessoa(nome2, idade2)
    st.subheader("Resultados")



    if pessoa1.idade > pessoa2.idade:
        st.success(f"{pessoa1.nome} é mais velho(a) com {pessoa1.idade} anos.")
    elif pessoa2.idade > pessoa1.idade:
        st.success(f"{pessoa2.nome} é mais velho(a) com {pessoa2.idade} anos.")
    else:
        st.warning("As duas pessoas têm a mesma idade")