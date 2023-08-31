# Напишите программу, которая принимает две строки вида “a/b” - # дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. 
# Для проверки своего кода используйте модуль fractions.

import math
import fractions

drobs = drobs_sum = [[0, 0], [0, 0]]
res = [0, 0]
nod = 0
value = 0

# 1.1
# drob_1 = input('Введите первое дробное число вида А/В: ')
# drob_2 = input('Введите второе дробное число вида А/В: ')
# drob_1 = drob_1.split('/')
# drobs[0] = int(drob_1[0])
# drobs[1] = int(drob_1[1])
# drob_2 = drob_2.split('/')
# drobs[2] = int(drob_2[0])
# drobs[3] = int(drob_2[1])

# 1.2 Умножение дробей
for i in range(2):
    text: str = input(f'Введите {i+1} дробь в виде А/В: ')
    text = text.split('/')
    drobs[i][0] = int(text[0])
    drobs[i][1] = int(text[1])
    drobs_sum = drobs

res[0] = drobs[0][0] * drobs[1][0]
res[1] = drobs[0][1] * drobs[1][1]
nod = math.gcd(res[0], res[1])

print(f'{drobs[0][0]}/{drobs[0][1]} * {drobs[1][0]}/{drobs[1][1]} = \
{res[0]}/{res[1]} или {int(res[0] / nod)}/{int(res[1] / nod)}')
print(fractions.Fraction(drobs[0][0], drobs[0][1]) * fractions.Fraction(drobs[1][0], drobs[1][1]))

print('')

# 2.1 Сложение дробей
print(f'{drobs_sum[0][0]}/{drobs_sum[0][1]} + {drobs_sum[1][0]}/{drobs_sum[1][1]} = ', end = '')

drobs_sum[0][0] *= drobs_sum[1][1]
drobs_sum[1][0] *= drobs_sum[0][1]
res[0] = (drobs_sum[0][0] * drobs_sum[1][1]) + (drobs_sum[1][0] * drobs_sum[0][1])
res[1] = drobs_sum[1][1] * drobs_sum[0][1]
nod = math.gcd(res[0], res[1])

print(f'{res[0]}/{res[1]} или {int(res[0] / nod)}/{int(res[1] / nod)}')
print(fractions.Fraction(drobs_sum[0][0], drobs_sum[0][1]) +\
fractions.Fraction(drobs_sum[1][0], drobs_sum[1][1]))