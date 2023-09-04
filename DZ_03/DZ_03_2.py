# В большой текстовой строке подсчитать 
# количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии 
# или из документации к языку.

text = 'Insomniac Games — американская студия, занимающаяся разработкой компьютерных игр; её офис находится в городе Бербанк, штат Калифорния. Компания была основана в феврале 1994 года Тедом Прайсом под названием Xtreme Software, год спустя переименована в Insomniac Games. Первым проектом студии стал шутер от первого лица Disruptor для PlayStation. Компания наиболее известна как создатель таких серий компьютерных игр, как Spyro the Dragon, Ratchet & Clank, Resistance и Marvel’s Spider-Man, а также игрой Sunset Overdrive 2014 года. До 2019 года Insomniac была независимой частной компанией и создавала игры для Sony, Microsoft, Electronic Arts и Oculus. В 2019 году студия была приобретена Sony Interactive Entertainment, став частью SIE Worldwide Studios. Компания неоднократно называлась различными игровыми изданиями одним из лучших разработчиков видеоигр.'
#Приведение всех слов к нижнему регистру:
text = text.lower()
# Только так нашел способ убрать все знаки припинания
text_list = []
text_list.extend(text)
# print(text_list)
i = 0
while i < len(text_list):
    if not (text_list[i].isalnum() or text_list[i] == ' '):
        text_list.pop(i)
    else:
        i += 1
    
# Сборка строки:
text = ''.join(text_list)
slovar = set(text.split(' '))
lists = []
for i in slovar:
    lists.append([[text.count(i)], [i]])
    
# Сортировка
lists.sort(reverse=True)

print('10 самых используемых слов:')
for i in range(1, 11):
    print(f'{lists[i][0]} - {lists[i][1]}')