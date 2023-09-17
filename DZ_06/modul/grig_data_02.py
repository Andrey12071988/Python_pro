import sys
# Запустить этот файл через терминал, передав значения вида 
# python grig_data_02.py 12.12.2000

def kalendar(argv_data) -> bool:
    """Введите дату в формате ДД ММ ГГГГ
    от 1 января 1 года (1 1 1)
    до 31 декабря 9999 года (31 12 9999)
    для определения существования даты"""
    
    d, m, y, *_ = map(int, argv_data[1].split('.'))
    if 0 < d < 32 and 0 < m < 13 and 0 < y < 10000:
        if m % 2 != 0 and _visokos(y):
            return True
        elif m != 2 and 0 < d < 31 and _visokos(y):
            return True
        elif 0 < d < 30 and m == 2 and _visokos(y):
            return True
        else:
            return False
    else:
        return False


def _visokos (year: int) -> bool:
    # True  - Високосный год
    # False - Не високосный год
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True
    
print(kalendar(sys.argv))