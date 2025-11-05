import streamlit as st
import math 

st.header ('Calculadora de Bhaskara')
st.write ("Calculadora de raízes \n de uma equação de segundo grau")
st.write ( "ax² + bx + c = 0" )

#Entrada de dados
a = st.number_input('Digite o valor de a:')
b = st.number_input('Digite o valor de b:')
c = st.number_input('Digite o valor de c:')



#Processamento de dados
if st.button('Calcular raízes'):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        delta = b**2 - 4*a*c
        if delta < 0:
            st.warning('A equação não possui raízes reais.')
        elif delta ==0:
            raiz = (-b + mt.sqrt(delta)) / (2*a)
            st.success(f'A equação possui uma raiz real: {raiz}')
        else:
            raiz1 = (-b + mt.sqrt(delta)) / (2*a)
            raiz2 = (-b - mt.sqrt(delta)) / (2*a)
            st.success(f'As raízes da equação são: \n Raiz 1: {raiz1} \n Raiz 2: {raiz2}')
    except:
        st.error("Por favor, insira valores numéricos válidos para a, b e c.")

