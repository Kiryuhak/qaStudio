# Text Type: str
text = 'Hello World'
print('String: ', text, 'Type: ', type(text), '\n')

name = 'Bob'
print(name, type(name))

name = name + '25' # Bob25
print(name, type(name))

# ----------
# Numeric Types: int, float, complex
integer = 42
floating_point = 3.14
complex_number = 1 + 2j

print('Integer: ', integer, 'Type: ', type(integer))
print('Float: ', floating_point, 'Type: ', type(floating_point))
print('Complex: ', complex_number, 'Type: ', type(complex_number), '\n')

a = 5000
a = a + 6000 # 11000

print("a =", a)

number = '50'
number_2 = 100

result = int(number) + number_2
print(f"result = {result}")

# Sequence Types: list, tuple, range
# List

# List
numbers = list()
empty_list = []

my_list = [1, 2, 3, 4, 5]
print('List:', empty_list, 'Type:', type(empty_list))
print('List:', my_list, 'Type:', type(my_list))

my_new_list = [0,1, True, False, [1,2,3], "Bob"]
print(f"my_new_list = {my_new_list}", "\n")

my_list[0] = "Bob"
print('List:', my_list, 'Type:', type(my_list))

my_list.append("Max")
print('List:', my_list, 'Type:', type(my_list), '\n')


# Tuple
my_tuple = (1, 2, 3,)
print('Tuple:', my_tuple, 'Type:', type(my_tuple))

my_tuple = (1, True, 'Max')
print('Tuple:', my_tuple, 'Type:', type(my_tuple))

my_tuple = my_tuple + (4,5,6,)
print('Tuple:', my_tuple, 'Type:', type(my_tuple), '\n')

# Range
my_range = range(5) # 0 to 4
print('Range:', list(my_range), 'Type:', type(my_range))  # Преобразуем в список для отображения

new_range = range(1,5)
print('Range:', list(new_range), 'Type:', type(new_range))

second_range = range(1,5,2)
print('Range:', list(second_range), 'Type:', type(second_range))
# -----------------------------------------------------------------------------------------
