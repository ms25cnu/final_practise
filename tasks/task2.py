from flask import Blueprint, render_template, request, session
import csv
import io

task2_bp = Blueprint('task2_bp', __name__)

@task2_bp.route('/task2', methods=['GET', 'POST'])
def task2():
    error = None
    selected_column = request.form.get('sort_column')

    # Якщо це новий запит або натиснули скидання, очищуємо попередні дані
    if request.method == 'GET' or request.form.get('action') == 'reset':
        session['csv_headers'] = []
        session['csv_rows'] = []
        return render_template('task2.html', headers=[], rows=[], error=error, selected_column=None)

    # 1. Випадок: Користувач завантажує НОВИЙ файл
    if 'csv_file' in request.files and request.files['csv_file'].filename != '':
        file = request.files['csv_file']
       
        if file.filename.endswith('.csv'):
            try:
                stream = io.StringIO(file.stream.read().decode("UTF-8"), newline=None)
                reader = csv.DictReader(stream)
               
                # Зберігаємо дані в сесію, щоб вони не зникали
                session['csv_headers'] = reader.fieldnames
                session['csv_rows'] = list(reader)
                selected_column = None # Скидаємо попереднє сортування для нового файлу
            except Exception as e:
                error = f"Помилка обробки файлу: {str(e)}"
        else:
            error = "Будь ласка, завантажте файл у форматі .csv"

    # Отримуємо дані з сесії (якщо вони там вже є)
    headers = session.get('csv_headers', [])
    rows = session.get('csv_rows', [])

    # 2. Випадок: Користувач обрав колонку для сортування (дані беруться з сесії)
    if selected_column and selected_column in headers and rows:
        def sort_key(row):
            val = row.get(selected_column, '')
            try:
                return float(val)  # Сортуємо як числа, якщо можливо
            except ValueError:
                return val.lower() # Інакше як текст

        # Сортуємо копію списку, щоб не псувати оригінал у сесії при кожному кліку
        rows = sorted(rows, key=sort_key)

    # Якщо спробували відправити форму без файлу і в сесії теж порожньо
    if request.method == 'POST' and not headers and not error:
        error = "Файл не вибрано або сесія застаріла. Завантажте файл знову."

    return render_template('task2.html', headers=headers, rows=rows, error=error, selected_column=selected_column)