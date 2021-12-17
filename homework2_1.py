# -----------------------------Задание 1------------------------------
# class FirstClass:
#     def __init__(self, one, two, three):
#         self.one = one
#         self.two = two
#         self.three = three
#
#     def show_my_var(self):
#         print(self.one)
#         print(self.two)
#         print(self.three)
#
# first_calss = FirstClass(4,6,7)
# first_calss.show_my_var()
# -----------------------------Задание 2------------------------------
# class Monkey:
#
#     max_age = 12
#     loves_bananas = True
#
#     def climb(self):
#         print('I am climbing the tree')
#
# firstmonkey = Monkey()
# secondmonkey = Monkey()
#
# print(firstmonkey.max_age)
# print(firstmonkey.loves_bananas)
#
# print(secondmonkey.max_age)
# print(secondmonkey.loves_bananas)
#
# firstmonkey.climb()
# secondmonkey.climb()
# -----------------------------Задание 3------------------------------
#
# class Person:
#     def __init__(self, name, age, gender):
#
#        self.name = name
#        self.age = age
#        self.gender = gender
#
#     def calculate_age(self, number):
#
#         print(f'Через {number} лет {self.name} исполнится {self.age+number}')
#
# p = Person('John', 23, 'male')
# p.calculate_age(10)
# -----------------------------Задание 4------------------------------
# Вложены отдельными файлами rectangles.py и rectangles_test.py
# -----------------------------Задание 5------------------------------
# Создайте программу для сохранения данных с профиля Facebook в excel файл. В вашей программе должна быть функция,
# которая обрабатывает данные и записывает их в excel файл. Считайте, что данные всегда приходят в виде словаря
# и в нем всегда одинаковые ключи. Учтите, что некторые значения в ключах могут иметь значение None.

# Пример поступающих данных:

import csv

# jason = {'first_name': 'Jason', 'last_name': 'Houston', 'age': 29, 'gender': 'male', 'hobby': 'video games',
#          'job': None}
# alice = {'first_name': 'Alice', 'last_name': 'Cooper', 'age': 21, 'gender': 'female', 'hobby': None,
#          'job': 'software engineer'}

# def write_csv(data):
#     with open('dict.csv', "a") as f:
#         writer = csv.writer(f, delimiter=';')
#         writer.writerow((data['first_name'], data['last_name'], data['age'], data['gender'], data['hobby'], data['job'] ))
#
# write_csv(jason)
# write_csv(alice)

# ---------------------Задача 5 - 2 вариант-----------------
# import pandas as pd
# from openpyxl import load_workbook
#
# jason = {'first_name': 'Jason', 'last_name': 'Houston', 'age': 29, 'gender': 'male', 'hobby': 'video games',
#          'job': None}
# alice = {'first_name': 'Alice', 'last_name': 'Cooper', 'age': 21, 'gender': 'female', 'hobby': None,
#          'job': 'software engineer'}
#
#
# def write_csv(data, data2):
#
#     z = pd.DataFrame(data,index=[0])
#     z.to_excel('dict.xlsx', index=False)
#
#     z = pd.DataFrame(data2,index=[0])
#     book = load_workbook('dict.xlsx')
#     writer = pd.ExcelWriter('dict.xlsx', engine='openpyxl')
#     writer.book = book
#     writer.sheets = {ws.title: ws for ws in book.worksheets}
#     z.to_excel(writer,sheet_name='Sheet1', startrow=writer.sheets['Sheet1'].max_row, index = False,header= False)
#
#     writer.save()
#
# write_csv(jason, alice)