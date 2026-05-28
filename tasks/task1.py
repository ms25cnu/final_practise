from flask import Blueprint, render_template, request

task1_bp = Blueprint('task1_bp', __name__)

data_dict = {str(x): x**2 for x in range(1, 11)}

@task1_bp.route('/task1', methods=['GET', 'POST'])
def task1():
    result = None
    if request.method == 'POST':
        search_key = request.form.get('key').strip()
        result = data_dict.get(search_key, "Ключ не знайдено у словнику!")
   
    return render_template('task1.html', result=result)