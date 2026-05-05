set1 = set()
print(set1)

set2 = {1, 2, 3, 4, 5, 6, 7, 8}
print(set2,  '\n')

set3 = set('hello')
print(set3, '\n')

# print(set3[4]) # Ошибка

#set1.add(1, 2, 3, 4, 6) # set.add() takes exactly one argument (5 given)
set1.add(1)
set1.add(2)
set1.add(3)
set1.add(4)
set1.add(6)
set1.add(1) # Дубли не показывает
print(set1, '\n')

set1.remove(1)
print(set1, '\n')

set1.discard(3)
print(set1, '\n')

set1.discard(4444) # Ошибку не выводит не существующий число
print(set1, '\n')

set4 = {1, True, 'spring', 34.7, 'summer', 299, False} # {False, 1, 34.7, 'spring', 299, 'summer'}
print(set4, '\n')


set4.add(4000.20)
set4.add('e')
set4.add('&')
set4.add(-22231.4)
print(set4, '\n')

set4.pop()
set4.pop()
set4.pop()
print(set4, '\n') # Удаляет

set4.clear()
print(set4, '\n')

set3.clear()
set2.clear()
set1.clear()
print(set1, set2, set3, set4, '\n')

set1.add(1)
set1.add(2)
set1.add(3)
set1.add(4)
set1.add(7)
set1.add(6)
set2.add(7)
set2.add(4)
set2.add(11)
print(set1, '\n')
print(set2, '\n')

print(set1 & set2, '\n')
print(set1 | set2, '\n')

print(set1.intersection(set2))
print(set1.union(set2))

print(set1 ^ set2)
set1.symmetric_difference(set2)
print(set1, '\n')

print(set1 - set2)

set1.difference(set2)
print(set1, '\n')
set2.symmetric_difference(set1)
print(set2, '\n')


