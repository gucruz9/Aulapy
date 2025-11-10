import streamlit as st

def celsius_fahrenheit(t):
        return (t * 1.8) + 32
def celsius_kelvin(t):
        return t + 273.15
def F_celsius (t):
        return (t - 32) * 5/9
def F_kelvin (t):
        return F_celsius(t) + 273.15
def K_celsius(t):
        return t - 273.15
def K_fahrenheit(t):
        return celsius_fahrenheit(K_celsius(t))

#Problema Temperatura
st.sidebar.title("Conversor de Temperatura")
st.title("🌡️Conversor de Temperatura🌡️")

st.sidebar.markdown("Converte a temperatura entre Celsius, Fahrenheit e Kelvin")


st.sidebar.radio(options=['Celsius', 'Kelvin', 'Fahrenheit'], key= "opcao_radio",label="Selecionar")    

#Entrada de dados
temp = st.number_input("Valor da temperatura",format="%.2f", step=1.0)

#Processamento de dados
if st.button("Convereter", icon = "🔄"):
            if celsius_selecionado:
                    st.write(f"{temp} ºC em Fahrenheit é: {celsius_fahrenheit(temp):.2f} ºF")
                    st.write(f"{temp} ºC em Kelvin é: {celsius_kelvin(temp):.2f} K")
            elif fahrenheit_selecionado:
                    st.write(f"{temp} ºF em Celsius é: {F_celsius(temp):.2f} ºC")
                    st.write(f"{temp} ºF em Kelvin é: {F_kelvin(temp):.2f} K")
            elif kelvin_selecionado:
                    st.write(f"{temp} K em Celsius é: {K_celsius(temp):.2f} ºC")
                    st.write(f"{temp} K em Fahrenheit é: {K_fahrenheit(temp):.2f} ºF")