import streamlit as st

#-------------------------------------------------- Sidebar
st.sidebar.image('logo.png')
st.sidebar.title('Autogo')
st.sidebar.title('Aluguel de carros')


carros = ['Onix','Argo','Kwid','Civic']

opcao = st.sidebar.selectbox('Escolha o carro para ser alugado', carros)




#------------------------------------------------- Principal
st.title('Autogo - Aluguel de carros')

st.image(f'{opcao}.png')
st.markdown(f'### Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado? ')
km = st.text_input(f'Quantos KM você rodou com o {opcao}? ')

if opcao == 'Onix':
    diaria = 100

elif opcao == 'Argo':
    diaria = 110

elif opcao == 'Kwid':
    diaria = 90

elif opcao == 'Civic':
    diaria = 150



if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou por {km} KM. O valor total a pagar é: {aluguel_total}')