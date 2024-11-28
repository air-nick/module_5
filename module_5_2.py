class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Имя дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:  # Проверяем, существует ли этаж
            for floor in range(1, new_floor + 1):  # Проходим по этажам от 1 до new_floor
                print(floor)  # Выводим номер этажа
        else:
            print("Такого этажа не существует")  # Если этаж недопустим, выводим сообщение

    def __len__(self):
        # Возвращает количество этажей здания
        return self.number_of_floors

    def __str__(self):
        # Возвращает строку с описанием здания
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Демонстрация работы __str__
print(h1)  # Ожидаемый вывод: "Название: ЖК Эльбрус, кол-во этажей: 10"
print(h2)  # Ожидаемый вывод: "Название: ЖК Акация, кол-во этажей: 20"

# Демонстрация работы __len__
print(len(h1))  # Ожидаемый вывод: 10
print(len(h2))  # Ожидаемый вывод: 20
