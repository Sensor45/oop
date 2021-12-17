import unittest
from Car import Car


class TestCar(unittest.TestCase):

    def test_enginestart(self):
        car = Car(2009, 'внедорожник', 'черный')
        self.assertEqual(car.engine_start(), 'Автомобиль заведен')

    def test_enginestop(self):
        car = Car(2009, 'внедорожник', 'черный')
        self.assertEqual(car.engine_stop(), 'Автомобиль заглушен')

    def test_age(self):
        car = Car(2009, 'внедорожник', 'черный')
        self.assertEqual(car.get_age(), f'Год вашего автомобиля: {car.age}')

    def test_type(self):
        car = Car(2009, 'внедорожник', 'черный')
        self.assertEqual(car.get_type(), f'Тип вашего автомобиля: {car.type}')

    def test_color(self):
        car = Car(2009, 'внедорожник', 'черный')
        self.assertEqual(car.get_color(), f'Цвет вашего автомобиля: {car.color}')

if __name__ == '__main__':
    unittest.main()
