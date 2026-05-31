def run_task4():
    print("\n--- Завдання 4: Евристика MRV у задачах CSP ---")
    print("Демонстрація вибору змінної за кількістю залишкових значень в домені.")
    
    domains = {
        'Область_A': ['Червоний', 'Зелений', 'Синій'],
        'Область_B': ['Червоний', 'Зелений'],
        'Область_C': ['Зелений'],
        'Область_D': ['Червоний', 'Зелений', 'Синій', 'Жовтий']
    }

    print("\nПоточний стан доменів змінних:")
    for var, values in domains.items():
        print(f"  {var}: {values} (Всього варіантів: {len(values)})")

    candidates = {var: len(values) for var, values in domains.items() if len(values) > 0}
    
    if candidates:
        mrv_variable = min(candidates, key=candidates.get)
        print("\n" + "-"*40)
        print(f"Результат евристики MRV:")
        print(f"Наступною для розфарбовування обирається: {mrv_variable}")
        print(f"Обґрунтування: ця змінна має найменший розмір домену ({candidates[mrv_variable]} варіант(ів)).")
        print("-"*40)
    else:
        print("\nНемає доступних змінних.")

if __name__ == '__main__':
    run_task4()
