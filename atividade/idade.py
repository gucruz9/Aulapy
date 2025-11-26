import streamlit as st

st.title("Análise de Pessoas 👤")

# Quantidade de pessoas
qtd = st.number_input("Quantas pessoas serão digitadas?", min_value=1, step=1)

nomes = []
idades = []
alturas = []

st.write("---")

# Entrada dos dados
for i in range(qtd):
    st.subheader(f"Dados da {i+1}ª pessoa:")

    nome = st.text_input(f"Nome da {i+1}ª pessoa", key=f"nome_{i}")
    idade = st.number_input(f"Idade da {i+1}ª pessoa", min_value=0, step=1, key=f"idade_{i}")
    altura = st.number_input(f"Altura da {i+1}ª pessoa", min_value=0.0, step=0.01, key=f"altura_{i}")

    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)

st.write("---")

if st.button("Calcular"):
    # Altura média
    altura_media = sum(alturas) / len(alturas)

    # Pessoas com menos de 16 anos
    menores_16 = [nomes[i] for i in range(qtd) if idades[i] < 16]
    perc_menores = (len(menores_16) / qtd) * 100

    st.subheader("Resultados:")

    st.write(f"**Altura média:** {altura_media:.2f}")
    st.write(f"**Pessoas com menos de 16 anos:** {perc_menores:.1f}%")

    for nome in menores_16:
        st.write(nome)

