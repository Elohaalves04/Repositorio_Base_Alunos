# EXERCICIO 1-4: Rota com número (tipagem na rota)
# Crie uma rota /dobro/<int:numero> que recebe um número e retorna o dobro dele.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá Mundo !!!'

@app.route('/sobre')
def sobre():
    return 'Oie, sou a Eloha. E reclamo demais!'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    if nome == 'Eloha':
        return 'Olá mestre, bom dia !'
    else:
        return f'Olá {nome}, Seja bem - vindo(a) !'
    
@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'{numero*2}'



if __name__ == '__main__':
    app.run(debug=True)