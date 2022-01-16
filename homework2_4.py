# ------------------------------------------------- Задание 1 --------------------------------------------------
# Создайте иерархию классов для описания фауны со следующими требованиями:
# Обязательное присутствие классов птиц, рыбы и млекопитающих. Напишите для них методы и парамметры свойственные для
# животных этих классов. Так же обязательное присутствие классов хищников и травоядных. У классов хищник и травоядное
# обязательно должен быть метод **eat**. Этот метод должен показывать, чем питается животное.
# Создайте классы сокол, пингвин, форель, кит. Наследуйте эти классы от вышеуказанных классов, при наследовании
# обратите внимание на природные свойства животных этих классов. Если есть необходимость, перепишите методы родителя
# для того чтобы эти методы соответствовали свойствам животного. Создайте экземпляры классов сокол, пингвин, форель, кит.
# Вызовите все доступные им методы
#
# **Пример:**
#
# ```python
# >>>p = Penguin(type='royal', age='1 year')
# >>>p.eat()
# I eat fish
# >>>p.can_swim()
# True
# >>>p.can_fly()
# I cannot fly
# ```
# ----------------Ниже код решения --------------------
# class Fish():
#
#     def swim(self):
#         return 'I can swim'
#
# class Bird():
#
#     def lay_eggs(self):
#         return 'I lay eggs'
#
# class FlyingBird(Bird):
#
#     def fly(self):
#         return 'I can fly'
#
# class Mammals():
#
#     def drink_milk(self):
#         return 'I drink milk'
#
# class Predator():
#
#     def eat(self):
#         return 'I eat other animals'
#
# class Herbivore():
#
#     def eat(self):
#         return 'I eat grass'
#
# class Falcon(FlyingBird, Predator):
#     def __init__(self, type, age):
#         self.type = type
#         self.age = age
#
#     def eat(self):
#         return 'I eat little animals'
#     def can_fly(self):
#         return 'I can Fly'
#
# class Penguin(Bird, Predator):
#     def __init__(self, type, age):
#         self.type = type
#         self.age = age
#
#     def eat(self):
#         return 'I eat fish'
#     def can_swim(self):
#         return 'I can swim' # Можно вернуть True
#     def can_fly(self):
#         return 'I cannot Fly'
#
#
# class Trout(Fish, Predator):
#     def __init__(self, type, age):
#         self.type = type
#         self.age = age
#
#     def eat(self):
#         return 'I eat other fish'
#
# class Whale(Mammals, Predator):
#     def __init__(self, type, age):
#         self.type = type
#         self.age = age
#
#     def eat(self):
#         return 'I eat fish'
#
# p = Penguin(type='royal', age='1 year')
#
# print(p.eat())
# print(p.can_swim())
# print(p.can_fly())
# print(p.lay_eggs())


# ---------------------------------------------- Задание 2 -----------------------------------------------------
#
# Вам дана функция:
#
# ```python
# def show_even_numbers(*args):
# 	even_numbers_lst = []
# 	for i in args:
# 		try:
# 			if i%2 == 0:
# 				even_numbers_lst.append(i)
# 		except TypeError:
# 			continue
# 	return even_numbers_lst
# ```
#
# Напишите декоративную функцию для этой функции чтобы выводить каждое чётное число введённое в эту функцию раздельно,
# а так же указывать каким номером вы их получили.
#
# **Пример выходных данных:**
#
# ```python
# >>>show_even_numbers(3, 8, 'hello', 100, [14, 13, 12], 12)
# 1 - 8
# 2 - 100
# 3 - 12
# ```
# ----------------Ниже код решения --------------------
# def decorator_function(show_even_numbers):
#     def wrapper(*args):
#         list = show_even_numbers(*args)
#         for i in range(len(list)):
#             print(f'{i+1} - {list[i]}')
#
#     return wrapper
#
# @decorator_function
# def show_even_numbers(*args):
#     even_numbers_lst = []
#     for i in args:
#         try:
#             if i % 2 == 0:
#                 even_numbers_lst.append(i)
#         except TypeError:
#             continue
#     return even_numbers_lst
#
# show_even_numbers(3, 8, 'hello', 100, [14, 13, 12], 12)


# -------------------------------------------- Задание 3 ----------------------------------------------------
#
# Создать интерфейс для сравнения геометрических фигур
#
# Создайте абстрактный класс **Shape** В нем должен быть абстрактный метод calculate_area. В наследуемых классах
# этот метод должен будет высчитывать площадь фигуры и сохранять результат в параметр экземпляра класса area.
# Создайте 3 класса: **Rectangle, Triangle, Circle** . Наследуйте их от класса **Shape**
#
# Класс **Rectangle:** При инициализации должен принять 2 обязательных аргумента length, height. Площадь должна
# определяться умножением этих сторон.
#
# ```python
# ...
# self.area = self.length*self.height
# ...
# ```
#
# Класс **Triangle**: При инициализации должен принять 2 обязательных аргумента length, height. Площадь должна
# определяться умножением этих сторон деленным на 2
#
# ```python
# ...
# self.area = self.length*self.height/2
# ...
# ```
#
# Класс **Circle**: При инициализации должен принять 1 обязательный аргумент radius. Площадь должна определяться
# формулой: (число Пи)*radius**2. Для простоты можете использовать значение числа Пи = 3.14
#
# ```python
# ...
# pi = 3.14
# self.area = pi*self.radius**2
# ...
# ```
#
# У каждого экземпляра любого из 3 классов должен быть приватный параметр __color. Если он не задается при инициализации,
# он должен быть равен **"black"**. Так же подумайте над методом, который смог бы показывать цвет фигуры
#
# Реализуйте протоколы сложения, вычитания и сравнения для всех фигур. Во всех случаях должен использоваться параметр
# area этих фигур. Если при вызове одного из этих протоколов у фигуры нет этого параметра, он должен высчитаться и
# потом реализовать функционал протокола. Примите во внимание, при реализации протокола вычитания, если у уменьшаемого
# объекта площадь меньше чем у вычитаемого, то должна вызваться ошибка ArithmeticError
#
# Создайте тестовый модуль. Импортируйте в него ваши классы фигур и используя модуль unittest, создайте экземпляры
# классов **Rectangle, Triangle, Circle**. Напишите тесты на  сложение, вычитание и сравнение каждого экземпляра с
# двумя другими. Напишите тесты проверяющие показ цвета каждого из экземпляров. Создайте новый экземпляр
# класса **Rectangle**, цвет этого экземпляра должен быть **"red"**. Напишите тесты на подтверждение того, что цвет
# этого экземпляра **"red"**.
#
# ----------------Ниже код решения --------------------
# class Shape:
#
#     def calculate_area():
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, length, height,__color='black'):
#         self.length = int(length)
#         self.height = int(height)
#         self.__color = __color
#
#     def calculate_area(self):
#         self.area = self.length * self.height
#         return self.length * self.height
#
#     def show_color(self):
#         return self.__color
#
#
# class Triangle(Shape):
#     def __init__(self, length, height, __color='black'):
#         self.length = int(length)
#         self.height = int(height)
#         self.__color = __color
#
#     def calculate_area(self):
#         self.area = self.length * self.height / 2
#         return self.area
#
#     def show_color(self):
#         return self.__color
#
#
# class Circle(Shape):
#     def __init__(self, radius, __color='black'):
#         self.radius = int(radius)
#         self.__color = __color
#         self.pi = 3.14
#
#     def calculate_area(self):
#         self.area = self.pi * self.radius**2
#         return self.area
#
#     def show_color(self):
#         return self.__color
#
# def protocol_addition():
#     rectangle_plus_triangle = a.area+b.area
#     rectangle_plus_circle = a.area+c.area
#     triangle_plus_circle = b.area+c.area
#     print(f' Cумма площяди пямоугольника и треугольника: {rectangle_plus_triangle}, cумма площяди пямоугольника и ' \
#            f' круга: {rectangle_plus_circle}, cумма площяди триугольника и круга: {triangle_plus_circle}!')
#
# def protocol_subtraction():
#     rectangle_minus_triangle = a.area - b.area
#     if rectangle_minus_triangle < 0:
#         raise ArithmeticError
#     else:
#         print(f'Разница площяди пямоугольника и треугольника: {rectangle_minus_triangle}')
#
#     triangle_minus_rectangle = b.area - a.area
#     if triangle_minus_rectangle < 0:
#         raise ArithmeticError
#     else:
#         print(f'Разница площяди треугольника  прямоугольника: {triangle_minus_rectangle}')
#
#     rectangle_minus_circle = a.area - c.area
#     if rectangle_minus_circle < 0:
#         raise ArithmeticError
#     else:
#         print(f'Разница площяди пямоугольника и круга: {rectangle_minus_circle}')
#
#     circle_minus_rectangle = c.area - a.area
#     if circle_minus_rectangle < 0:
#         raise ArithmeticError
#     else:
#         print(f'Разница площяди круга и прямоугольника: {circle_minus_rectangle}')
#
#     triangle_minis_circle = b.area - c.area
#     if triangle_minis_circle < 0:
#         raise ArithmeticError
#     else:
#         print(f'Разница площяди треугольника и круга: {triangle_minis_circle}')
#
#     circle_minis_triangle = c.area - b.area
#     if circle_minis_triangle < 0:
#         raise ArithmeticError
#
#     else:
#         print(f'Разница площяди круга и треугольника: {circle_minis_triangle}')
#
# def protocol_comparisons():
#     if a.area < b.area:
#         print(f'Площядь прямоугольника меньше площяди треугольника')
#     elif a.area > b.area:
#         print(f'Площядь прямоугольника больше площяди треугольника')
#     else:
#         print(f'Площядь прямоугольника и треугольника равны')
#
#     if a.area < c.area:
#         print(f'Площядь прямоугольника меньше площяди круга')
#     elif a.area > c.area:
#         print(f'Площядь прямоугольника больше площяди круга')
#     else:
#         print(f'Площядь прямоугольника и круга равны')
#
#     if b.area < c.area:
#         print(f'Площядь триугольника меньше площяди круга')
#     elif b.area > c.area:
#         print(f'Площядь триугольника больше площяди круга')
#     else:
#         print(f'Площядь триугольника и круга равны')
#
#
# a = Rectangle('2', '2')
# b = Triangle('3', '4', 'red')
# c = Circle('2', 'blue')
#
# print(a.show_color())
# print(b.show_color())
# print(c.show_color())
#
# print(a.calculate_area())
# print(b.calculate_area())
# print(c.calculate_area())
#
# protocol_addition()
# protocol_comparisons()
# protocol_subtraction()
#


# -------------------------------------------------Задание 4--------------------------------------------------
#
# Создайте класс для даты **MyCustomDate**, который при инициализации принимает такие параметры, как **день, месяц,
# год.** Переопределите следующие магические (служебные) методы:
#
# - Метод отображения объекта **__str__**
# - Методы для сравнения разных дат **__eq__,  __ne__, __lt__, __gt__, __le__, __ge__**
# - Методы сложения **__add__** и вычитания **__sub__**, которые должны выдавать количество дней между датами.
# Результат должен быть положительным целым числом. Для упрощения задачи можете принять, что в каждом месяце
# 30 дней, а в году 360 дней.
#
# Создайте 5 дат, используя созданный ранее класс **MyCustomDate**. Проверьте, корректно ли работают магические
# методы, сравнив даты с использованием всех операторов сравнения: **==, !=, >, <, >=, <=**. Также сложите 2 даты
# и вычтите одну дату из другой, тем самым проверив работу магических методов сложения и вычитания
# **__add__**, **__sub__**.
# ----------------Ниже код решения --------------------

# from datetime import datetime
#
# class MyCustomDate():
#
#
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def __str__(self,*args, **kwargs):
#         return f'{datetime(self.year, self.month, self.day)}'
#
#     def __gt__(self, other):
#         return datetime(self.year, self.month, self.day) > datetime(other.year, other.month, other.day)
#
#     def __lt__(self, other):
#         return datetime(self.year, self.month, self.day) < datetime(other.year, other.month, other.day)
#
#     def __ge__(self, other):
#         return datetime(self.year, self.month, self.day) >= datetime(other.year, other.month, other.day)
#
#     def __le__(self, other):
#         return datetime(self.year, self.month, self.day) <= datetime(other.year, other.month, other.day)
#
#     def __add__(self, other):
#         return abs(datetime(self.year, self.month, self.day) - datetime(other.year, other.month, other.day))
#
#     def __sub__(self, other):
#         return abs(datetime(self.year, self.month, self.day) - datetime(other.year, other.month, other.day))
#
#
# date1 = MyCustomDate(4,5,2021)
# date2 = MyCustomDate(30,6,2000)
# date3 = MyCustomDate(22,2,2022)
# date4 = MyCustomDate(5,7,2012)
# date5 = MyCustomDate(1,12,2002)
#
# print(date1)
# print(date2)
# print(date3)
# print(date4)
# print(date5)
#
# print(date1 - date2)
# print(date2 + date1)
#
# print(date1>date2)
#

# ------------------------------------------------------- Задание 5----------------------------------------------
#
# Используя парадигмы композиции и наследования в ООП, создайте систему мониторинга офисной работы АйТи компании.
# В вашей системе должно быть разделение на 3 типа работников: Frontend, Backend, Management. Общими чертами всех
# работников является то, что у каждого из них есть имя, фамилия, заработная плата и возможность отметить какую-то
# одну дату для полученя отгула(реализуйте методом).
#
# Backend и Frontend  работники должны иметь аттрибут experience - который бы говорил об уровне опыта этого
# разработчика (Junior, Middle, Senior).
#
#  Frontend работник должен иметь метод visualize - который будет в выводить на экран текст:
# '*Making visual appearance of project*'. Backend работник должен иметь метод **set_up_db** - который будет выводить
# на экран текст: '*Setting up database of project*'. Сделайте оба эти метода статичными.
#
# У класса Management должен быть аттрибут **rank** - который бы говорил о занимаемой должности
# менеджмера(CEO, HR-manager, Project-manager). Так же реализуйте классовый метод fire. Этот метод аргументом
# должен принимать экземпляр другого класса, и, если это экземпляр класса Frontend или Backend, удалять его.
#
# Реализуйте класс Project, для мониторинга проектов компании. В проекте обязательно должен быть один представитель
# менеджмента, 1 старший Frontend разработчик(senior). 1 старший Backend разработчик(senior). Несколько обычных Backend
# и Frontend разработчиков. У экземпляра этого класса должен быть метод **check_backend**, который циклом проходится
# по всем backend разработчикам в этом проекте, выводит на экран имя каждого и вызывает метод **set_up_db** для каждого
# из них. Так же должен быть метод **check_frontend**, который циклом проходится по всем frontend разработчикам, выводит
# на экран имя каждого и вызывает метод **visualize** для каждого из них.
# ----------------Ниже код решения --------------------
# from datetime import datetime
#
# class Employee():
#
#     def __init__(self, first_name, second_name, salary, day_off):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.salary = salary
#         self.day_off = day_off
#
# class Frontend_employee(Employee):
#
#     def __init__(self, first_name, second_name, salary, day_off, experience):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.salary = salary
#         self.day_off = day_off
#         self.experience = experience
#
#     def visualize(self):
#         print('Making visual appearance of project')
#
#
# class Beckend_employee(Employee):
#
#     def __init__(self, first_name, second_name, salary, day_off, experience):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.salary = salary
#         self.day_off = day_off
#         self.experience = experience
#
#     def set_up_db(self):
#         print('Setting up database of project')
#
#
# class Management_employee(Employee):
#
#     def __init__(self, first_name, second_name, salary, day_off, rank):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.salary = salary
#         self.day_off = day_off
#         self.rank = rank
#
# class Project():
#
#     @classmethod
#     def fire(cls):
#         if cls == Frontend_employee or cls == Beckend_employee:
#             del cls
#
#     managment = Management_employee('John', 'Doe', 1000, datetime(2022,2,20),'CEO')
#     frontend_senior = Frontend_employee('Alex', 'Smith', 1000, datetime(2022,3,22),'senior')
#     backend_senior = Beckend_employee('Alan', 'Delon', 1000, datetime(2022,4,2),'senior')
#     frontend1 = Frontend_employee('Aman', 'Ishenbekov', 500, datetime(2022,5,12),'junior')
#     frontend2 = Frontend_employee('Almaz', 'Mokoev', 700, datetime(2022,6,30),'middle')
#     backend1 = Beckend_employee('Jane', 'Jonson', 500, datetime(2022,7,5),'junior')
#     backend2 = Beckend_employee('Sharon', 'Stone', 700, datetime(2022,8,7),'middle')
#
#     frontend_employee = [frontend_senior,frontend1,frontend2]
#     backend_employee = [backend_senior, backend1, backend2]
#
#     def check_backend(self):
#         for x in Project.backend_employee:
#             print(x.first_name)
#             x.set_up_db()
#
#     def check_frontend(self):
#         for x in Project.frontend_employee:
#             print(x.first_name)
#             x.visualize()
#
# project1 = Project()
# project1.check_backend()
# project1.check_frontend()

# ------------------------------------------------------- Задание 6----------------------------------------------
#
# Вам дана функция:
#
# ```python
# def advanced_search(integer_lst, searched_value):
# 	if not isinstance(searched_value, int):
# 		raise ValueError('Arguments should be integers')
#
# 	for i in integer_lst:
# 		if not isinstance(i, int):
# 			raise ValueError('Arguments should be integers')
#
# 	integer_set = set(integer_lst)
# 	new_lst = list(integer_set)
# 	if not searched_value in new_lst:
# 		result_index = -1
# 	else:
# 		result_index = new_lst.index(searched_value)
#
# 	return new_lst, result_index
# ```
#
# И вам дается вторая функция:
#
# ```python
# def search(integer_lst, searched_value):
# 	return searched_value in integer_lst
# ```
#
# Напишите декоратор для второй функции чтобы при вызове обеих функций с одинкавоыми параметрами они выдавали
# одинкавый результат:
#
# ```python
# >>>lst = [-3, 7, -3, 13, -4, 1, 10, 3, 19, 6, 12, 13, 3, 6, 19, 22, 25, 21, 11, 3]
#
# >>>print(advanced_search(lst, 3))
# ([1, 3, 6, 7, 10, 11, 12, 13, 19, 21, 22, 25, -4, -3], 1)
# >>>print(search(lst, 3))
# ([1, 3, 6, 7, 10, 11, 12, 13, 19, 21, 22, 25, -4, -3], 1)
# ```
# ----------------Ниже код решения --------------------
# def advanced_search(integer_lst, searched_value):
#     if not isinstance(searched_value, int):
#         raise ValueError('Arguments should be integers')
#
#     for i in integer_lst:
#         if not isinstance(i, int):
#             raise ValueError('Arguments should be integers')
#
#     integer_set = set(integer_lst)
#     new_lst = list(integer_set)
#     if not searched_value in new_lst:
#         result_index = -1
#     else:
#         result_index = new_lst.index(searched_value)
#
#     return new_lst, result_index
#
# def decorator_function(search):
#     def wrapper(integer_lst, searched_value):
#         if not isinstance(searched_value, int):
#             raise ValueError('Arguments should be integers')
#
#         for i in integer_lst:
#             if not isinstance(i, int):
#                 raise ValueError('Arguments should be integers')
#
#         integer_set = set(integer_lst)
#         new_lst = list(integer_set)
#         if not searched_value in new_lst:
#             result_index = -1
#         else:
#             result_index = new_lst.index(searched_value)
#
#         return new_lst, result_index
#
#     return wrapper
#
# @decorator_function
# def search(integer_lst, searched_value):
#     return searched_value in integer_lst
#
# lst = [-3, 7, -3, 13, -4, 1, 10, 3, 19, 6, 12, 13, 3, 6, 19, 22, 25, 21, 11, 3]
#
# print(advanced_search(lst, 3))
#
# print(search(lst, 3))


# ------------------------------------------------------- Задание 7----------------------------------------------
#
# Создать класс Person. У экземпляров данного класса должно быть одно поле **name**, которое будет присваиваться
# пользователем при создании. Напишите этому классу метод show_name. Этот метод должен возвращать строку
# '**My name is {имя}**' (имя - **name** экземпляра класса). Создайте 3 экземпляра этого класса. Напишите
# функцию, принимающую производное количество аргументов и используя конструкцию try ... except вызывает метод
# show_name у каждого своего аргумента. Если вызвать метод show_name не получается должен выводиться текст
# "**У данного аргумента нет имени**". Вызовите эту функцию, аргументами возьмите 3 созданных раннее экземпляра
# класса Person.
#
# **Пример**:
#
# ```python
# >>>john = Person('John')
# >>>alice = Person('Alice')
# >>>charlie = Person('Charlie')
#
# >>>func(john, alice, charle)
# My name is John
# My name is Alice
# My name is Charlie
# ```
# ----------------Ниже код решения --------------------
#
# class Person():
#
#     def __init__(self, name):
#         self.name = name
#
#     def show_name(self):
#         print(f'My name is {self.name}')
#
# def func(*args):
#     for i in args:
#         try:
#             i.show_name()
#         except:
#             print('У данного аргумента нет имени')
#
# john = Person('John')
# alice = Person('Alice')
# charlie = Person('Charlie')
#
# func(john, alice, charlie)


# ------------------------------------------------------- Задание 8----------------------------------------------
#
# Создайте класс **Pizza**, которая будет иметь атрибуты: name, ingredients. name - строка, в которой будет хранится
# название экземпляра. ingredients - список из строк. Оба атрибута должны приниматься от пользователя при создании
# экземпляра класса. Напишите для этого класса классовый метод  margarita, которая будет создавать экземпляр
# класса **Pizza** с name = 'Margarita' и ingredients = ['mozarella', 'tomatos', 'olives']. Так же напишите статичный
# метод calculate_area, который будет принимать один парамметр - radius, и высчитывать площадь пиццы(пицца - это
# круг, и площадь будет вычисляться формулой pi*radius**2, где pi - число Пи (для простоты считайте его равным 3.14))
#
# Вызовите у класса метод **margarita**  и сохраните его в переменную. Высчитайте у этого экземпляра класса
# площадь при радиусе 50
#
# **Пример выходных данных:**
#
# ```python
# >>>marg = Pizza.margraita()
# >>>marg.name
# 'Margarita'
# >>>marg.igredients
# ['mozarella', 'tomatos', 'olives']
# >>>marg.calculate_area(radius=50)
# 7850.0
# ```
# ----------------Ниже код решения --------------------
#
# class Pizza:
#     def __init__(self, name, ingredients):
#         self.ingredients = ingredients
#         self.name = name
#         self.ingredients = ingredients
#
#     @classmethod
#     def margarita(cls):
#         mar = Pizza(name='Margarita', ingredients=['mozarella', 'tomatos', 'olives'])
#         return mar
#     @staticmethod
#     def calculate_area(radius):
#         pi = 3.14
#         return pi * radius ** 2
#
# marg = Pizza.margarita()
#
# print(marg.name)
# print(marg.ingredients)
# print(marg.calculate_area(radius=50))
