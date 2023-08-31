# Напишите программу, которая получает целое число 
# и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

num = num2 = int(input('Введите любое целое положительное число: '))
num_hex = ''

while num:
    if num % 16 < 10:
        num_hex = str(num % 16) + num_hex
    elif num % 16 == 10:
        num_hex = 'A' + num_hex
    elif num % 16 == 11:
        num_hex = 'B' + num_hex
    elif num % 16 == 12:
        num_hex = 'C' + num_hex
    elif num % 16 == 13:
        num_hex = 'D' + num_hex
    elif num % 16 == 14:
        num_hex = 'E' + num_hex
    else:
        num_hex = 'F' + num_hex
    num //= 16

print(num_hex)
print(hex(num2))
