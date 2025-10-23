import streamlit as st

#--------------------------------------------------------- Sidebar 
st.sidebar.image('logo_imc.png')
st.sidebar.title('CALCULE SEU IMC')


#--------------------------------------------------------- Sidebar
st.title('CLÍNICA LIFE')
st.image('imagem_central.png')

st.title('Calcule ')
st.markdown('---')

altura = st.text_input('Qual é a sua altura? ')
peso = st.text_input('Qual é o seu peso? ')

if st.button('Calcular'):
    altura = float(altura)
    peso = float(peso)
    imc = peso / (altura ** 2)
    
    if imc <= 18.5:
        st.warning(f'O resultado do seu imc é: {imc:.2f}. Você está abaixo do peso, se alimente melhor...')
    
    elif imc <= 24.9:
        st.warning(f'O resultado do seu imc é: {imc:.2f}. Você no peso ideal, parábens!!!')

    elif imc <= 29.9:
        st.warning(f'O resultado do seu imc é: {imc:.2f}. Você está acima do peso, tome mais cuidado com sua alimentação.')

    elif imc <= 34.9: 
        st.warning(f'O resultado do seu imc é: {imc:.2f}. Você está com obesidade grau I, é hora de se cuidar...')

    elif imc <= 39.9: 
        st.warning(f'O resultado do seu imc é: {imc:.2f}. Você está com obesidade grau II, é hora de ter mais atenção!!!')

    else:
        st.warning(f'O resultado do seu imc é: {imc:.2f}. Você está com obesidade grau III, Cuide melhor de si mesmo, isso é sério.')