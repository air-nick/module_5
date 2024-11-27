class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка на корректность номера этажа
        if 1 <= new_floor <= self.number_of_floors:
            # Вывод номеров этажей от 1 до new_floor
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            # Сообщение о несуществующем этаже
            print("Такого этажа не существует")

# Создаем объекты класса House
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызываем метод go_to
h1.go_to(5)  # Ожидаемый результат: 1, 2, 3, 4, 5
h2.go_to(10)  # Ожидаемый результат: "Такого этажа не существует"
