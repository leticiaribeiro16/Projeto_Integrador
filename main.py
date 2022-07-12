from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/sobre/<id>')
def sobre(id):
  if id == "projeto":
    return render_template('projeto.html')
  elif id == "equipe":
    return render_template('equipe.html')

@app.route('/solicitacao')
def solitacao():
	return render_template('solicitacao.html')

@app.route('/inscricao')
def inscricao():
	return render_template('inscricao.html')

@app.route('/avaliacoes')
def avaliacoes():
  clientes = [
    {'nome': 'Caio', 'nota': 3},
	  {'nome': 'Melissa', 'nota': 1},
	  {'nome': 'Bianca', 'nota': 4},
	  {'nome': 'Ana', 'nota': 5},
	  {'nome': 'Diogo', 'nota': 3},  
  ]
  return render_template('avaliacoes.html', clientes=clientes)

  

    # otherwise handle the GET request
  return render_template('form.html')
app.run(host='0.0.0.0', port=8080)
