# 📌Напишите код, который запускается из командной строки 
# и получает на вход путь до директории на ПК.

# 📌Соберите информацию о содержимом в виде объектов namedtuple.
# 📌Каждый объект хранит: 
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл, 
# ○ флаг каталога, 
# ○ название родительского каталога.
# 📌В процессе сбора сохраните данные в текстовый файл используя логирование.

import sys
import logging
import os
from collections import namedtuple

# Установка уровня логгирования
# Определение файла логгирования
logging.basicConfig(level=logging.NOTSET, filename='jurnal.txt', filemode='a', encoding='UTF-8', style='%')

def func(part):
    directory = namedtuple('Directory', ['name', 'exp_file', 'dir_flag', 'parent_folder'])
    _, res = part
    result = os.listdir(res)
    parent_folder = res.split(os.path.sep)
    for i in result:
        dir_file = i.split('.')
        if len(dir_file) == 1:
            logging.info(directory(dir_file[0], None, True, parent_folder[-1]))
        else:
            logging.info(directory(dir_file[:-1], dir_file[-1], False, parent_folder[-1]))
            
    
func(sys.argv)