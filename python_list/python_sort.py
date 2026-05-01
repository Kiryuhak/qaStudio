list1 = ['lorem', 'ipsum', 'dolor', 'sit', 'amet']
print(list1)
list1.sort() # Сортировка по алфавиту
print('Отсортированный лист', list1)

list1.sort(reverse=True) # Поменяли сортировку
print('Поменяли сортировку', list1, '\n')


list2 = [213, 24, 5, 632, 5223.3, 52.3, 23.1]
print(list2)
list2.sort() # Сортировка по алфавиту
print('Отсортированный лист', list2)

list2.sort(reverse=True) # Поменяли сортировку
print('Поменяли сортировку', list2, '\n')

numbers = [x for x in range(5)]
print(numbers, '\n')

squares = [x**2 for x in range(5)]
print(squares, '\n')

list_a = [1, 2, 3, 4, 5]
list_b = list_a
print(list_b, '\n')

list_b.append(4)
print(list_b, '\n')
print(list_a, '\n')

