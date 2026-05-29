from flask import Blueprint, render_template, request

task4_bp = Blueprint('task4_bp', __name__)

@task4_bp.route('/task4', methods=['GET', 'POST'])
def task4():
    # Визначаємо карту: 4 області (A, B, C, D) та їхні сусіди (обмеження)
    # Наприклад: А межує з B і C. B межує з А, C, D. І так далі.
    neighbors = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }

    # Початкові домени (можливі кольори для кожної області)
    # Уявімо, що для демонстрації деякі області вже частково обмежені користувачем
    default_domains = {
        'A': ['Червоний', 'Зелений', 'Синій'],
        'B': ['Червоний', 'Зелений'],
        'C': ['Зелений'],
        'D': ['Червоний', 'Зелений', 'Синій', 'Жовтий']
    }

    domains = default_domains.copy()
    mrv_variable = None
    explanation = ""

    if request.method == 'POST':
        # Дозволимо користувачу вручну налаштувати «поточний стан доменів» на сторінці,
        # щоб поекспериментувати з вибором MRV
        for var in domains.keys():
            selected_colors = request.form.getlist(f'colors_{var}')
            if selected_colors:
                domains[var] = selected_colors
            else:
                domains[var] = []  # Порожній домен, якщо нічого не обрано

        # --- АЛГОРИТМ MRV ---
        # Шукаємо змінні, які ще НЕ розфарбовані (тобто мають > 1 варіанту)
        # або просто обираємо серед усіх непустих ту, у якої найменший розмір домену.
        # Для класичного кроку CSP: обираємо змінну з найменшою кількістю доступних значень (> 0).
       
        candidates = {var: len(values) for var, values in domains.items() if len(values) > 0}
       
        if candidates:
            # Сортуємо кандидатів за кількістю значень (розміром домену)
            # min(candidates, key=candidates.get) поверне ключ з найменшим значенням
            mrv_variable = min(candidates, key=candidates.get)
           
            explanation = (
                f"📊 Евристика MRV обрала змінну <strong>{mrv_variable}</strong>, "
                f"оскільки її домен містить найменшу кількість доступних варіантів ({candidates[mrv_variable]})."
            )
        else:
            explanation = "❌ Немає доступних змінних для вибору (усі домени порожні або задача розв'язана)."

    return render_template('task4.html', domains=domains, mrv_variable=mrv_variable, explanation=explanation)