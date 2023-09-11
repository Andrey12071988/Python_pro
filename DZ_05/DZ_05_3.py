# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: 
# имена str, 
# ставка int, 
# премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа
# и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

name = ['Вася', 'Коля', 'Петя']
salary = [10_000, 15_000, 20_000]
premia = ['10.25%', '20.00%', '30.00%']

slovar = {i[0]: (i[1] * i[2] / 100) for i in zip(name, salary, (float(i[:-1]) for i in premia))}

# def slovar_2 (name, salary, premia):
#     res = {}
#     x = zip(name, salary, (float(i[:-1]) for i in premia))
#     for i in x:
#         res[i[0]] = i[1] * i[2] / 100
#     return res


print(slovar)
# print(slovar_2 (name, salary, premia))