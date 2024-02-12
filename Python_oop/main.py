class Shape:
    def __init__(self, name):
        self.name = name

    # Атрибут объекта
    def set_name(self, name):
        self.name = name

    # Атрибут класса
    counter = 0

    # Метод экземпляра класса
    def describe(self):
        return f"This is a {self.name}."

    # Метод __init__
    @classmethod
    def create_shape(cls, name):
        return cls(name)

    # Модификаторы доступа (getter и setter)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Геттер
    def get_name(self):
        return self.name

    # Сеттер
    def set_counter(cls, value):
        cls.counter = value

    # Статический метод
    @staticmethod
    def print_info():
        return "This is a Shape class."

    # Метод класса
    @classmethod
    def get_counter(cls):
        return cls.counter

# Создание экземпляра класса Shape
my_shape = Shape("triangle")

# Установка нового значения атрибута
my_shape.set_name("circle")

# Получение значения атрибута
print(my_shape.get_name())

# Вызов метода экземпляра класса
print(my_shape.describe())

# Вызов статического метода
print(Shape.print_info())

# Создание объекта через метод класса
another_shape = Shape.create_shape("rectangle")

# Изменение атрибута класса
Shape.set_counter(5)

# Получение значения атрибута класса
print(Shape.get_counter())
