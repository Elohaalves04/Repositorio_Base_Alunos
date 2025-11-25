# EXERCICIO 1-2: Rota personalizada
# Adicione uma nova rota /sobre que retorna uma mensagem com seu nome e uma frase sobre você.
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá Mundo !!!'

@app.route('/sobre')
def sobre():
    return 'Oie, sou a Eloha. E reclamo demais!'


if __name__ == '__main__':
    app.run(debug=True)