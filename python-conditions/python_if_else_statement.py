# if

number = -1
print('Введенное число: ', number)

if number < 0:
    print('Число отрицательное', '\n')
else:
    print('Число положительное', '\n')

# if else
age = 22
print('Введенное число: ', age)

if age < 18:
    print('Вы не допущены к вождению ТС')
else:
    print('Вы допущены к вождению ТС')

print('Проверка завершена', '\n')

#-------------------
number = 5
if number < 0:
    print('Число отрицательное')

number = 5
if number < 0:
    print('Число отрицательное')
elif number > 0:
    print('Число положительное')

number = 5
if number < 0:
    print('Число отрицательное')
elif number > 0:
    print('Число положительное', '\n')
else:
    print('Это число ноль')

# if elif else
person_type = None
age = 19
print('Введенное число:', age)

if age < 7:
    print('Вы посещаете детский садик.')
    person_type = 'ребенок'
elif 7 <= age < 18:
    print('Вы посещаете школу.')
    person_type = 'школьник'
else:
    print('Вы посещаете университет.')
    person_type = 'студент'

print(f'Вы {person_type} и вам {age} лет !')

# ---------------------------
age = input("Введите число больше нуля: ")

if age.isnumeric():
    age = int(age)
else:
    print('Вы ввели некорректное число')

print('Число', age, 'Тип', type(age))