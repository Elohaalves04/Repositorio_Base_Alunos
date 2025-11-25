# EXERCICIO 1-3: Parâmetros na URL (rotas dinâmicas)
# Crie uma rota /saudacao/<nome> que retorna "Olá, <nome>! Seja bem-vindo!".

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



if __name__ == '__main__':
    app.run(debug=True)