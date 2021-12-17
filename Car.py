class Car:
    def __init__(self, age, type, color):
        self.color = color
        self.type = type
        self.age = age

    def engine_start(self):
        return 'Автомобиль заведен'

    def engine_stop(self):
        return 'Автомобиль заглушен'

    def get_age(self):
        return f'Год вашего автомобиля: {self.age}'

    def get_type(self):
        return f'Тип вашего автомобиля: {self.type}'

    def get_color(self):
        return f'Цвет вашего автомобиля: {self.color}'


car = Car(2009, 'внедорожник', 'черный')

print(car.engine_start())
print(car.engine_stop())
print(car.get_age())
print(car.get_type())
print(car.get_color())