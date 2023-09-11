# ✔ Создайте функцию-генератор. Функция генерирует 
# N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def is_simple (num: int) -> bool:
    if num == 1:
        return False
    if num == 2:
        return True
    if not num % 2:
        return False
    for div in range(3, int(num ** 0.5) + 1, 2):
        if not num % div:
            return False
    return True

def simple_gen (*args):
    """
    Для работы генератора введите до 2 значений:\n
    1 значение:\n
        1-е значение: верхняя граница вывода чисел
    2 значения:\n
        1-е значение: нижняя граница вывода чисел\n
        2-е значение: верхняя граница вывода чисел
    """
    if len(args) == 1 and isinstance(args[0], int):
        low_limit = 2
        hi_limit = args[0]
    elif len(args) == 2 and all(map(lambda x: isinstance(x, int), args)):
        low_limit = args[0]
        hi_limit = args[1]
    else:
        ValueError
    for i in range(hi_limit + 1):
        if is_simple(i):
            if i >= low_limit:
                yield i
                
print(*simple_gen(10, 30))