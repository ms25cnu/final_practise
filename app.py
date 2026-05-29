from flask import Flask, render_template

from tasks.task1 import task1_bp
from tasks.task2 import task2_bp
from tasks.task3 import task3_bp
from tasks.task4 import task4_bp
from tasks.task5 import task5_bp

app = Flask(__name__)
app.secret_key = 'super-secret-key-for-nim-game'

# Словник
app.register_blueprint(task1_bp)
# CSV file
app.register_blueprint(task2_bp)
# Game Nim
app.register_blueprint(task3_bp)
# MRV
app.register_blueprint(task4_bp)
# Task5
app.register_blueprint(task5_bp)

# Головна сторінка
@app.route('/')
def main_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
