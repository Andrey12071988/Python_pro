# 1.2 Определить возможность существования треугольника и его тип
a = int(input('Вваедите длинну стороны A: '))
b = int(input('Вваедите длинну стороны B: '))
c = int(input('Вваедите длинну стороны C: '))

if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or b == c or a == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник с такими сторонами существовать не может')