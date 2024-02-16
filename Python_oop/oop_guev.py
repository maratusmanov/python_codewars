# Реализуйте класс PiggyBank , а затем создайте экземпляр этого класса и
# присвойте его переменной money_box .
# Класс PiggyBank должен иметь:
# • атрибут content со значением 'coins'
# • атрибут alternate_name со значением 'penny bank

# class PiggyBank:
#     def __init__(self, content, alternate_name):
#         self._content = content
#         self._alternate_name = alternate_name
# money_box = PiggyBank("coins", "penny_bank")
# print(money_box)

# Реализуйте пустой класс PiggyBank , а затем создайте два экземпляра этого
# класса и присвойте их переменным money_box1 и money_box2 .
# Экземпляр money_box1 должен иметь:
# • атрибут coins со значением 10
# Экземпляр money_box2 должен иметь:
# • атрибут coins со значением 15
# • атрибут color со значением 'pink

# class PiggyBank:
#     pass
#
# money_box1 = PiggyBank()
# money_box2 = PiggyBank()
#
# money_box1.coins = 10
# money_box2.coins = 15
# money_box2.color = "pink"

# Реализуйте класс PiggyBank , а затем создайте экземпляр этого класса и
# присвойте его переменной money_box .
# Класс PiggyBank должен иметь:
# • атрибут content со значением 'coins'
# • атрибут alternate_name со значением 'penny bank'

# class PiggyBank:
#     content = 'coins'
#     alternate_name = 'penny bank'
#
# obj_piggy = PiggyBank()
# money_box = obj_piggy

# Реализуйте класс Gun , описывающий ружье. При создании экземпляра класс не
# должен принимать никаких аргументов.
# Класс Gun должен иметь один метод экземпляра:
# • shoot() — метод, при вызове которого выводится строка pif

# class Gun:
#     def shoot(self):
#         print("pif")

# Вам доступен класс User , описывающий интернет-пользователя. При создании
# экземпляра класс принимает один аргумент:
# • name — имя пользователя
# Экземпляр класса User имеет два атрибута:
# • name — имя пользователя
# • friends — количество друзей пользователя, начальным значением
# является 0
# Класс User имеет один метод экземпляра:
# • add_friends() — метод, принимающий в качестве аргумента целое
# число n и увеличивающий количество друзей пользователя на n
# Найдите и исправьте ошибки, допущенные при реализации
# метода add_friends()

# class User:
#     def __init__(self, name, friends = 0):
#         self._name = name
#         self._friends = friends
#     def add_friends(self, n):
#         self._friends += n

# Вам доступен класс House , описывающий дом. При создании экземпляра класс
# принимает два аргумента в следующем порядке:
# • color — цвет дома
# • rooms — количество комнат в доме
# Экземпляр данного класса имеет два атрибута:
# • color — цвет дома
# • rooms — количество комнат в доме
# Реализуйте для класса House два метода экземпляра:
# • paint() — метод, принимающий в качестве аргумента
# значение new_color и изменяющий текущий цвет дома на new_color
# • add_rooms() — метод, принимающий в качестве аргумента целое
# число n и увеличивающий количество комнат в доме на n

# class House:
#     def __init__(self, color, rooms):
#         self._color = color
#         self._rooms = rooms
#     def paint(self, new_color):
#         self._color = new_color
#     def add_rooms(self, n):
#         self._rooms += n

# Реализуйте класс Circle , описывающий круг. При создании экземпляра класс
# должен принимать один аргумент:
# • radius — радиус круга
# Экземпляр класса Circle должен иметь три атрибута:
# • radius — радиус круга
# • diameter — диаметр круга
# • area — площадь круга

# import math
#
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#         self._diameter = 2 * radius
#         self._area = math.pi * (radius ** 2)
#     def get_radius(self):
#         return self._radius
#     def get_diameter(self):
#         return self._diameter
#     def get_area(self):
#         return self._area
#
# my_circle = Circle(5)
# print("Радиус круга: ", my_circle.get_radius())
# print("Диаметр круга: ", my_circle.get_diameter())
# print("Площадь круга: ", my_circle.get_area())


# Реализуйте класс Bee , описывающий пчелку, которая перемещается по
# координатной плоскости в четырех направлениях: вверх, вниз, влево и вправо.
# При создании экземпляра класс должен принимать два аргумента в следующем
# порядке:
# • x — координата пчелки по оси �x, по умолчанию имеет значение 0
# • y — координата пчелки по оси �y, по умолчанию имеет значение 0
# Экземпляр класса Bee должен иметь два атрибута:
# • x — координата пчелки по оси �x
# • y — координата пчелки по оси �y
# Класс Bee должен иметь четыре метода экземпляра:
# • move_up() — метод, принимающий в качестве аргумента целое число n и
# увеличивающий координату пчелки по оси �y на n
# • move_down() — метод, принимающий в качестве аргумента целое
# число n и уменьшающий координату пчелки по оси �y на n
# • move_right() — метод, принимающий в качестве аргумента целое
# число n и увеличивающий координату пчелки по оси �x на n
# • move_left() — метод, принимающий в качестве аргумента целое
# число n и уменьшающий координату пчелки по оси �x на n

# class Bee:
#     def __init__(self, x = 0, y = 0):
#         self._x = x
#         self._y = y
#     def move_up(self, n):
#         self._y += n
#     def move_down(self, n):
#         self._y -= n
#     def move_right(self, n):
#         self._x += n
#     def move_left(self, n):
#         self._x -= n

# Реализуйте класс Gun , описывающий ружье. При создании экземпляра класс не
# должен принимать никаких аргументов.
# Класс Gun должен иметь один метод экземпляра:
# • shoot() — метод, при первом вызове которого выводится строка pif ,
# при втором — paf , при третьем — pif , при четвертом — paf , и так
# далее

# class Gun:
#     def __init__(self):
#         self.shots_fired = 0
#
#     def shoot(self):
#         if self.shots_fired % 2 == 0:
#             print("pif")
#         else:
#             print("paf")
#         self.shots_fired += 1

# Реализуйте класс Gun , описывающий ружье. При создании экземпляра класс не
# должен принимать никаких аргументов.
# Класс Gun должен иметь три метода экземпляра:
# • shoot() — метод, при первом вызове которого выводится строка pif ,
# при втором — paf , при третьем — pif , при четвертом — paf , и так
# далее
# • shots_count() — метод, возвращающий актуальное количество вызовов
# метода shoot()
# • shots_reset() — метод, сбрасывающий количество вызовов
# метода shoot() до нуля

# class Gun:
#     def __init__(self):
#         self.shoot_fired += 1
#     def shoot(self):
#         if self.shooot_fired % 2 == 0:
#             print("pif")
#         else:
#             print("paf")
#         self.shoot_fired += 1
#     def shots_count(self):
#         self.shoot_fired
#     def shots_reset(self):
#         self.shots_fired = 0

# Реализуйте класс Vector , описывающий вектор на плоскости. При создании
# экземпляра класс должен принимать два аргумента в следующем порядке:
# • x — координата вектора по оси x, по умолчанию имеет значение 0
# • y — координата вектора по оси y, по умолчанию имеет значение 0
# Экземпляр класса Vector должен иметь два атрибута:
# • x — координата вектора по оси x
# • y — координата вектора по оси y
# Класс Vector должен иметь один метод экземпляра:
# • abs() — метод, возвращающий модуль вектора

# class Vector:
#     def __init__(self, x = 0, y = 0):
#         self._x = x
#         self._y = y
#     def abs(self):
#         return sqrt(self.x**2 + self.y**2)

# Реализуйте класс Numbers , описывающий изначально пустой расширяемый
# набор целых чисел. При создании экземпляра класс не должен принимать
# никаких аргументов.
# Класс Numbers должен иметь три метода экземпляра:
# • add_number() — метод, принимающий в качестве аргумента целое число
# и добавляющий его в набор
# • get_even() — метод, возвращающий список всех четных чисел из набора
# • get_odd() — метод, возвращающий список всех нечетных чисел из
# набора

# class Numbers:
#     def __init__(self):
#         self._numbers = []
#     def add_number(self, n):
#         self._numbers.append(n)
#     def get_even(self):
#         sort_list = []
#         for i in range(len(self._numbers)):
#             if self._numbers[i] % 2 == 0:
#                 sort_list.append(self._numbers[i])
#         return sort_list
#     def get_add(self):
#         sort_list = []
#         for i in range(len(self._numbers)):
#             if self._numbers[i] % 2 != 0:
#                 sort_list.append(self._numbers[i])
#         return sort_list

# Будем называть словом любую последовательность из одной или более букв.
# Текстом будем считать набор слов, разделенных пробелами.
# Реализуйте класс TextHandler , описывающий изначально пустой расширяемый
# набор слов. При создании экземпляра класс не должен принимать никаких
# аргументов.
# Экземпляр класса TextHandler должен иметь три метода:
# • add_words() — метод, принимающий в качестве аргумента текст и
# добавляющий слова из данного текста в набор
# • get_shortest_words() — метод, возвращающий актуальный список
# самых коротких слов в наборе
# • get_longest_words() — метод, возвращающий актуальный список
# самых длинных слов в наборе

class TextHandler:
    def __init__(self):
        self.text_ = []

    def add_words(self, str_):
        self.text_.extend(str_.split())
        self.text_.sort(key=len)
        self.min_ = len(self.text_[0])
        self.max_ = len(self.text_[-1])

    def get_shortest_words(self):
        return [i for i in self.text_ if len(i) == self.min_]

    def get_longest_words(self):
        return [j for j in self.text_ if len(j) == self.max_]


handler = TextHandler()

handler.add_words("Hello world")
handler.add_words("Python is amazing")

shortest_words = handler.get_shortest_words()

print(shortest_words)

longest_words = handler.get_longest_words()

print(longest_words)