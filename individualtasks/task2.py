import csv
import os

def run_task2():
    print("\n--- Завдання 2: Сортування даних з CSV ---")
    
    # Назва файлу, який має лежати в тій же папці, що й цей скрипт
    file_name = "data.csv"
    
    # Отримуємо абсолютний шлях до папки, де лежить цей файл task2.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    print(f"Зчитую файл")

    try:
        # Відкриваємо та зчитуємо CSV файл з комп'ютера
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            rows = list(reader)

        if not headers or not rows:
            print("Помилка: Файл порожній або має некоректну структуру.")
            return

        print(f"\nДоступні колонки для сортування: {', '.join(headers)}")
        sort_col = input("Введіть назву колонки для сортування: ").strip()

        if sort_col not in headers:
            print(f"Помилка: Колонки з назвою '{sort_col}' немає в файлі.")
            return

        # Функція-ключ для сортування (намагається конвертувати в числа)
        def sort_key(row):
            val = row.get(sort_col, '')
            try:
                return float(val)
            except ValueError:
                return val.lower()

        # Сортуємо рядки
        rows.sort(key=sort_key)

        # Виводимо відсортовану таблицю в консоль
        print(f"\nВідсортовані дані за колонкою '{sort_col}':")
        print("\t".join(headers))
        print("-" * 50)
        for row in rows:
            print("\t".join([row[h] for h in headers]))

    except Exception as e:
        print(f"Помилка при роботі з файлом: {e}")

if __name__ == '__main__':
    run_task2()
