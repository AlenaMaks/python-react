# 3 задание
from faker import Faker
from string import ascii_letters, digits, punctuation
from random import randint, choices
from json import dump, load

chars = ascii_letters + digits + punctuation

name = Faker().name() # для генерации нормальных имён

information = {
    "name": name, 
    "age": randint(18, 90),
    "email": name.split()[0].lower()+'.'+name.split()[1].lower()+'@mail.com',
    "password": ''.join(choices(chars, k = 12))
}

filename = input('Введите имя файла для сохранения json: ')

with open(filename, 'w') as file:
    dump(information, file)
    
with open(filename, 'r') as file:
    result = load(file)
    
print(result, type(result))