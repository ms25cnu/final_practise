import math

def parse_vector(text):
    try:
        return [float(x.strip()) for x in text.split(',') if x.strip()]
    except ValueError:
        return None

def run_task5():
    print("\n--- Завдання 5: Метрики відстані (Машинне Навчання) ---")
    print("Вводьте координати багатовимірних векторів через кому (наприклад: 1, 2, 3)")
    
    str1 = input("Введіть Вектор 1 (через кому): ")
    str2 = input("Введіть Вектор 2 (через кому): ")
    
    v1 = parse_vector(str1)
    v2 = parse_vector(str2)
    
    if v1 is None or v2 is None:
        print("Помилка: некоректний формат чисел.")
        return
        
    if len(v1) != len(v2):
        print(f"Помилка: розмірності векторів відрізняються ({len(v1)} і {len(v2)}).")
        return

    manhattan_dist = sum(abs(p - q) for p, q in zip(v1, v2))
    euclidean_dist = math.sqrt(sum((p - q) ** 2 for p, q in zip(v1, v2)))
    
    print("\n" + "="*40)
    print(f"Результати обчислень ({len(v1)}-вимірний простір):")
    print(f"  Евклідова відстань:  {round(euclidean_dist, 4)}")
    print(f"  Мангеттенська відстань: {round(manhattan_dist, 4)}")
    print("="*40)

if __name__ == '__main__':
    run_task5()
