# 1.3 определить, простое число или составное с ограничением +- 100.000
num = 0
status = True
while status:
    num = int(input('Введите любое число от -100.000 до +100.000: '))
    
    if -100000 <= num <= 100001:
        if num < 0: num = abs(num) # получение модуля числа
        
        if num > 3:
            for i in range(2, num+1):
                if i >= num:
                    print('Число простое')
                    status = False
                    break
                elif num % i == 0:
                    print('Число составное')
                    status = False
                    break
        else:
            print('Число простое')
            status = False
    else:
        print('Введено число за пределами диапазона')