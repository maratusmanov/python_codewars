#Todo : методы экземпляра класса =>
import datetime


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

# Реализуйте класс Todo3 , описывающий список дел. При создании экземпляра
# класс не должен принимать никаких аргументов.
# Экземпляр класса Todo3 должен иметь один атрибут:
# • things — изначально пустой список дел, которые нужно выполнить
# Класс Todo3 должен иметь четыре метода экземпляра:
# • add() — метод, принимающий название дела и его приоритет (целое
# число) и добавляющий данное дело в список дел в виде кортежа:
# (<название дела>, <приоритет>)
# • get_by_priority() — метод, принимающий в качестве аргумента целое
# число n и возвращающий список названий дел, имеющих приоритет n
# • get_low_priority() — метод, возвращающий список названий дел,
# имеющих самый низкий приоритет
# • get_high_priority() — метод, возвращающий список названий дел,
# имеющих самый высокий приоритет

# class Todo3:
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

# class Knight:
#     pass

#Todo : модификаторы доступа =>

# Класс Circle
# Реализуйте класс Circle , описывающий круг. При создании экземпляра класс
# должен принимать один аргумент:
# • radius — радиус круга
# Экземпляр класса Circle должен иметь три атрибута:
# • _radius — радиус круга
# • _diameter — диаметр круга
# • _area — площадь круга
# Класс Circle должен иметь три метода экземпляра:
# • get_radius() — метод, возвращающий радиус круга
# • get_diameter() — метод, возвращающий диаметр круга
# • get_area() — метод, возвращающий площадь круга

# import math
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#         self._diameter = radius * 2
#         self._area = math.pi * radius ** 2
#     def get_radius(self):
#         return self._radius
#     def get_diameter(self):
#         return self._diameter
#     def get_area(self):
#         return self._area


# Реализуйте класс BankAccount , описывающий банковский счет. При создании
# экземпляра класс должен принимать один аргумент:
# • balance — баланс счета, по умолчанию имеет значение 0
# Экземпляр класса BankAccount должен иметь один атрибут:
# • _balance — баланс счета
# Класс BankAccount должен иметь четыре метода экземпляра:
# • get_balance() — метод, возвращающий актуальный баланс счета
# • deposit() — метод, принимающий в качестве аргумента число amount и
# увеличивающий баланс счета на amount
# • withdraw() — метод, принимающий в качестве аргумента
# число amount и уменьшающий баланс счета
# на amount . Если amount превышает количество средств на балансе счета,
# должно быть возбуждено исключение ValueError с сообщением:
# На счете недостаточно средств
# • transfer() — метод, принимающий в качестве аргументов банковский
# счет account и число amount . Метод должен уменьшать баланс текущего
# счета на amount и увеличивать баланс
# счета account на amount . Если amount превышает количество средств
# на балансе текущего счета, должно
# быть возбуждено исключение ValueError с сообщением:
# На счете недостаточно средств

# class BankAccount:
#     def __init__(self, balance = 0):
#         self._balance = balance
#     def get_balance(self):
#         return self._balance
#     def deposit(self, amount):
#         self._balance += amount
#     def withdraw(self, amount):
#         if self._balance - amount < 0:
#             raise ValueError('На счете недостаточно средств')
#         else:
#             self._balance -= amount
#     def transfer(self, account, amount):
#         if amount > account.get_balance():
#             raise ValueError('На счете недостаточно средств')
#         else:
#             self.withdraw(amount)
#             account.deposit(amount)
#


# Реализуйте класс User , описывающий интернет-пользователя. При создании
# экземпляра класс должен принимать два аргумента в следующем порядке:
# • name — имя пользователя. Если name не является непустой строкой,
# состоящей только из букв, должно быть возбуждено
# исключение ValueError с текстом:
# Некорректное имя
# • age — возраст пользователя. Если age не является целым числом,
# принадлежащим отрезку [0; 110] , должно быть
# возбуждено исключение ValueError с текстом:
# Некорректный возраст
# Экземпляр класса User должен иметь два атрибута:
# • _name — имя пользователя
# • _age — возраст пользователя
# Класс User должен иметь четыре метода экземпляра:
# • get_name() — метод, возвращающий имя пользователя
# • set_name() — метод, принимающий в качестве аргумента
# значение new_name и изменяющий имя пользователя на new_name .
# Если new_name не является непустой строкой, состоящей только из букв,
# должно быть возбуждено исключение ValueError с текстом:
# Некорректное имя
# • get_age() — метод, возвращающий возраст пользователя
# • set_age() — метод, принимающий в качестве аргумента
# значение new_age и изменяющий возраст пользователя на new_age .
# Если new_age не является целым числом, принадлежащим отрезку [0;
# 110] , должно быть возбуждено исключение ValueError с текстом:
# Некорректный возраст

# class User:
#     def __init__(self, name, age):
#         if name == "":
#             raise ValueError("Некорректное имя")
#         if not isinstance(age, int):
#             raise ValueError("Некорректный возраст")
#         if not (0 <= age <= 100):
#             raise ValueError("Некорректный возраст")
#         self._name = name
#         self._age = age
#     def get_name(self):
#         return self._name
#     def get_age(self):
#         return self._age
#     def set_name(self, new_name):
#         if not (isinstance(new_name, str) and new_name.isalpha() and new_name):
#             raise ValueError('Некорректное имя')
#         self._name = new_name
#     def set_age(self, new_age):
#         if not (isinstance(new_age, int) and (0 <= new_age <= 110)):
#             raise ValueError('Некорректный возраст')
#         self._age = new_age


#Todo: свойства, функция property()

# Реализуйте класс Rectangle , описывающий прямоугольник. При создании
# экземпляра класс должен принимать два аргумента в следующем порядке:
# • length — длина прямоугольника
# • width — ширина прямоугольника
# Экземпляр класса Rectangle должен иметь два атрибута:
# • length — длина прямоугольника
# • width — ширина прямоугольника
# Класс Rectangle должен иметь два свойства:
# • perimeter — свойство, доступное только для чтения, возвращающее
# периметр прямоугольника
# • area — свойство, доступное только для чтения, возвращающее площадь
# прямоугольника

# class Rectangle:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#     def get_perimeter(self):
#         return (self._width + self._length) * 2
#     def get_area(self):
#         return self._width * self._length
#     perimeter = property(get_perimeter)
#     area = property(get_area())

# Реализуйте класс HourClock , описывающий часы с одной лишь часовой
# стрелкой. При создании экземпляра класс должен принимать один аргумент:
# • hours — количество часов. Если hours не является целым числом,
# принадлежащим диапазону [1; 12] , должно быть
# возбуждено исключение ValueError с текстом:
# Некорректное время
# Класс HourClock должен иметь одно свойство:
# • hours — свойство, доступное для чтения и записи,
# возвращающее текущее количество часов. При изменении свойство
# должно проверять, что новое значение является целым числом,
# принадлежащим диапазону [1; 12] , в противном случае должно быть
# возбуждено исключение ValueError с текстом:
# Некорректное время

# class HourClock:
#     def __init__(self, hours):
#         if not isinstance(hours, int):
#             raise ValueError("error hours")
#         if not (1 <= hours <= 12):
#             raise ValueError("error hours")
#         self._hours = hours
#     def get_hours(self):
#         return self._hours
#     def set_hours(self, new_hours):
#         if not isinstance(new_hours, int) or not (0 < new_hours <= 12):
#             raise ValueError('error hours')
#         self._hours = new_hours
#     hours = property(get_hours, set_hours)

# Реализуйте класс Person , описывающий человека. При создании экземпляра
# класс должен принимать два аргумента в следующем порядке:
# • name — имя человека
# • surname — фамилия человека
# Экземпляр класса Person должен иметь два атрибута:
# • name — имя человека
# • surname — фамилия человека
# Класс Person должен иметь одно свойство:
# • fullname — свойство, доступное для чтения и записи, возвращающее
# полное имя человека в виде строки:
# <имя> <фамилия>

# class Person:
#     def __init__(self, name, surname):
#         self._name = name
#         self._surname = surname
#     def get_fullname(self):
#         return f"<{self._name}> <{self._surname}>"
#     def set_fullname(self, fullname):
#         total_list = fullname.split()
#         self._name = total_list[0]
#         self._surname = total_list[1]
#     fullname = property(get_fullname, set_fullname)

#Todo : декоратор @property =>

# Вам доступен класс Person , описывающий человека. При создании экземпляра
# класс принимает два аргумента в следующем порядке:
# • name — имя человека
# • surname — фамилия человека
# Экземпляр класса Person имеет два атрибута:
# • name — имя человека
# • surname — фамилия человека
# Класс Person имеет одно свойство:
# • fullname — свойство, доступное для чтения и записи, возвращающее
# полное имя человека в виде строки:
# <имя> <фамилия>
# Реализуйте свойство fullname класса Person с помощью
# декоратора @property

# class Person:
#     def __init__(self, name, surname):
#         self._name = name
#         self._surname = surname
#     @property
#     def fullname(self):
#         return f"<{self._name}> <{self._surname}>"
#     @property.setter
#     def fullname(self, fullname):
#         total_list = fullname.split()
#         self._name = total_list[0]
#         self._surname = total_list[1]

# В целях безопасности в базах данных пароли от аккаунтов пользователей
# хранятся не в явном виде, а в виде хеш-значений — чисел, вычисленных по
# специальному алгоритму на основе паролей.
# Вам доступна функция hash_function() , которая принимает в качестве
# аргумента пароль и возвращает его хеш-значение.
# Реализуйте класс Account , описывающий аккаунт интернет-пользователя на
# некотором сервисе. При создании экземпляра класс должен принимать два
# аргумента в следующем порядке:
# • login — логин пользователя
# • password — пароль пользователя
# Класс Account должен иметь два свойства:
# • login — свойство, доступное только для чтения, возвращающее логин
# пользователя. При попытке изменения свойство должно быть возбуждено
# исключение AttributeError с текстом:
# Изменение логина невозможно
# • password — свойство, доступное для чтения и записи, возвращающее
# хеш-значение пароля от аккаунта пользователя. При изменении свойство
# должно вычислять хеш-значение нового пароля и сохранять его, а не сам
# пароль
#
# def hash_function(password):
#     hash_value = 0
#     for char, index in zip(password, range(len(password))):
#         hash_value += ord(char) * index
#     return hash_value % 10 ** 9
#
# class Account:
#     def __init__(self, login, password):
#         self._login = login
#         self._password = password
#     @property
#     def login(self):
#         return self._login
#     @property.setter
#     def login(self, new_login):
#         raise AttributeError('Изменение логина невозможно')
#     @property
#     def password(self):
#         return self._password
#     @property.setter
#     def password(self, new_password):
#         self._password = hash_function(new_password)
#     password = property(password, login)

# Для кодирования цвета часто используется шестнадцатеричное значение цвета.
# Оно записывается в формате #RRGGBB , где RR (красный), GG (зеленый)
# и BB (синий) являются шестнадцатеричными целыми числами в
# диапазоне [00; FF] (или [0; 255] в десятичной системе счисления), которые
# указывают интенсивность соответствующих
# цветов. Например, #0000FF представляет чистый синий цвет, так как синий
# компонент имеет наивысшее значение ( FF ), а остальные — 00 .
# Реализуйте класс Color , описывающий цвет. При создании экземпляра класс
# должен принимать один аргумент:
# • hexcode — шестнадцатеричное значение цвета
# Экземпляр класса Color должен иметь три атрибута:
# • r — интенсивность красного компонента цвета в виде десятичного числа
# • g — интенсивность зеленого компонента цвета в виде десятичного числа
# • b — интенсивность синего компонента цвета в виде десятичного числа
# Класс Color должен иметь одно свойство:
# • hexcode — свойство, доступное для чтения и записи, возвращающее
# шестнадцатеричное значение цвета

# class Color:
#     def __init__(self, hexcode):
#         self._hexcode = hexcode
#     @property.getter
#     def hexcode(self):
#         return self._hexcode
#     @hexcode.setter
#     def hexcode(self, hexcode):
#         self._hexcode = hexcode
#         self.r = int(hexcode[0:2], 16)
#         self.g = int(hexcode[2:4], 16)
#         self.b = int(hexcode[4:6], 16)


#Todo: декоратор @classmethod =>

# Реализуйте класс Circle , описывающий круг. При создании экземпляра класс
# должен принимать один аргумент:
# • radius — радиус круга
# Экземпляр класса Circle должен иметь один атрибут:
# • radius — радиус круга
# Класс Circle должен иметь один метод класса:
# • from_diameter() — метод, принимающий в качестве аргумента диаметр
# круга и возвращающий экземпляр класса Circle , созданный на основе
# переданного диаметра

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#     @classmethod
#     def from_diameter(cls, diameter):
#         return cls(diameter / 2)

# Реализуйте класс Rectangle , описывающий прямоугольник. При создании
# экземпляра класс должен принимать два аргумента в следующем порядке:
# • length — длина прямоугольника
# • width — ширина прямоугольника
# Экземпляр класса Rectangle должен иметь два атрибута:
# • length — длина прямоугольника
# • width — ширина прямоугольника
# Класс Rectangle должен иметь один метод класса:
# • square() — метод, принимающий в качестве аргумента число side и
# возвращающий экземпляр класса Rectangle c длиной и шириной,
# равными side
#
# class Rectangle:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#     @classmethod
#     def square(cls, side):
#         return cls(side, side)

# Реализуйте класс Pet , описывающий домашнее животное. При создании
# экземпляра класс должен принимать один аргумент:
# • name — имя домашнего животного
# Экземпляр класса Pet должен иметь один атрибут:
# • name — имя домашнего животного
# Класс Pet должен иметь три метода класса:
# • first_pet() — метод, возвращающий самый первый созданный
# экземпляр класса Pet . Если ни одного экземпляра еще не было создано,
# метод должен вернуть значение None
# • last_pet() — метод, возвращающий самый последний созданный
# экземпляр класса Pet . Если ни одного экземпляра еще не было создано,
# метод должен вернуть значение None
# • num_of_pets() — метод, возвращающий количество созданных
# экземпляров класса Pet

# class Pet:
#     pets = []
#     def __init__(self, name):
#         self._name = name
#         Pet.pets.append(self)
#     @classmethod
#     def first_pet(cls):
#         if cls.pets:
#             return cls.pets[0]
#         else:
#             return None
#     @classmethod
#     def last_pet(cls):
#         if cls.pets:
#             return cls.pets[len(cls.pets) - 1]
#         else:
#             return None
#     @classmethod
#     def num_of_pets(cls):
#         return len(cls.pets)

# Реализуйте класс StrExtension , описывающий набор функций для работы со
# строками. При создании экземпляра класс не должен принимать никаких
# аргументов.
# Класс StrExtension должен иметь три статических метода:
# • remove_vowels() — метод, который принимает в качестве аргумента
# строку, удаляет из нее все гласные латинские буквы без учета регистра и
# возвращает полученный результат
# • leave_alpha() — метод, который принимает в качестве аргумента
# строку, удаляет из нее все символы, не являющиеся латинскими буквами, и
# возвращает полученный результат
# • replace_all() — метод, который принимает три строковых
# аргумента string, chars и char , заменяет в строке string все
# символы из chars на char с учетом регистра и возвращает полученный
# результат

# import re
# class StrExtension:
#     __VOWELS = re.compile(r'[aeiouy]', flags=re.I)
#     __ALPHABET = re.compile(r'[^a-zA-Z]')
#
#     @staticmethod
#     def remove_vowels(string):
#         return StrExtension.__VOWELS.sub('', string)
#     @staticmethod
#     def leave_alpha(string):
#         return StrExtension.__ALPHABET.sub('', string)
#     @staticmethod
#     def replace_all(string, chars, char):
#         return re.sub(fr'[{chars}]', char, string)

#Todo: декоратор @singledispatchmethod =>

# Вам доступен класс Processor . При создании экземпляра класс не принимает
# никаких аргументов.
# Класс Processor имеет один статический метод:
# • process() — метод, который принимает в качестве аргумента
# произвольный объект, преобразует его в зависимости от его типа и
# возвращает полученный результат. Если тип переданного объекта не
# поддерживается методом, возбуждается исключение TypeError с
# текстом:
# Аргумент переданного типа не поддерживается
# Перепишите метод process() класса Processor с использованием
# декоратора @singledispatchmethod , чтобы он выполнял ту же задачу.

#todo ,,,
#Todo Магические методы. Создание, инициализация и очищение объектов =>


# Реализуйте класс Config , который соответствует шаблону синглтон и
# описывает конфигурационный объект с фиксированными параметрами. При
# создании экземпляра класс не должен принимать никаких аргументов.
# При первом вызове конструктора класса Config должен создаваться и
# возвращаться экземпляр этого класса, а при последующих вызовах должен
# возвращаться экземпляр, созданный при первом вызове.
# Экземпляр класса Config должен иметь четыре атрибута:
# • program_name — атрибут со строковым значением GenerationPy
# • environment — атрибут со строковым значением release
# • loglevel — атрибут со строковым значением verbose
# • version — атрибут со строковым значением 1.0.0
#singleton
# class Config:
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls)
#         return cls._instance
#     def __init__(self):
#         self.program_name = "GenerationPay"
#         self.inviroment = "release"
#         self.loglevel = "verbose"
#         self.version = "1.0.0"
#
# config1 = Config()
# config2 = Config()
#
#
# print(config1.program_name)

#Todo Магические методы. Строковое представление объектов =>

# Требовалось реализовать класс Book , описывающий книгу. При создании
# экземпляра класс должен был принимать три аргумента в следующем порядке:
# • title — название книги
# • author — автор книги
# • year — год выпуска книги
# Предполагалось, что экземпляры класса Book будут иметь следующее
# формальное строковое представление:
# Book('<название книги>', '<автор книги>', <год выпуска книги>)
# И следующее неформальное строковое представление:
# <название книги> (<автор книги>, <год выпуска книги>)
# Программист торопился и решил задачу неправильно. Исправьте приведенный
# ниже код и реализуйте класс Book правильно

# class Book:
#     def __init__(self, title, author, year):
#         self._title = title
#         self._author = author
#         self._year = year
#     def __str__(self):
#         return f"<{self._title}> <{self._author}> <{self._year}>"
#     def __repr__(self):
#         return f"Book(\'{self._title}\', \'{self._author}\', \'{self._year}\')"
#
# book = Book("aaa", "bbb", 2024)
#
# print(book)
# print(repr(book))

# Вам доступен класс Rectangle , описывающий прямоугольник. При создании
# экземпляра класс принимает два аргумента в следующем порядке:
# • length — длина прямоугольника
# • width — ширина прямоугольника
# Реализуйте для экземпляров класса Rectangle следующее формальное и
# неформальное строковое представление:
# Rectangle(<длина прямоугольника>, <ширина прямоугольника>)

# class Rectangle:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#     def __str__(self):
#         return f"Rectangle({self._length}, {self._width})"
#     def __repr__(self):
#         return f"Rectangle({self._length}, {self._width}) => repr"
#

# Реализуйте класс Vector , описывающий вектор на плоскости. При создании
# экземпляра класс должен принимать два аргумента в следующем порядке:
# • x — координата вектора по оси x
# • y — координата вектора по оси y
# Экземпляр класса Vector должен иметь следующее формальное строковое
# представление:
# Vector(<координата x>, <координата y>)
# И следующее неформальное строковое представление:
# Вектор на плоскости с координатами (<координата x>, <координата y>)

# class Vector:
#     def __init__(self, x = 0, y = 0):
#         self._x = x
#         self._y = y
#     def __str__(self):
#         return f"Vector(<{self._x}>, <{self._y}>)"
#     def __repr__(self):
#         return f"<координата {self._x}>, <координата {self._y}>"

# IP-адрес — это уникальный адрес, идентифицирующий устройство в интернете
# или локальной сети. IP-адреса представляют собой набор из четырех целых
# чисел, разделенных точками. Например, 192.158.1.38 . Каждое число в наборе
# принадлежит интервалу от 0 до 255 . Таким образом, полный диапазон IPадресации — это адреса от 0.0.0.0 до 255.255.255.255 .
# Реализуйте класс IPAddress , описывающий IP-адрес. При создании экземпляра
# класс должен принимать один аргумент:
# • ipaddress — IP-адрес, представленный в одном из следующих вариантов:
# 1. строка из четырех целых чисел, разделенных точками
# 2. список или кортеж из четырех целых чисел
# Экземпляр класса IPAddress должен иметь следующее формальное строковое
# представление:
# IPAddress('<IP-адрес в виде четырех целых чисел, разделенных
# точками>')
# И следующее неформальное строковое представление:
# <IP-адрес в виде четырех целых чисел, разделенных точками>
#
# class IPAddress:
#     def __init__(self, ipadress):
#         if isinstance(ipadress, str):
#             self.ipadress = ipadress
#         elif isinstance(ipadress, (list, tuple)):
#             self.ipadress = '.'.join(map(str, ipadress))
#     def __str__(self):
#         return self.ipadress
#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.ipadress}')"

# Реализуйте класс PhoneNumber , описывающий телефонный номер. При создании
# экземпляра класс должен принимать один аргумент:
# • phone_number — телефонный номер, представляющий строку из десяти
# цифр в одном из следующих форматов:
# 1. dddddddddd
# 2. ddd ddd dddd
# Экземпляр класса PhoneNumber должен иметь следующее формальное строковое
# представление:
# PhoneNumber('<телефонный номер в формате dddddddddd>')
# И следующее неформальное строковое представление:
# <телефонный номер в формате (ddd) ddd-dddd>
#
# import re
# class PhoneNumber:
#     def __init__(self, phone_number):
#         pattern = r'^(\d{10})|(\d{3}\s\d{3}\s\d{4})$'
#         if re.match(pattern, phone_number):
#             self._phone_number = phone_number
#         else:
#             raise ValueError("error")
#     def __str__(self):
#         pattern = r'^\d{10}$'
#         if re.match(pattern, self._phone_number):
#             return f"PhoneNumber(\'<{self._phone_number}>\')"
#         else:
#             new_phone_number = re.sub(r'\s', '', self._phone_number)
#             return f"PhoneNumber(\'<{new_phone_number}>\')"
#     def __repr__(self):
#         pattern = r'^\d{10}$'
#         if re.match(pattern, self._phone_number):
#             formatted_phone_number = re.findall(r'\d{3}|\d{4}', self._phone_number)
#             return f"({formatted_phone_number[0]}) {formatted_phone_number[1]}-{formatted_phone_number[2]}"
#         else:
#             phone_number_array = self._phone_number.split()
#             return f"({phone_number_array[0]}) {phone_number_array[1]}-{phone_number_array[2]}"
#
# phone = PhoneNumber('9285936260')
# print(phone)
# print(repr(phone))
#
# phone2 = PhoneNumber('928 593 6260')
# print(phone2)
# print(repr(phone2))

# Реализуйте класс AnyClass . При создании экземпляра класс должен принимать
# произвольное количество именованных аргументов и устанавливать их в
# качестве атрибутов создаваемому экземпляру.
# `Экземпляр класса AnyClass должен иметь следующее формальное строковое
# представление:
# AnyClass(<имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го
# атрибута>=<значение 2-го атрибута>, ...)`
# И следующее неформальное строковое представление:
# AnyClass: <имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го
# атрибута>=<значение 2-го атрибута>, ...
#
# class AnyClass:
#     def __init__(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#     def __str__(self):
#         attributes = ""
#         for attr, value in vars(self).items():
#             attributes += f"{attr}={value}"
#         attributes = attributes.rstrip(", ")
#         return f"AnyClass({attributes})"
#
# string = AnyClass(name="John", age=30, city="New York", language="Python", version="3.10", framework="Django")
# print(string)

#Todo: Магические методы. Сравнение объектов =>

# Реализуйте класс Vector , описывающий вектор на плоскости. При создании
# экземпляра класс должен принимать два аргумента в следующем порядке:
# • x — координата вектора по оси x
# • y — координата вектора по оси y
# Экземпляр класса Vector должен иметь следующее формальное строковое
# представление:
# Vector(<координата x>, <координата y>)
# Также экземпляры класса Vector должны поддерживать операции сравнения с
# помощью операторов == и != . Два вектора считаются равными, если их
# координаты по обеим осям совпадают. Методы, реализующие операции
# сравнения, должны уметь сравнивать как два вектора между собой, так и вектор с
# кортежем из двух чисел, представляющих координаты x и y.

# class Vector:
#     def __init__(self, x = 0, y = 0):
#         self._x = x
#         self._y = y
#     def get_tuple_coordinate(self):
#         return (self._x, self._y)
#     def __repr__(self):
#         return f"Vector({self._x}, {self._y})"
#     def __eq__(self, other):
#         if isinstance(other, Vector):
#             return self.get_tuple_coordinate() == other.get_tuple_coordinate()
#         if isinstance(other, tuple):
#             return self.get_tuple_coordinate() == other
#         return NotImplemented
#
# vector1 = Vector(1, 2)
# vector2 = Vector(1, 2)
#
# print(vector1.get_tuple_coordinate())
# print(vector2.get_tuple_coordinate())
#
# print(vector1 == vector2)

# Будем называть словом любую последовательность из одной или более
# латинских букв.
# Реализуйте класс Word , описывающий слово. При создании экземпляра класс
# должен принимать один аргумент:
# • word — слово
# Экземпляр класса Word должен иметь следующее формальное строковое
# представление:
# Word('<слово в исходном виде>')
# И следующее неформальное строковое представление:
# <слово, в котором первая буква заглавная, а все остальные строчные>
# Также экземпляры класса Word должны поддерживать между собой все
# операции сравнения с помощью операторов ==, !=, >, <, >=, <= . Два
# слова считаются равными, если их длины совпадают. Слово считается больше
# другого слова, если его длина больше.

# class Word:
#     def __init__(self, word):
#         self._word = word
#     def __str__(self):
#         return f"Word(\'<{self._word}>\')"
#     def __repr__(self):
#         return self._word.capitalize()
#     def __eq__(self, other):
#         if isinstance(other, Word):
#             return other._word == self._word or self._word == other._word
#         return NotImplemented
#     def __ne__(self, other):
#         if isinstance(other, Word):
#             return other._word != self._word or self._word != other._word
#         return NotImplemented
#
# word = Word("ghghhg")
# print(word)
# word2 = Word("ghghhg")
#
# print(word != word2)

# Реализуйте класс Month , описывающий месяц. При создании экземпляра класс
# должен принимать два аргумента в следующем порядке:
# • year — год
# • month — порядковый номер месяца
# Экземпляр класса Month должен иметь следующее формальное строковое
# представление:
# Month(<год>, <порядковый номер месяца>)
# И следующее неформальное строковое представление:
# <год>-<порядковый номер месяца>
# Также экземпляры класса Month должны поддерживать все операции сравнения
# с помощью операторов ==, !=, >, <, >=, <= . Два Month объекта считаются
# равными, если их годы и порядковые номера месяцев совпадают. Month объект
# считается больше другого Month объекта, если его год больше. В случае если
# два Month объекта имеют равные года, большим считается тот, чей месяц
# больше. Методы, реализующие операции сравнения, должны уметь сравнивать
# как два Month объекта между собой, так и Month объект с кортежем из двух
# чисел, представляющих год и месяц.

# class Month:
#     def __init__(self, year, month):
#         self._year = year
#         self._month = month
#     def __str__(self):
#         return f"Month({self._year}, {self._month})"
#     def __repr__(self):
#         return f"<{self._year}>-<{self._month}>"
#     def fields(self):
#         return (self._year, self._month)
#     def __eq__(self, other):
#         if isinstance(other, Month):
#             return other.fields() == self.fields() or self.fields() == other.fields()
#         return NotImplemented
#
#     ...
# month = Month(1999, 12)
# print(month)

#...

#Todo: Магические методы. Унарные операторы =>

# Реализуйте класс ReversibleString , описывающий строку. При создании
# экземпляра класс должен принимать один аргумент:
# • string — значение строки
# Экземпляр класса ReversibleString должен иметь следующее неформальное
# строковое представление:
# <значение строки>
# Также экземпляр класса ReversibleString должен поддерживать унарный
# оператор - , результатом которого должен являться новый экземпляр
# класса ReversibleString со значением строки в обратном порядке.

#
# class ReversibleString:
#     def __init__(self, string):
#         self._string = string
#     def __repr__(self):
#         return f"<{self._string}>"
#     def __neg__(self):
#         neg_string = self._string[::-1]
#         return ReversibleString(neg_string)
#
# reverse = ReversibleString("marat")
# print(repr(reverse))
# reverse_string = -reverse
# print(reverse_string)

# Реализуйте класс Money , описывающий денежную сумму в рублях. При создании
# экземпляра класс должен принимать один аргумент:
# • amount — количество денег
# Экземпляр класса Money должен иметь следующее неформальное строковое
# представление:
# <количество денег> руб.
# Также экземпляр класса Money должен поддерживать унарные
# операторы + и - :
# • результатом унарного + должен являться новый экземпляр
# класса Money с неотрицательным количеством денег
# • результатом унарного - должен являться новый экземпляр
# класса Money с отрицательным количеством денег

# class Money:
#     def __init__(self, amount):
#         self._amount = amount
#     def __repr__(self):
#         return f"<{self._amount}> руб."
#     def __pos__(self):
#         return Money(abs(self._amount))
#     def __neg__(self):
#         return Money(-abs(self._amount))

# Реализуйте класс Vector , описывающий вектор на плоскости. При создании
# экземпляра класс должен принимать два аргумента в следующем порядке:
# • x — координата вектора по оси x
# • y — координата вектора по оси y
# Экземпляр класса Vector должен иметь следующее формальное строковое
# представление:
# Vector(<координата x>, <координата y>)
# И следующее неформальное строковое представление:
# (<координата вектора по оси x>, <координата вектора по оси y>)
# Также экземпляр класса Vector должен поддерживать унарные
# операторы + и - :
# • результатом унарного + должен являться новый экземпляр
# класса Vector с исходными координатами
# • результатом унарного - должен являться новый экземпляр
# класса Vector с координатами, взятыми с противоположным знаком
# Наконец, при передаче экземпляра класса Vector в функцию abs() должен
# возвращаться его модуль

# class Vector:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#     def __str__(self):
#         return f"Vector(<координата {self._x}><координата {self._y}>)"
#     def fields(self):
#         return (self._x, self._y)
#     def __pos__(self):
#         return self.fields()
#     def __neg__(self):
#         return Vector(-self.x, -self.y)
#     def __abs__(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5

#todo : ...

#Todo: Магические методы. Арифметические операторы =>

# Реализуйте класс FoodInfo , описывающий пищевую ценность продуктов. При
# создании экземпляра класс должен принимать три аргумента в следующем
# порядке:
# • proteins — количество белков в граммах
# • fats — количество жиров в граммах
# • carbohydrates — количество углеводов в граммах
# Экземпляр класса FoodInfo должен иметь три атрибута:
# • proteins — количество белков в граммах
# • fats — количество жиров в граммах
# • carbohydrates — количество углеводов в граммах
# И следующее формальное строковое представление:
# FoodInfo(<количество белков>, <количество жиров>, <количество
# углеводов>)
# Также экземпляры класса FoodInfo должны поддерживать между собой
# операцию сложения с помощью оператора + , результатом которой должен
# являться новый экземпляр класса FoodInfo с суммарным количеством белков,
# жиров и углеводов исходных экземпляров.
# Наконец, экземпляр класса FoodInfo должен поддерживать операции
# умножения, деления и деления нацело на число n с помощью операторов *,
# / и // соответственно:
# • результатом умножения должен являться новый экземпляр
# класса FoodInfo , количество белков, жиров и углеводов которого
# умножены на n
# • результатом деления должен являться новый экземпляр
# класса FoodInfo , количество белков, жиров и углеводов которого
# поделены на n
# • результатом деления нацело должен являться новый экземпляр
# класса FoodInfo , количество белков, жиров и углеводов которого
# поделены нацело на n

# class FoodInfo:
#     def __init__(self, proteins, fats, carbohydrates):
#         self._proteins = proteins
#         self._fats = fats
#         self._carbohydrates = carbohydrates
#     def __str__(self):
#         return f"FoodInfo(<{self._proteins}>, <{self._fats}>, <{self._carbohydrates}>)"
#     def __add__(self, other):
#         if isinstance(other, FoodInfo):
#             return FoodInfo(self._proteins + other._proteins, self._fats + other._fats, self._carbohydrates + other._carbohydrates)
#         return NotImplemented
#     def __mul__(self, n):
#         if isinstance(n, int) or isinstance(n, float):
#             return FoodInfo(self._proteins * n, self._fats * n, self._carbohydrates * n)
#         return NotImplemented
#     def __truediv__(self, n):
#         if isinstance(n, int) or isinstance(n, float):
#             return FoodInfo(self._proteins / n, self._fats / n, self._carbohydrates / n)
#         return NotImplemented
#     def __floordiv__(self, n):
#         if isinstance(n, int) or isinstance(n, float):
#             return FoodInfo(self._proteins // n, self._fats // n, self._carbohydrates // n)
#         return NotImplemented

# Реализуйте класс Vector , описывающий вектор на плоскости. При создании
# экземпляра класс должен принимать два аргумента в следующем порядке:
# • x — координата вектора по оси x
# • y — координата вектора по оси y
# Экземпляр класса Vector должен иметь следующее формальное строковое
# представление:
# Vector(<координата x>, <координата y>)
# Также экземпляры класса Vector должны поддерживать между собой операции
# сложения и вычитания с помощью операторов + и - соответственно:
# • результатом сложения должен являться новый экземпляр
# класса Vector , координата по оси x которого равна сумме координат по
# оси x исходных векторов, координата по оси y — сумме координат по
# оси y исходных векторов
# • результатом вычитания должен являться новый экземпляр
# класса Vector координата по оси x которого равна разности координат по
# оси x исходных векторов с учетом порядка, координата по оси y —
# разности координат по оси y исходных векторов с учетом порядка
# Наконец, экземпляр класса Vector должен поддерживать операции умножения
# и деления на число n с помощью операторов * и / соответственно:
# • результатом умножения должен являться новый экземпляр
# класса Vector , координаты которого умножены на n
# • результатом деления должен являться новый экземпляр
# класса Vector , координаты которого поделены на n
# Операция умножения должна быть выполнима независимо от порядка
# операндов, то есть должна быть возможность умножить как вектор на число, так
# и число на вектор.

# class Vector:
#     def __init__(self, x = 0, y = 0):
#         self._x = x
#         self._y = y
#     def __str__(self):
#          return f"Vector(<координата {self._x}><координата {self._y}>)"
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(other._x + self._x, other._y + self._y)
#         return NotImplemented
#     def __sub__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self._x - other._x, self._y - other._y)
#         return NotImplemented
#     def __mul__(self, other):
#         if isinstance(other, (int, float)):
#             return Vector(self._x * other, self._y * other)
#         elif isinstance(other, Vector):
#             return Vector(self._x * other._x, self._y * other._y)
#         else:
#             return NotImplemented
#     def __rmul__(self, other):
#         return self * other

# Реализуйте класс SuperString , описывающий строку. При создании экземпляра
# класс должен принимать один аргумент:
# • string — значение строки
# Экземпляр класса SuperString должен иметь следующее неформальное
# строковое представление:
# <значение строки>
# Помимо этого, экземпляры класса SuperString должны поддерживать между
# собой операцию сложения с помощью оператора + , результатом которой должен
# являться новый экземпляр класса SuperString , представляющий
# конкатенацию исходных.
# Также экземпляр класса SuperString должен поддерживать операции
# умножения, деления, побитового сдвига влево и побитового сдвига вправо на
# целое число n с помощью операторов *, /, << и >> соответственно:
# • результатом умножения должен являться новый экземпляр
# класса SuperString , представляющий исходную строку, умноженную
# на n
# • результатом деления должен являться новый экземпляр
# класса SuperString , представляющий строку из первых m символов
# исходной строки, где m — длина исходной строки, поделенная нацело
# на n
# • результатом побитового сдвига влево должен являться новый экземпляр
# класса SuperString , представляющий исходную строку без
# последних n символов. Если n больше или равно длине исходной строки,
# результатом должен являться экземпляр класса SuperString ,
# представляющий пустую строку
# • результатом побитового сдвига вправо должен являться новый экземпляр
# класса SuperString , представляющий исходную строку без
# первых n символов. Если n больше или равно длине исходной строки,
# результатом должен являться экземпляр класса SuperString ,
# представляющий пустую строку
# Операция умножения должна быть выполнима независимо от порядка
# операндов, то есть должна быть возможность умножить как строку на число, так
# и число на строку
# class SuperString:
#     def __init__(self, string):
#         self.string = string
#     def __str__(self):
#         return self.string
#     def __add__(self, other):
#         if isinstance(other, SuperString):
#             return SuperString(self.string + other.string)
#         return NotImplemented
#     def __mul__(self, other):
#         if isinstance(other, int):
#             return SuperString(self.string * other)
#         return NotImplemented
#     def __rmul__(self, other):
#         return self.__mul__(other)
#     def __truediv__(self, other):
#         if isinstance(other, int):
#             return SuperString(self.string[:len(self.string) // other])
#         return NotImplemented
#     def __lshift__(self, other):
#         if isinstance(other, int):
#             if (length := len(self.string)) <= other:
#                 return SuperString('')
#             else:
#                 return SuperString(self.string[0:length - other])
#         return NotImplemented
#     def __rshift__(self, other):
#         if isinstance(other, int):
#             if len(self.string) <= other:
#                 return SuperString('')
#             else:
#                 return SuperString(self.string[other:])
#         return NotImplemented

# Реализуйте класс Time , описывающий время на цифровых часах. При создании
# экземпляра класс должен принимать два аргумента в следующем порядке:
# • hours — количество часов; каждые 24 часа должны преобразовываться
# в 0 часов
# • minutes — количество минут; каждые 60 минут должны
# преобразовываться в 1 час
# Экземпляр класса Time должен иметь следующее неформальное строковое
# представление:
# <количество часов в формате HH>:<количество минут в формате MM>
# Также экземпляры класса Time должны поддерживать между собой операцию
# сложения с помощью операторов + и += :
# • результатом сложения с помощью оператора + должен являться новый
# экземпляр класса Time , количество часов которого равно сумме
# часов исходных экземпляров класса Time , количество минут — сумме
# минут исходных экземпляров класса Time
# • результатом сложения с помощью оператора += должен являться левый
# экземпляр класса Time , количество часов которого увеличено на
# количество часов правого экземпляра класса Time , количество минут —
# на количество минут правого экземпляра класса Time
#
# class Time:
#     def __init__(self, hours, minutes):
#         self.hours, self.minutes = Time._normalize(hours, minutes)
#     @staticmethod
#     def _normalize(hours, minutes):
#         return (hours + minutes // 60) % 24, minutes % 60
#     def __str__(self):
#         return f'{self.hours:>02}:{self.minutes:>02}'
#     def __add__(self, other):
#         if isinstance(other, Time):
#             hours, minutes = self._normalize(self.hours + other.hours, self.minutes + other.minutes)
#             return Time(hours, minutes)
#         return NotImplemented
#     def __iadd__(self, other):
#         if isinstance(other, Time):
#             self.hours, self.minutes = self._normalize(self.hours + other.hours, self.minutes + other.minutes)
#             return self
#         return NotImplemented

#Todo: Магические методы. Вызываемые объекты

# Реализуйте класс Calculator , экземпляры которого позволяют выполнять
# различные арифметические операции с двумя числами. При создании экземпляра
# класс не должен принимать никаких аргументов.
# Экземпляр класса Calculator должен являться вызываемым объектом и
# принимать три аргумента:
# • a — число
# • b — число
# • operation — один из символов +, -, * и /
# Если operation равняется + , экземпляр класса Calculator должен вернуть
# сумму a и b , если - — разность a и b , если * —
# произведение a и b , если / — частное a и b . При попытке выполнить деление
# на ноль должно быть возбуждено исключение ValueError с текстом:
# Деление на ноль невозможно

# class Calculator:
#     def __call__(self, a, b, operation):
#         match operation:
#             case '+':
#                 return a + b
#             case '-':
#                 return a - b
#             case '*':
#                 return a * b
#             case '/':
#                 if b == 0:
#                     raise ValueError('Деление на ноль невозможно')
#                 return a / b

# Реализуйте класс RaiseTo , экземпляры которого позволяют возводить числа в
# фиксированную степень. При создании экземпляра класс должен принимать один
# аргумент:
# • degree — показатель степени
# Экземпляр класса RaiseTo должен являться вызываемым объектом и
# принимать один аргумент:
# • x — число
# Экземпляр класса RaiseTo должен возвращать значение x в степени degree .

# class RaiseTo:
#     def __init__(self, degree):
#         self._degree = degree
#     def __call__(self, x):
#         return x ** self._degree

# Реализуйте класс Dice , описывающий игральный кубик с определенным
# количеством граней. При создании экземпляра класс должен принимать один
# аргумент:
# • sides — количество граней игрального кубика
# Экземпляр класса Dice должен являться вызываемым объектом и не принимать
# никаких аргументов. При вызове он должен возвращать значение
# случайной грани игрального кубика. Например, если кубик имеет 6 граней,
# экземпляр класса Dice должен вернуть случайное число из диапазона [1; 6]
#
# from random import randint
# class Dice:
#     def __init__(self, sides):
#         self._sides = sides
#     def __call__(self):
#         return randint(1, self.sides)

# Реализуйте класс DateFormatter , экземпляры которого позволяют
# преобразовывать даты в формат определенной страны из таблицы выше. При
# создании экземпляра класс должен принимать один аргумент:
# • country_code — код страны
# Экземпляр класса DateFormatter должен являться вызываемым объектом и
# принимать один аргумент:
# • d — дата (тип date )
# Экземпляр класса DateFormatter должен возвращать строку с датой d в
# формате страны с кодом country_code .

# import datetime
#
# class DateFormatter:
#     def __init__(self, country_code):
#         if isinstance(country_code, str):
#             self._country_code = country_code
#         else:
#             raise ValueError("Неверный формат кода страны")
#
#     def __call__(self, date: datetime.date):
#         if not hasattr(self, '_country_code'):
#             raise ValueError("Код страны не установлен")
#
#         if not isinstance(date, datetime.date):
#             raise ValueError("Входной аргумент не является объектом datetime.date")
#
#         date_list = [date.year, date.month, date.day]
#         if self._country_code == 'ru':
#             return f"{date_list[2]}.{date_list[1]}.{date_list[0]}"
#         elif self._country_code == 'us':
#             return f"{date_list[1]}-{date_list[2]}-{date_list[0]}"
#         elif self._country_code == 'ca':
#             return f"{date_list[0]}-{date_list[1]}-{date_list[2]}"
#         elif self._country_code == 'br':
#             return f"{date_list[2]}/{date_list[1]}/{date_list[0]}"
#         elif self._country_code == 'fr':
#             return f"{date_list[2]}.{date_list[1]}.{date_list[0]}"
#         elif self._country_code == 'pt':
#             return f"{date_list[2]}-{date_list[1]}-{date_list[0]}"
#         else:
#             raise ValueError("Неверный код страны")
# time_formatter = DateFormatter('')
# formatted_date = time_formatter(datetime.date(2022, 11, 7))
# print(formatted_date)

#....

#Todo: Магические методы. Преобразование типов =>

# Реализуйте класс Vector , описывающий вектор на плоскости. При создании
# экземпляра класс должен принимать два аргумента в следующем порядке:
# • x — координата вектора по оси x
# • y — координата вектора по оси y
# Экземпляр класса Vector должен иметь следующее неформальное строковое
# представление:
# (<координата x>, <координата y>)
# Также экземпляр класса Vector должен поддерживать приведение к
# типам bool, int, float и complex :
# • при приведении к типу bool значением вектора должно являться
# значение True , если хотя бы одна его координата не равна нулю,
# или False в противном случае
# • при приведении к типу int значением вектора должен являться его
# модуль в виде целого числа с отброшенной дробной частью
# • при приведении к типу float значением вектора должен являться его
# модуль в виде вещественного числа
# • при приведении к
# типу complex значением вектора должно являться комплексное число,
# вещественная часть которого равна координате вектора по оси �x,
# мнимая часть — координате вектора по оси �y

# class Vector:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#     def __bool__(self):
#         return self.x != 0 or self.y != 0
#     def __int__(self):
#         return int(self.__float__())
#     def __float__(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#     def __complex__(self):
#         return complex(self.x, self.y)

# Реализуйте класс Temperature , описывающий температуру в градусах по шкале
# Цельсия. При создании экземпляра класс должен принимать один аргумент:
# • temperature — температура в градусах по шкале Цельсия
# Класс Temperature должен иметь один метод экземпляра:
# • to_fahrenheit() — метод, возвращающий температуру по шкале
# Фаренгейта
# Класс Temperature должен иметь один метод класса:
# • from_fahrenheit() — метод, принимающий в качестве
# аргумента температуру по шкале Фаренгейта и возвращающий экземпляр
# класса Temperature , созданный на основе переданной температуры
# Экземпляр класса Temperature должен иметь следующее неформальное
# строковое представление:
# <температура в градусах по шкале Цельсия с округлением до двух
# знаков после запятой>°C
# Также экземпляр класса Temperature должен поддерживать приведение к
# типам bool, int и float :
# • при приведении к типу bool значением экземпляра
# класса Temperature должно являться значение True , если его
# температура выше нуля, или False в противном случае
# • при приведении к типу int значением экземпляра
# класса Temperature должна являться его температура в виде целого
# числа с отброшенной дробной частью
# • при приведении к типу float значением экземпляра
# класса Temperature должна являться его температура в виде
# вещественного числа
#
# class Temperature:
#     def __init__(self, temperature):
#         self.temperature = temperature
#     def to_fahrenheit(self):
#         return self.temperature * 1.8 + 32
#     def __str__(self):
#         return f'{self.temperature.__round__(2)}°C'
#     def __bool__(self):
#         return self.temperature > 0
#     def __int__(self):
#         return int(self.temperature)
#     def __float__(self):
#         return float(self.temperature)
#     @classmethod
#     def from_fahrenheit(cls, value):
#         celsius = (5 / 9) * (value - 32)
#         return cls(celsius)

#Todo: Магические методы.

# Требовалось реализовать класс Item , описывающий предмет. При создании
# экземпляра класс должен был принимать три аргумента в следующем порядке:
# • name — название предмета
# • price — цена предмета в рублях
# • quantity — количество предметов
# Предполагалось, что при обращении к атрибуту name экземпляра
# класса Item будет возвращаться его название с заглавной буквы, а при
# обращении к атрибуту total — произведение цены предмета на его количество.
# Программист торопился и решил задачу неправильно. Дополните приведенный
# ниже код и реализуйте правильный класс Item
# class Item:
#     def __init__(self, name, price, quantity):
#         self._name = name
#         self._price = price
#         self._quantity = quantity
#
#     def __getattribute__(self, name):
#         if name == 'total':
#             return self._price * self._quantity
#         elif name == 'name':
#             return object.__getattribute__(self, '_name').title()
#         return object.__getattribute__(self, name)
#
# item = Item('apple', 1.99, 5)
# print(item.__getattribute__('name'))


# Требовалось реализовать класс Logger . При создании экземпляра класс не
# должен был принимать никаких аргументов.
# Предполагалось, что при установке или изменении значения атрибута
# экземпляра класса Logger будет выводиться текст:
# Изменение значения атрибута <имя атрибута> на <новое значение
# атрибута>
# Также планировалось, что при удалении атрибута будет выводиться текст:
# Удаление атрибута <имя атрибута>
# Программист торопился и решил задачу неправильно. Дополните приведенный
# ниже код и реализуйте правильный класс Logger

# class Logger:
#     def __setattr__(self, name, value):
#         print(f'Изменение значения атрибута {name} на {value}')
#         self.__dict__['name'] = value
#     def __delattr__(self, name):
#         print(f'Удаление атрибута {name}')
#         del self.__dict__['name']

# Реализуйте класс Ord . При создании экземпляра класс не должен принимать
# никаких аргументов.
# Экземпляр класса Ord должен выступать в качестве альтернативы
# функции ord() . При обращении к атрибуту экземпляра, именем которого
# является одиночный символ, должна возвращаться его позиция в таблице
# символов Unicode.

# class Ord:
#     def __getattr__(self, name):
#         return ord(name)

# Реализуйте класс Const . При создании экземпляра класс должен принимать
# произвольное количество именованных аргументов. Все передаваемые
# аргументы должны устанавливаться создаваемому экземпляру в качестве
# атрибутов.
# Класс Const должен разрешать устанавливать атрибуты своим экземплярам и
# получать их значения, но не разрешать изменять значения этих атрибутов, а
# также удалять их. При попытке изменить значение атрибута должно
# возбуждаться исключение AttributeError с текстом:
# Изменение значения атрибута невозможно
# При попытке удалить атрибут должно возбуждаться
# исключение AttributeError с текстом:
# Удаление атрибута невозможно
#
# class Const:
#     def __init__(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#     def __setattr__(self, k, v):
#         if k in self.__dict__:
#             raise AttributeError('Изменение значения атрибута невозможно')
#         object.__setattr__(self, k, v)
#     def __getattribute__(self, name):
#         return object.__getattribute__(self, name)
#     def __delattr__(self, name):
#         raise AttributeError('Удаление атрибута невозможно')

#Todo: Магические методы. Хеширование объектов =>

