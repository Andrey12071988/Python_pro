# Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, 
# где ключ — значение переданного аргумента, 
# значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.


def key_hash(**kwargs):
    slovar = {}
    for i in kwargs:
        # i - имя ключа
        try:
            slovar[hash(kwargs[i])] = i
        except:
            slovar[str(kwargs[i])] = i
    return slovar


print(key_hash(key_1=123, key_2="hello", key_3=[125, 22] ))