t1 = (1, 2, 3)
print(t1, '\n')

t2 = (1, 'hello', [2, 3, 4])
print(t2, '\n')
print(t2[0]) # 1
print(t2[1]) # hello
print(t2[2][1]) # 3

t3 = ('apple', 340, True, 40.2, [23, 16, 33])
print(t3, '\n')
print(t3[0:3]) # ('apple', 340, True)
print(t3[::-1])  # ([23, 16, 33], 40.2, True, 340, 'apple')
print(t3[2::], '\n') # (True, 40.2, [23, 16, 33])

colors = ('red', 'green', 'blue', 'yellow', 'white')

for i, color in enumerate(colors):
    print(f'{i+1}. {color}')

t4 = (4, 5, 6, 2, 6, 1, 3, 7)
print(t4)
print(t4.count(6)) # Сколько раз встречается 6ка

list1 = [1, 2, 3]
list1.append(4)
print(list1, '\n')
print(t1)
print(t2)
t2[2].append(5)
print(t2, '\n')

print(t4)
print(id(t4))
t4 = t4 + (9, )
print(t4, '\n')
print(id(t4))

import sys
print(sys.getsizeof(list1))
print(sys.getsizeof(t1))



