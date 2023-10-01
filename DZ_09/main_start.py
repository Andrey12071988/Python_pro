from random import randint
import json
import csv

# file_json = "json_file.json"
# file_csv = "csv_file.csv"

def json_save(db, file_json="json_file.json"):
    with open(file_json, 'w', encoding='UTF-8') as file:
        json.dump(db, file, indent=4, ensure_ascii=False)

def json_read (file_json):
    with open(file_json, 'r', encoding='UTF-8') as file:
        return json.load(file)

def csv_save(db, file_csv="csv_file.csv"):
    with open(file_csv, 'w', encoding='UTF-8') as file:
        # wr = csv.writer(file, dialect='excel', delimiter=';')
        # wr.writerows(db)
        csv.writer(file, dialect='excel', delimiter=';').writerows(db)

def csv_read(file_csv="csv_file.csv"):
    result = []
    with open(file_csv, 'r', encoding='UTF-8') as file:
        reader =  csv.reader(file, dialect='excel', delimiter=';')
        for row in reader:
            if row:
                result.append(list(map(float, row)))
    return result


def deco_abc(func):
    abc_list = csv_read()
    def inner():
        result = {}
        for abc in abc_list:
            roots = func(abc)
            a, b, c = abc
            result[f'{a= }, {b= }, {c=}'] = roots
        return result
    return inner

def deco_json_save(func):
    def inner():
        roots = func()
        json_save(roots)
        return roots
    return inner


@deco_json_save
@deco_abc
def quadro(abc: [int, int, int]):
    a, b, c = abc
    result = []
    d = b**2 - (4 * a * c)
    if d > 0:
        result.append(round(((-b + d**0.5) / (2 * a)), 2))
        result.append(round(((-b - d**0.5) / (2 * a)), 2))
    elif d == 0:
        result.append(round((-b / (2 * a)), 2))
    else:
        result.append(None)
    return result

def gen_abc(count: int):
    abc = []
    for i in range(count):
        res = []
        for j in range(3):
            if j:
                res.append(randint(-100, 100))
            else:
                while True:
                    a = randint(-100, 100)
                    if a:
                        res.append(a)
                        break
        abc.append(res)
    csv_save(abc)


gen_abc(randint(100, 1000))
quadro()