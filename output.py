def print_results(arr, s, new_s):
    """Выводит пронумерованные хэши из массива, добавляя информацию об исходной строке"""
    for i, hash_value in enumerate(arr):
        if i + 1 < len(arr):
            print(f'{i + 1}-й хэш: {hash_value}, {s}')
        else:
            print(f'{i + 1}-й хэш: {hash_value}, {new_s}')

def check_same(arr):
    """Проверяет, все ли хэши в массиве одинаковы"""
    if len(set(arr)) == 1: # Преобразуем список в множество (удаляет дубликаты) и проверяем, остался ли один элемент
        print(f'Все из {len(arr)} хэшей одинаковые\n')
    else:
        print('Хотя бы один хэш отличается\n')