from flask import Flask, render_template

from tasks.task1 import task1_bp
from tasks.task2 import task2_bp
from tasks.task3 import task3_bp

app = Flask(__name__)

# Словник
app.register_blueprint(task1_bp)
# CSV file
app.register_blueprint(task2_bp)
# Game Nim
app.register_blueprint(task3_bp)

# Головна сторінка
@app.route('/')
def main_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
