

from flask import Flask
import time


app = Flask(__name__)

@app.route("/")
def home():
	return "<h1>Home</h1> <br> <p>Olá, essa é uma página de testes com Flask</p>"

@app.route("/horario")
def tempo():
	tempo = time.time()
	return str(tempo)

@app.route("/usuario/<user>")
def usuario(user):
	return f'Olá senhor {user}! como você está?'


if __name__ == '__main__':
	app.run(debug = True)