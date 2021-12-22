# --------------------------------------------Задача 1-------------------------------------------------------
# Создайте аналог телефонной книги. Каждая запись в книге должна иметь идентификационный номер, имя, фамилия,
# дату рождения, профессию. Напишите для этого класса метод get_information которая будет выдавать информацию
# об экземпляре этого класса.
#
# Пример входных данных:
# ID - 1 Full name - John Dow Birth Date - 21.04.1996 Profession - Python developer

# from datetime import date

#
# class Contact:
#     def __init__(self, id, first_name, last_name, birth_date, profession):
#         self.id = id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birth_date = birth_date
#         self.profession = profession
#
#     def get_information(self):
#         return f'ID - {self.id}, Full name - {self.first_name} {self.last_name}, Birth Date - {self.birth_date}, Profession - {self.profession}'
#
# c = Contact(id=1, first_name='John', last_name='Dow', birth_date=date(day=21, month=4, year=1996), profession='Python developer')
#
# print(c.get_information())

# --------------------------------------------Задача 2-------------------------------------------------------
# Создайте иерархию классов для описания фауны со следующими требованиями:
# Обязательное присутствие классов птиц, рыбы и млекопитающих. Напишите для них методы и парамметры свойственные
# для животных этих классов. Так же обязательное присутствие классов хищников и травоядных. У классов хищник и травоядное
# обязательно должен быть метод eat. Этот метод должен показывать, чем питается животное.
#
# Создайте классы сокол, пингвин, форель, кит. Наследуйте эти классы от вышеуказанных классов, при наследовании
# обратите внимание на природные свойства животных этих классов. Если есть необходимость, перепишите методы родителя
# для того чтобы эти методы соответствовали свойствам животного. Создайте экземпляры классов сокол, пингвин, форель, кит.
# Вызовите все доступные им методы
# Пример:
# >>>p = Penguin(type='royal', age='1 year') >>>p.eat() I eat fish >>>p.can_swim() True >>>p.can_fly() I cannot fly
#
#
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
#         return 'I can swim'
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
# --------------------------------------------Задача 3-------------------------------------------------------
# Решение в стороннем файле velocity и velovity_test
# --------------------------------------------Задача 4-------------------------------------------------------
# Решение в стороннем файле sphere_volume.py и test_sphere_volume.py
