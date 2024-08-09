from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('finance.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    transactions = conn.execute('SELECT * FROM transactions').fetchall()
    conn.close()
    return render_template('index.html', transactions=transactions)

@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = request.form['amount']
        type = request.form['type']  # 'expense' or 'income'

        conn = get_db_connection()
        conn.execute('INSERT INTO transactions (date, category, amount, type) VALUES (?, ?, ?, ?)',
                     (date, category, amount, type))
        conn.commit()
        conn.close()
        return redirect('/')

    return render_template('add.html')

@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM transactions WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    transaction = conn.execute('SELECT * FROM transactions WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = request.form['amount']
        type = request.form['type']

        conn.execute('UPDATE transactions SET date = ?, category = ?, amount = ?, type = ? WHERE id = ?',
                     (date, category, amount, type, id))
        conn.commit()
        conn.close()
        return redirect('/')

    conn.close()
    return render_template('edit.html', transaction=transaction)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
