
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Criação do banco de dados (caso não exista)
def init_db():
    conn = sqlite3.connect('pereirao.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            whatsapp TEXT,
            placa TEXT,
            modelo TEXT,
            ano TEXT,
            observacoes TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        dados = (
            request.form['nome'],
            request.form['telefone'],
            request.form['whatsapp'],
            request.form['placa'],
            request.form['modelo'],
            request.form['ano'],
            request.form['observacoes']
        )
        conn = sqlite3.connect('pereirao.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, telefone, whatsapp, placa, modelo, ano, observacoes) VALUES (?, ?, ?, ?, ?, ?, ?)", dados)
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('clientes.html')

if __name__ == '__main__':
    app.run(debug=True)
