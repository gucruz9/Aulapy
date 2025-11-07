import streamlit as st

def celsius_fahrenheit(temp):
        return (temp * 1.8) + 32
def celsius_kelvin(temp):
        return temp + 273.15
def F_celsius (temp):
        return (temp - 32) * 5/9
def F_kelvin (temp):
        return F_celsius(temp) + 273.15
def K_celsius(temp):
        return temp - 273.15
def K_fahrenheit(temp):
        return celsius_fahrenheit(K_celsius(temp))

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