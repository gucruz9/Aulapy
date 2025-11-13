import streamlit as st 

#Problema Triângulo
TITULO = ("🔺Simulação de Triângulo🔺")
st.title(TITULO)

#Entrada de dados
st.markdown("<h3 style='text-align: left;'> Inserir os três lados do triângulo </h3>", unsafe_allow_html=True)

LadoA = st.number_input("Lado A:", min_value=0)
LadoB = st.number_input("Lado B:", min_value=0)   
LadoC = st.number_input("Lado C:", min_value=0)

perímetro = LadoA + LadoB + LadoC
area_trapezio = ((LadoA + LadoB) *LadoC) / 2

#Processamento de dados
if st.button("É um triângulo?"):

    if LadoA + LadoB >= LadoC:
        st.write (f"É um triângulo.")
    elif LadoA + LadoB <= LadoC:
        st.write (f"Não é um triângulo.")

    elif LadoA + LadoC >= LadoB:
        st.write (f"É um triângulo.")
    elif LadoA + LadoC <= LadoB:
        st.write (f"Não é um triângulo.")

    elif LadoB + LadoC >= LadoA:
        st.write (f"É um triângulo.")
    elif LadoB + LadoC <= LadoA:
        st.write (f"Não é um triângulo.")
    if (LadoA + LadoB > LadoC) and (LadoA + LadoC > LadoB) and (LadoB + LadoC > LadoA):
        st.success(f"O perímetro do triângulo é: {perímetro}")
    if  (LadoA + LadoB <= LadoC) or (LadoA + LadoC <= LadoB) or (LadoB + LadoC <= LadoA):
        st.error("Os valores inseridos não formam um triângulo.")

    if (LadoA + LadoB <= LadoC) and (LadoA + LadoC <=LadoB) and (LadoB + LadoC <= LadoA):
        st.warning (f"Não é um triângulo e sim um trapézio. A área do trapézio é: {area_trapezio}")