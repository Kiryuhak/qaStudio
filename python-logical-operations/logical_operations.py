# Операторы сравнения в Python
#  Оператор равно "=="
x = 10
y = 10
print("x == y ->", x == y)

#  Оператор не равно "!="
x = 10
y = 10
value = x != y
print("x != y ->", value)

#  Оператор больше чем ">"
x = 10
y = 5
value = x > y
print("x > y ->", value)

#  Оператор меньше чем "<"
x = 10
y = 5
value = x < y
print("x < y ->", value)

# Оператор больше чем или равно ">="
x = 5
y = 5
value = x >= y
print("x >= y ->", value, '\n')

# -----------------------
# Операторы тождественности 'is' -> возвращает true если переменные являются одним объектом
x = 5
y = 5
print('x is y ->', x is y)
print(id(x))
print(id(y))

a = 'Bob'
b = 'Bob'
print('a is b ->', a is b)
print(id(a))
print(id(b), '\n')

# Операторы тождественности 'is not' -> возвращает true если переменные разные
x = 10
y = 10
print('x is not y ->', x is not y, '\n')

# ---------------------------------------------------------
# Логические операторы в Python
x = 4
# Конъюнкция
#  Оператор логическое и "and" -> возвращает значение True если оба утверждения верны

print("x < 5 and x < 10 ->", x < 5 and x < 10)
# True and True # 1 and 1 # True

x = 6
print("x < 5 and x < 10 ->", x < 5 and x < 10)
# False and True # 0 and 1 # False

x = 11
print("x < 5 and x < 10 ->", x < 5 and x < 10)
# False and False # 0 and 0 # Flase

