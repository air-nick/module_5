class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Имя дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    # Сравнение объектов по количеству этажей
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    # Арифметические операции
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        raise TypeError("Можно добавлять только целые числа")

    def __radd__(self, value):
        return self + value  # Используем уже реализованный __add__

    def __iadd__(self, value):
        return self + value  # Используем уже реализованный __add__


# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Демонстрация методов __str__
print(h1)  # Ожидаемый вывод: "Название: ЖК Эльбрус, кол-во этажей: 10"
print(h2)  # Ожидаемый вывод: "Название: ЖК Акация, кол-во этажей: 20"

# Демонстрация метода __eq__
print(h1 == h2)  # Ожидаемый вывод: False

# Демонстрация метода __add__
h1 = h1 + 10
print(h1)  # Ожидаемый вывод: "Название: ЖК Эльбрус, кол-во этажей: 20"
print(h1 == h2)  # Ожидаемый вывод: True

# Демонстрация метода __iadd__
h1 += 10
print(h1)  # Ожидаемый вывод: "Название: ЖК Эльбрус, кол-во этажей: 30"

# Демонстрация метода __radd__
h2 = 10 + h2
print(h2)  # Ожидаемый вывод: "Название: ЖК Акация, кол-во этажей: 30"

# Сравнение этажей (методы __gt__, __ge__, __lt__, __le__, __ne__)
print(h1 > h2)   # Ожидаемый вывод: False
print(h1 >= h2)  # Ожидаемый вывод: True
print(h1 < h2)   # Ожидаемый вывод: False
print(h1 <= h2)  # Ожидаемый вывод: True
print(h1 != h2)  # Ожидаемый вывод: False
