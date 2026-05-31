MAX_TAKE = 3

def minimax(stones, is_maximizing):
    if stones == 1:
        return 1 if not is_maximizing else -1
    if stones == 0:
        return 1 if is_maximizing else -1

    if is_maximizing:
        best_score = float('-inf')
        for i in range(1, min(MAX_TAKE, stones) + 1):
            score = minimax(stones - i, False)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(1, min(MAX_TAKE, stones) + 1):
            score = minimax(stones - i, True)
            best_score = min(score, best_score)
        return best_score

def find_best_move(stones):
    best_score = float('-inf')
    best_move = 1
    for i in range(1, min(MAX_TAKE, stones) + 1):
        score = minimax(stones - i, False)
        if score > best_score:
            best_score = score
            best_move = i
    return best_move

def run_task3():
    print("\n--- Завдання 3: Гра Нім проти ШІ (Minimax) ---")
    print("Правила: на столі 15 каменів. Можна брати 1, 2 або 3 камені. Хто бере ОСТАННІЙ — програє!")
    
    stones = 15
    while stones > 0:
        print(f"\nКаменів на столі: {stones} " + "* " * stones)
        
        while True:
            try:
                take = int(input(f"Ваш хід! Скільки каменів берете (1-{min(MAX_TAKE, stones)}): "))
                if 1 <= take <= min(MAX_TAKE, stones):
                    break
                print("Некоректна кількість!")
            except ValueError:
                print("Будь ласка, введіть число.")

        stones -= take
        if stones <= 0:
            print("\nВи взяли останній камінь! Ви ПРОГРАЛИ. Переміг ШІ!")
            break

        print("ШІ думає...")
        ai_take = find_best_move(stones)
        print(f"Робот взяв каменів: {ai_take}")
        stones -= ai_take
        
        if stones <= 0:
            print("\nШІ змушений був взяти останній камінь! Ви ПЕРЕМОГЛИ!")
            break

if __name__ == '__main__':
    run_task3()
