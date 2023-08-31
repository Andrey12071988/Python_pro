# 1.1 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке

for i in range(1, 10, 3):
    for j in range(1, 10):
        for k in range(i, i+3):
            print(f'{k} * {j} = {k*j}', end='     ')
        print('')
    print('')