import os

def group_rename (ending: str,
                  size_number: int,
                  extension_start: str,
                  extension_end: str,
                  range_name_file: list):
    """
    ending - желаемое конечное имя файлов\n
    size_number - количество цифр в порядковом номере\n
    extension_start - изначальное расширение файла\n
    extension_end - конечное расширение файла\n
    range_name_file - диапазон сохраняемой старой части имени файла [a, b]
    """
    count = 1
    list_dir = os.listdir()
    count_text = ''
    new_name = ''
    for file in list_dir:
        file_name = file.split('.') # Разделение имени файла на имя и расширение
        if file_name[-1] == extension_start:
            # Создание порядкового номера (в скобках, под виндовс)
            count_text = f'({str(count).zfill(size_number)})'
            count += 1
            # Создание нового имени файла
            new_name = file_name[0][range_name_file[0]: range_name_file[1]]
            new_name += f'{ending}{count_text}.{extension_end}'
            os.rename(file, new_name)
    
group_rename("pikachu", 3, "pro", "tpm", [2, 5])