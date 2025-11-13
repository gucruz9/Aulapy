import streamlit as st

TITULO=("Classificação de níveis de glicose no sangue")
st.markdown("<h3 style='text-align: center;'> Classificação de níveis de glicose no sangue </h3>", unsafe_allow_html=True)

st.markdown(
  """
|Nível de glicose | Classificação |
|-----------------|---------------|
| 0 - 70          | Hipoglicêmica |
| 70 - 100        | Normal        |
| 101 - 140       | Pré-diabetes  |
| 141 ou mais     | Diabetes      |
"""
)

#Entrada de dados
glicose = st.number_input("Insira o nível de glicose no sangue (mg/dL):", min_value=0)  


#Processamento de dados
if st.button("Classificar"):
    if glicose <= 70:
        st.write("Nível de glicose: Hipoglicemia")
    elif glicose <= 100:
        st.write("Nível de glicose classificado como: Normal")
        st.balloons()
    elif glicose <= 140:
        st.write("Nível de glicose classificado como: Pré-diabetes")
    else:
        st.write("Nível de glicose classificado como: Diabetes")