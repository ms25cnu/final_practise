from flask import Blueprint, render_template, request
import math

task5_bp = Blueprint('task5_bp', __name__)

def parse_vector(text):
    """Конвертує рядок типу '1, 2, 3' у список чисел [1.0, 2.0, 3.0]"""
    try:
        return [float(x.strip()) for x in text.split(',') if x.strip()]
    except ValueError:
        return None

@task5_bp.route('/task5', methods=['GET', 'POST'])
def task5():
    result = None
    error = None
    # Початкові значення для полів введення
    vec1_str = "1, 3, 5"
    vec2_str = "4, 1, 9"

    if request.method == 'POST':
        vec1_str = request.form.get('vector1', '')
        vec2_str = request.form.get('vector2', '')
       
        v1 = parse_vector(vec1_str)
        v2 = parse_vector(vec2_str)
       
        if v1 is None or v2 is None:
            error = "Некоректний формат! Вводьте числа через кому (наприклад: 1, 2.5, -3)."
        elif len(v1) != len(v2):
            error = f"Вектори повинні мати однакову розмірність! (Розмірність V1: {len(v1)}, V2: {len(v2)})."
        else:
            # --- ОБЧИСЛЕННЯ МЕТРИК ---
           
            # 1. Мангеттенська відстань (L1-норма): сума абсолютних різниць координат
            manhattan_dist = sum(abs(p - q) for p, q in zip(v1, v2))
           
            # 2. Евклідова відстань (L2-норма): корінь із суми квадратів різниць координат
            euclidean_dist = math.sqrt(sum((p - q) ** 2 for p, q in zip(v1, v2)))
           
            result = {
                "dimension": len(v1),
                "manhattan": round(manhattan_dist, 4),
                "euclidean": round(euclidean_dist, 4)
            }

    return render_template('task5.html', result=result, error=error, vec1=vec1_str, vec2=vec2_str)