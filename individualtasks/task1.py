def run_task1():
    print("\n--- Завдання 1: Dictionary Comprehension ---")
    # Створення словника через comprehension
    squares_dict = {x: x**2 for x in range(1, 11)}
    
    print("Згенеровано словник квадратів для чисел від 1 до 10.")
    
    key_input = input("Введіть число-ключ (від 1 до 10): ").strip()
    try:
        key = int(key_input)
        if key in squares_dict:
            print(f"Значення для ключа {key} (квадрат числа): {squares_dict[key]}")
        else:
            print("Помилка: Ключ не знайдено у словнику! (Оберіть число від 1 до 10).")
    except ValueError:
        print("Помилка: введіть коректне ціле число.")

if __name__ == '__main__':
    run_task1()
