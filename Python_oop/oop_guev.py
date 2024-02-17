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
#
# class TextHandler:
#     def __init__(self):
#         self.text_ = []
#
#     def add_words(self, str_):
#         self.text_.extend(str_.split())
#         self.text_.sort(key=len)
#         self.min_ = len(self.text_[0])
#         self.max_ = len(self.text_[-1])
#
#     def get_shortest_words(self):
#         return [i for i in self.text_ if len(i) == self.min_]
#
#     def get_longest_words(self):
#         return [j for j in self.text_ if len(j) == self.max_]
#
#
# handler = TextHandler()
#
# handler.add_words("Hello world")
# handler.add_words("Python is amazing")
#
# shortest_words = handler.get_shortest_words()
#
# print(shortest_words)
#
# longest_words = handler.get_longest_words()
#
# print(longest_words)

# Реализуйте класс Todo , описывающий список дел. При создании экземпляра
# класс не должен принимать никаких аргументов.
# Экземпляр класса Todo должен иметь один атрибут:
# • things — изначально пустой список дел, которые нужно выполнить
# Класс Todo должен иметь четыре метода экземпляра:
# • add() — метод, принимающий название дела и его приоритет (целое
# число) и добавляющий данное дело в список дел в виде кортежа:
# (<название дела>, <приоритет>)
# • get_by_priority() — метод, принимающий в качестве аргумента целое
# число n и возвращающий список названий дел, имеющих приоритет n
# • get_low_priority() — метод, возвращающий список названий дел,
# имеющих самый низкий приоритет
# • get_high_priority() — метод, возвращающий список названий дел,
# имеющих самый высокий приоритет

# class Todo:
#     def __init__(self):
#         self._things = []
#     def add(self, thing, priority):
#         self._things.append((thing, priority))
#     def get_by_priority(self, n):
#         list_priority = []
#         for tuple in self._things:
#             if tuple[1] == n:
#                 list_priority.append(tuple[0])
#         return list_priority
#     def get_low_priority(self):
#         list_tuple_1 = []
#         for i in range(len(self._things)):
#             list_tuple_1.append(self._things[i][1])
#
#         list_low_tuple_0 = []
#         low_priority = min(list_tuple_1)
#         for tuple in self._things:
#             if tuple[1] == low_priority:
#                 list_low_tuple_0.append(tuple[0])
#         return list_low_tuple_0
#     def get_hight_priority(self):
#         list_tuple_1 = []
#         for i in range(len(self._things)):
#             list_tuple_1.append(self._things[i][1])
#
#         list_hight_tuple_0 = []
#         hight_priority = max(list_tuple_1)
#         for tuple in self._things:
#             if tuple[1] == hight_priority:
#                 list_hight_tuple_0.append(tuple[0])
#         return list_hight_tuple_0
#
#     def get_things_priority(self):
#         return self._things

# Реализуйте класс Postman , описывающий почтальона. При создании экземпляра
# класс не должен принимать никаких аргументов.
# Экземпляр класса Postman должен иметь один атрибут:
# • delivery_data — изначально пустой список адресов, по которым следует
# доставить письма
# Экземпляр класса Postman должен иметь три метода экземпляра:
# • add_delivery() — метод, принимающий в качестве аргументов улицу,
# дом и квартиру, и добавляющий в список адресов эти данные в виде
# кортежа:
# (<улица>, <дом>, <квартира>)
# • get_houses_for_street() — метод, принимающий в качестве аргумента
# улицу и возвращающий список всех домов на этой улице, в которые
# требуется доставить письма
# • get_flats_for_house() — метод, принимающий в качестве
# аргументов улицу и дом и возвращающий список всех квартир в этом
# доме, в которые требуется доставить письма

# class Postman:
#     def __init__(self):
#         self._delivery_data = []
#     def add_delivery(self, street, house, apartment):
#         self._delivery_data.append((street, house, apartment))
#     def get_houses_for_house(self, desired_street):
#         result_list = []
#         for tuple in self._delivery_data:
#             street = tuple[0]
#             house = tuple[1]
#             if street == desired_street:
#                 result_list.append(house)
#         return result_list
#     def get_flats_for_house(self, desired_street, desired_house):
#         result_list = []
#         for delivery in self._delivery_data:
#             street, house, apartment = delivery
#             if street == desired_street and house == desired_house:
#                 result_list.append(apartment)
#         return result_list


# Будем называть словом любую последовательность из одной или более
# латинских букв.
# Реализуйте класс Wordplay , описывающий расширяемый набор слов. При
# создании экземпляра класс должен принимать один аргумент:
# • words — список, определяющий начальный набор слов. Если не передан,
# начальный набор слов считается пустым
# Экземпляр класса Wordplay должен иметь один атрибут:
# • words — список, содержащий набор слов
# Класс Wordplay должен иметь четыре метода экземпляра:
# • add_word() — метод, принимающий в качестве аргумента слово и
# добавляющий его в набор. Если слово уже есть в наборе, метод ничего не
# должен делать
# • words_with_length() — метод, принимающий в качестве аргумента
# натуральное число n и возвращающий список слов из набора, длина
# которых равна n
# • only() — метод, принимающий произвольное количество
# аргументов — букв, и возвращающий все слова из набора, которые
# включают в себя только переданные буквы
# • avoid() — метод, принимающий произвольное количество
# аргументов — букв, и возвращающий все слова из списка words , которые
# не содержат ни одну из этих букв

# class Wordplay:
#     def __init__(self, words = None):
#         if words:
#             self._words = words
#         else:
#             self._words = []
#     def add_words(self, word):
#         if word not in self._words:
#             self._words.append(word)
#     def words_with_length(self, n):
#         total_list = []
#         for word in self._words:
#             if len(word) == n:
#                 total_list.append(word)
#         return total_list
#     def only(self, *args):
#         result_list = []
#         for word in self._words:
#             if set(args).issubset(set(word)):
#                 result_list.append(word)
#         return result_list
#     def avoid(self, *args):
#       result_list = []
#       for word in self._words:
#           if set(word).difference(args) == set(word):
#               result_list.append(word)
#       return result_list


# Реализуйте класс Knight , описывающий шахматного коня. При создании
# экземпляра класс должен принимать три аргумента в следующем порядке:
# • horizontal — координата коня по горизонтали,
# представленная латинской буквой от a до h
# • vertical — координата коня по
# вертикали, представленная целым числом от 1 до 8 включительно
# • color — цвет коня ( black или white )
# Экземпляр класса Knight должен иметь три атрибута:
# • horizontal — координата коня на шахматной доске по горизонтали
# • vertical — координата коня на шахматной доске по вертикали
# • color — цвет коня
# Класс Knight должен иметь четыре метода экземпляра:
# • get_char() — метод, возвращающий символ N
# • can_move() — метод, принимающий в качестве аргументов
# координаты клетки по горизонтали и по вертикали, и
# возвращающий True , если конь может переместиться на клетку с
# данными координатами, или False в противном случае
# • move_to() — метод, принимающий в качестве аргументов
# координаты клетки по горизонтали и по вертикали и заменяющий
# текущие координаты коня на переданные. Если конь из текущей клетки не
# может переместиться на клетку с указанными координатами, его
# координаты должны остаться неизменными
# • draw_board() — метод, печатающий шахматное поле, отмечающий на
# этом поле коня и клетки, на которые может переместиться конь. Пустые
# клетки должны быть отображены символом . , конь — символом N ,
# клетки, на которые может переместиться конь, — символом *

class Knight:
    pass