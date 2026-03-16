# 4 задание

class Bottle:
    material: str = 'Пластик'
    volume: float = 1.5
    
    # конструктор класса
    def __init__(self, title: str = 'Без названия', color: str = 'Прозрачная', fullness: int = 0, 
                 stopper: bool = True, fill: str = 'Пусто') -> None:
        self.title = title
        self.fill = fill
        self.color = color
        self.fullness = fullness
        self.stopper = stopper
        
    # переопределение метода удаления
    def __del__ (self):
        print("Бутылка выброшена...")
        
    # налить жидкость в бутылку
    def pour(self) -> None:
        if self.fill == 'Пусто':
            print(f"Что вы хотите налить в бутылку?")
            self.choice_fill()
        if self.fullness == 100:
            print("Бутылка уже полная!")
        else: 
            print(f"Бутылка полна жидкостью {self.fill} на {self.fullness}%")
            percent = int(input("Сколько процентов долить? "))
            if percent < 0:
                print("Вы не можете долить отрицательное значение!")
            elif percent + self.fullness > 100:
                self.fullness = 100
                print(f"Бутылка полна жидкостью {self.fill} на {self.fullness}%. Даже немного вылилось...")
            else:
                self.fullness = self.fullness + percent
                print(f"Бутылка полна жидкостью {self.fill} на {self.fullness}%.")
                
    # отлить жидкость из бутылки
    def pour_out(self) -> None:
        if self.fullness == 0:
            print("Бутылка и так пуста!")
        else: 
            print(f"Бутылка полна жидкостью {self.fill} на {self.fullness}%")
            percent = int(input("Сколько процентов вылить? "))
            if percent < 0:
                print("Вы не можете вылить отрицательное значение!")
            elif self.fullness - percent < 0:
                self.fullness = 0
                self.fill = 'Пусто'
                print(f"Вы вылили всю жикость. Кажется вы переоценили налитый объём...")
            elif self.fullness - percent == 0:
                self.fullness = 0
                self.fill = 'Пусто'
                print(f"Вы вылили всю жикость.")
            else:
                self.fullness = self.fullness - percent
                print(f"Бутылка полна жидкостью {self.fill} на {self.fullness}%.")
    
    # ввод наливаемой жидкости
    def choice_fill(self) -> None:
        self.fill = input()
        
    # подбросить бутылку и попытаться установить ровно
    def flip(self) -> None:
        print("Вы подбросили бутылку...")
        if self.stopper == False and self.fullness > 0:
            print("Ой. Кажется из бутылки вылилась вся жидкость... Стоило закрутить крышку")
            self.fullness = 0
            self.fill = 'Пусто'
        elif self.fullness == 0:
            print("Бутылка слишком лёгкая и её сносит ветром.")
        else:
            print("Если бы тут была библиотека random, то у вас был бы шанс, но сейчас бутылка заваливается на бок(")
           
    # закрутить крышку 
    def twist(self) -> None:
        if self.stopper == True:
            print("Крышка уже закручена!")
        else:
            self.stopper = True
            print("Вы закрутили крышку.")
      
    # открутить крышку
    def not_twist(self) -> None:
        if self.stopper == False:
            print("Крышка уже откручена!")
        else:
            self.stopper = False
            print("Вы открутили крышку.")

bottle = Bottle("Черноголовка")
print(f"Вы нашли бутылку {bottle.title} цвета {bottle.color}.\n")

print("""1. Налить жидкость в бутылку
2. Вылить жидкость из бутылки
3. Открутить крышку
4. Закрутить крышку
5. Подбросить бутылку
exit - Выбросить бутылку""")

while True:
    try:
        print("-------------")
        command = input("Введите команду: ")
        if command == '1':
            bottle.pour()
        elif command == '2':
            bottle.pour_out()
        elif command == '3':
            bottle.twist()
        elif command == '4':
            bottle.not_twist()
        elif command == '5':
            bottle.flip()
        elif command == 'exit':
            break
        else:
            print("Команда введена неккоректно или отсутствует.")
        
    except (ValueError, TypeError) as e:
        print(e)
            