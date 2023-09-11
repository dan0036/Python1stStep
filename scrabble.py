
scrableDict = dict.fromkeys(['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r', 'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'], 1)
scrableDict.update(dict.fromkeys(['d', 'g', 'д', 'к', 'л', 'м', 'п', 'у'], 2))
scrableDict.update(dict.fromkeys(['b', 'c', 'm', 'p', 'б', 'г', 'ё', 'ь', 'я'], 3))
scrableDict.update(dict.fromkeys(['f', 'h', 'v', 'w', 'y', 'й', 'ы'], 4))

# fivePoints = ['KЖЗХЦЧ']
# scrableDict.update(dict.fromkeys([i for i in fivePoints], 5))

scrableDict.update(dict.fromkeys(['k', 'ж', 'з', 'х', 'ц', 'ч'], 5))
scrableDict.update(dict.fromkeys(['j', 'x', 'ш', 'ю', 'э'], 8))
scrableDict.update(dict.fromkeys(['q', 'z', 'ф', 'щ', 'ъ'], 10))

print(scrableDict)

k = list(input('Введите слово строчными буквами: '))
sum = 0
for i in k:
    sum += scrableDict[i]

print(f'Стоимость слова: {sum}')
