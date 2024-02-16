
#1. создание пользовательских классов и их объектов
#2. атрибуты объектов
#3. атрибуты класса
#4. атрибут __dict__
#5. функции getattr(), setattr(), delattr(), hasattr()

#1
class Car:
    def __init__(self, make, model, year, mileage = 0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def print_attr(self):
        return f"{self.make} {self.model} {self.year}"
    #2
    def update_milage(self, new_mileage):
        self.mileage = new_mileage
    #3
    company = "Mercedes_Porsche_union"



#1
car = Car("mercedes", "e63", 2019)
print(car.print_attr())
#2
car.update_milage(200)
print(car.mileage)
#3
print(car.company)
#4
print(car.__dict__)
car_trash = Car("bmw", "m5", 2000)
#5 проверка наличия атрибута
print(hasattr(car_trash, "make"))
print(getattr(car_trash, "year"))
setattr(car_trash, "year", 2005)
print(getattr(car_trash, "year"))
delattr(car_trash, "make")
print(hasattr(car_trash, "make"))