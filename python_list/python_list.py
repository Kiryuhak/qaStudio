list1 = ['lorem', 'ipsum', 'dolor', 'sit', 'amet']
list2 = [356, 'lorem', True, 'ipsum', 23.9]

print(list1[0])
print(list1[4])
print(len(list1)) # Кол-во индекса
print(len(list1)-1) # Обратиться к 4 элементу
print(len(list1[:2]))
print(len(list1[1:4]), '\n')

backpack = []
print('Сумка пуста', backpack)

backpack = ["верёвка", "фонарь", "нож"]
print(backpack)

backpack.append("карта")
print('Добавили карту', backpack)

print(backpack.index("фонарь"))
backpack.insert(1, "компас")

backpack.remove("фонарь")
print('Удалили фонарь',backpack)

print('Индекс 3: ', backpack[3]) # "карта"

while len(backpack) > 0:
    backpack.pop()
    print(backpack)