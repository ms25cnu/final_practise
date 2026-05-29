from flask import Blueprint, render_template, request, session

task3_bp = Blueprint('task3_bp', __name__)

# Максимальна кількість предметів, яку можна взяти за один хід
MAX_TAKE = 3

def minimax(stones, is_maximizing):
    """
    Алгоритм Minimax для гри Нім.
    stones: поточна кількість каменів на столі.
    is_maximizing: True, якщо хід ШІ; False, якщо хід людини.
    """
    # Базовий випадок: якщо залишився 1 камінь, той, чий зараз хід - програв.
    if stones == 1:
        return 1 if not is_maximizing else -1
    if stones == 0: # якщо забрали все, той хто ходив — програв
        return 1 if is_maximizing else -1

    if is_maximizing:
        best_score = float('-inf')
        # ШІ перебирає можливі ходи (взяти 1, 2 або 3 камені)
        for i in range(1, min(MAX_TAKE, stones) + 1):
            score = minimax(stones - i, False)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        # Симуляція ідеальних ходів людини
        for i in range(1, min(MAX_TAKE, stones) + 1):
            score = minimax(stones - i, True)
            best_score = min(score, best_score)
        return best_score

def find_best_move(stones):
    """Знаходить найкращий хід для ШІ за допомогою Minimax"""
    best_score = float('-inf')
    best_move = 1
   
    for i in range(1, min(MAX_TAKE, stones) + 1):
        score = minimax(stones - i, False)
        if score > best_score:
            best_score = score
            best_move = i
           
    return best_move

@task3_bp.route('/task3', methods=['GET', 'POST'])
def task3():
    # Нам потрібні сесії (session), щоб зберігати поточний стан гри між запитами сторінки
    if 'stones' not in session or request.form.get('action') == 'reset':
        session['stones'] = 15  # Початкова кількість каменів
        session['winner'] = None
        session['log'] = ["Гра почалася! На столі 15 каменів. Ваш хід."]

    if request.method == 'POST' and not session['winner']:
        action = request.form.get('action')
       
        # Хід користувача
        if action == 'player_move':
            player_take = int(request.form.get('player_take', 1))
            stones = session['stones']
           
            if 1 <= player_take <= min(MAX_TAKE, stones):
                stones -= player_take
                session['stones'] = stones
                session['log'].insert(0, f"Ви взяли каменів: {player_take}. Залишилось: {stones}.")
               
                # Перевірка на програш людини
                if stones <= 0:
                    session['winner'] = "Робот (ШІ)"
                    session['log'].insert(0, "🚨 Ви забрали останній камінь і програли!")
                else:
                    # Хід ШІ (якщо гра продовжується)
                    ai_take = find_best_move(stones)
                    stones -= ai_take
                    session['stones'] = stones
                    session['log'].insert(0, f"🤖 ШІ подумав і взяв каменів: {ai_take}. Залишилось: {stones}.")
                   
                    # Перевірка на програш ШІ
                    if stones <= 0:
                        session['winner'] = "Ви (Людина)"
                        session['log'].insert(0, "🎉 ШІ змушений був взяти останній камінь! Ви перемогли!")

    return render_template('task3.html',
                           stones=session['stones'],
                           winner=session['winner'],
                           log=session['log'])