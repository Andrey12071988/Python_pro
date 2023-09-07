# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

number = [1, 9, 8, 3, 8, 2, 5, 1, 8, 3, 1, 0, 0, 0]
number_duble = []
# for i in list:
#     if list.count(i) > 1:
#         if list_duble.count(i) == 0:
#             list_duble.append(i)
for i in number:
    if i not in number_duble and number.count(i) > 1:
        number_duble.append(i)
print(number_duble)

# 1, 8, 3, 0