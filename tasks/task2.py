from flask import Blueprint, render_template, request
import csv
import io

task2_bp = Blueprint('task2_bp', __name__)

@task2_bp.route('/task2', methods=['GET', 'POST'])
def task2():
    headers = []
    rows = []
    error = None
    selected_column = None

    if request.method == 'POST':
        # 1. Перевіряємо, чи завантажено файл
        if 'csv_file' not in request.files:
            error = "Файл не знайдено."
            return render_template('task2.html', error=error)
           
        file = request.files['csv_file']
        selected_column = request.form.get('sort_column')

        if file.filename == '':
            error = "Файл не вибрано."
        elif file and file.filename.endswith('.csv'):
            try:
                stream = io.StringIO(file.stream.read().decode("UTF-8"), newline=None)
                reader = csv.DictReader(stream)
               
                headers = reader.fieldnames
                rows = list(reader)

                # 2. Якщо користувач обрав колонку для сортування — сортуємо рядки
                if selected_column and selected_column in headers:
                    # Сортуємо, намагаючись конвертувати в числа, якщо це можливо
                    def sort_key(row):
                        val = row.get(selected_column, '')
                        try:
                            return float(val)
                        except ValueError:
                            return val.lower()

                    rows.sort(key=sort_key)
            except Exception as e:
                error = f"Помилка обробки файлу: {str(e)}"
        else:
            error = "Будь ласка, завантажте файл у форматі .csv"

    return render_template('task2.html', headers=headers, rows=rows, error=error, selected_column=selected_column)