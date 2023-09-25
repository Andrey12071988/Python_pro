# Напишите функцию, которая получает на вход директорию 
# и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, 
# а для директорий размер файлов в ней 
# с учётом всех вложенных файлов и директорий. 
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет 
# для работы с файлами разных форматов.

import os
from pathlib import Path
import json

dir_rout = 'DZ_08'
dir_list = 'dirs.json'

# Чтение файла json
def load_json(rout_dir: str) -> dict:
    if os.path.exists(rout_dir):
        with open(rout_dir, 'r', encoding='UTF-8') as file:
            data = json.load(file)
    else:
        data = {}
    return data

def dump_json(data_list: dict, rout_file: str):
    with open(rout_file, 'w', encoding='UTF-8') as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)


def dir_list (dirs: str):
    lst = os.listdir(dirs)
    for i in lst:
        if not i.count('.'):
            dir_name = dirs.split(os.path.sep)
            d = dir_name[-1]
            print(f'{d} -> {i}')
            rout = os.path.join(os.getcwd(), dirs, i)
            dir_list(rout)
            pass
        else:
            # это файл, его заносим в файл json/
            dir_name = dirs.split(os.path.sep)
            d = dir_name[-1]
            print(f'{i} ({d})')

dir_list(dir_rout)