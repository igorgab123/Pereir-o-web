
from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Criação do banco de dados
conn = sqlite3.connect('pereirao.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    whatsapp TEXT,
    placa TEXT,
    modelo TEXT,
    ano TEXT,
    observacoes TEXT
)''')

conn.commit()
conn.close()

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Cadastro de cliente
@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        whatsapp = request.form['whatsapp']
        placa = request.form['placa']
        modelo = request.form['modelo']
        ano = request.form['ano']
        observacoes = request.form['observacoes']

        conn = sqlite3.connect('pereirao.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, telefone, whatsapp, placa, modelo, ano, observacoes) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (nome, telefone, whatsapp, placa, modelo, ano, observacoes))
        conn.commit()
        conn.close()

        return redirect('/')
    return render_template('clientes.html')

if __name__ == '__main__':
    app.run(debug=True)
