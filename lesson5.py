# static method
# class method
# instance method


class Car:

    wheels_count = 4

    def __init__(self, name, color):
        self._name = name
        self._color = color

    def get_color(self):
        return self._color
    def get_name(self):
        return self._name

    @classmethod
    def get_wheel_count(cls):
        return cls.wheels_count

    @classmethod
    def set_wheel_count(cls,wheel_count):
        cls.wheels_count = wheel_count

    @staticmethod
    def calc_fuel(count):
        return count*5


car1 = Car(name='Audi', color='red')
car2 = Car(name='BMW', color='black')

car1.set_wheel_count(wheel_count=3)
print(car1.get_name())
print(car1.get_color())
print(car1.wheels_count)

print(car2.get_name())
print(car2.get_color())
print(car2.wheels_count)

print(Car.calc_fuel(100))




