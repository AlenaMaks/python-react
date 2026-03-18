# 1 задание
from random import choice
from pathlib import Path

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
lst_filenames = []
for name in range(10):
    filename = ''
    for i in range(8):
        chr = choice(chars)
        filename += chr
    filename += '.txt'
    lst_filenames.append(filename)
print(lst_filenames)

directory = Path(input('Введите название директории: ')) # Path преобразовывает в <class 'pathlib.WindowsPath'>
directory.mkdir(exist_ok=True) # если папка уже есть, не будет ошибки

for filename in lst_filenames:
    full_path = directory / filename
    full_path.touch()
    print(full_path.absolute())