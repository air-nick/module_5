class House:
    houses_history = []  # Список для хранения истории построек

    def __new__(cls, *args, **kwargs):
        # Создание нового объекта
        instance = super().__new__(cls)
        # Добавление названия объекта в историю
        if len(args) > 0:  # Проверяем, что передано название
            cls.houses_history.append(args[0])  # args[0] — название здания
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name  # Имя дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def __del__(self):
        # Сообщение при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")

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

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        elif isinstance(value, House):
            return House(
                f"{self.name} + {value.name}",
                self.number_of_floors + value.number_of_floors,
            )
        raise TypeError("Можно добавлять только целые числа или объекты House")

    def __radd__(self, value):
        return self + value

    def __iadd__(self, value):
        return self + value


# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2
del h3

# История остаётся неизменной
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление оставшегося объекта
del h1
