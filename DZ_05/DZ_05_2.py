# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

route = input('Введите абсолютный путь до файла:\n')

# C:\Games\Goblin Wars\start.exe
# C:\Games\text.txt

def data_file(route_file: int) -> tuple:
    text = route_file.split("\\")
    file = text[-1].split('.')
    route = "\\".join(text[:-1])
    name = file[0]
    type_file = file[1]
    return (route, name, type_file)

print(data_file(route))
print(*data_file(route))

# Если распечатать кортеж полностью 
# Тo печатается два слэша, а при распаковке один
# Почему так происходит?