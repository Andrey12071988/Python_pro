from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
STEP_LIMIT = 10
step = 1
num = randint(LOWER_LIMIT, UPPER_LIMIT+1)
num_player = 0

print(f'Я загадала число от 0 до 1000. Угадай его за {STEP_LIMIT} попыток')
while step <= 10:
    num_player = int(input('Введите число: '))
    if num == num_player:
        print(f'Ты угадал число за {step} попыток')
        break
    elif num > num_player:
        print('Число больше')
    else:
        print('Число меньше')
    step += 1
else:
    print(f'Ты не смог угадать число {num} за {STEP_LIMIT} попыток')