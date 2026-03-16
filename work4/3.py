# 3 задание

def text_to_file(filename, text):
    # запись в файл
    # контекстный менеджер автоматически закрывает файл в отличии от обычного open/close
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text + '\n')

    # чтение из файла 
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.readlines()
        
    print("\nВывод чётных строк: ")
    for i, line in enumerate(text, 1): # начинаем индексацию с 1
        if i % 2 == 0:
            print(f"{i}. {line}", end = '')
    
filename = input("Введите название текстового файла с расширением txt: ")
text = input("Введите текст, который хотите добавить в файл: ")
text_to_file(filename, text)