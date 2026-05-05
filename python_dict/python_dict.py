dict1 = {'name': "John", 'city': 'Montreal', 'age': 34}
dict2 = dict(name='John', city='Montreal', age=34)
keys = ['name', 'city', 'age']
values = ['John', 'Montreal', 34]
print(values, '\n')

dict3 = dict(zip(keys, values))
print(dict3, '\n')

keys.append('address')
print(keys, '\n')

dict4 = dict(zip(keys, values))
print(dict4, '\n')

dict5 = {(1, 2, 3): 'value'}
print(dict5, '\n')


library = [
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "genre": "Fantasy"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Classic"},
    {"title": "Dune", "author": "Frank Herbert", "year": 1965, "genre": "Science Fiction"}
]

print(library[2], '\n')

book = library[0]
for key in book:
    print(key)

for value in book.values():
    print(value)

for key, value in book.items():
    print(f'{key}: {value}')

print(dict1, '\n')
print(dict1['city'], '\n')

for i, key in enumerate(dict4):
    print(f'{i+1}. {key}: {dict4[key]}')

print(book, '\n')
book['color'] = 'green'
print(book, '\n')

book.update(dict1)
print(book, '\n')

book.setdefault('pages', 450)
print(book, '\n')

book.setdefault('color', 'red')
print(book, '\n')

book.pop('city')
book.pop('age')
book.pop('name')
print(book, '\n')

print(book.popitem())

dict4.clear()
print(dict4, '\n')

book['details'] = {
    'pages': 382,
    'publisher': 'New Your Book',
    'parts': {
        "book1": 'The Hobbit',
        "book2": 'The Hobbit 2'
    }
}

print(book, '\n')

dict4.clear()
print(dict4, '\n')

dict4 = book.copy()
print(dict4, '\n')

import copy

dict6 = copy.deepcopy(book)
print(dict6, '\n')

dict7 = dict(sorted(dict6.items()))
print(dict7, '\n')

dict8 = {i: i**2 for i in range(1, 11)}
print(dict8, '\n')

fruits = [('apple', 378), ('banana', 100), ('kiwi', 292)]
print(fruits, '\n')

dict9 = {key: value for key, value in fruits}
print(dict9, '\n')

dict10 = {i: i**2 for i in range(20, 40) if i % 2 == 0}
print(dict10, '\n')