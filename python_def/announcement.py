from datetime import datetime

def greet():
    print("Приветствуем наших новых сотрудников!")


def first_day():
    return datetime.today().strftime('%d.%m.%Y')


# def announcement():
#     print(happy_birthday('Анна Юрьева'))

def announcement():
    print(f"Всем привет! {first_day()} у нас вышли новые сотрудники.")
    print(new_person("Анна Юрьева", 29, "менеджер по продажам"))
    print(new_person("Олег Симонов", 34, "инженер связи", "бильярд"))
    print(new_person("Дарья Герасимова", 41, "секретарь", "вязание"))
    greet()


def happy_birthday(name: str) -> str:
    return f'Поздравляем тебя, {name}, с днем рождения!'


def new_person(name: str, age: int, position: str, hobby= "танцы") -> str:
    return f'{name}, {age} {age_word(age)}, позиция - {position.capitalize()}. Хобби - {hobby}'


def age_word(age: int) -> str:
    if age % 10 == 1:
        return "год"
    elif age % 10 in (2, 3, 4):
        return "года"
    elif age % 10 in (0, 5, 6, 7, 8, 9):
        return "лет"


announcement()