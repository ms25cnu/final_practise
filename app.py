from flask import Flask, request, render_template

app = Flask(__name__)

# Словник
data_dict = {str(x): x**2 for x in range(1, 11)}

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        search_key = request.form.get('key').strip()
        result = data_dict.get(search_key, "Ключ не знайдено у словнику!")
   
    # Передаємо змінну result всередину HTML-файлу
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
