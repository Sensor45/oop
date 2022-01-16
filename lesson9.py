# def is_polindrome(text_):
#     if text_.lower() == text_[::-1].lower():
#         return True
#     else:
#         return False
#
# text = 'Заказ'
# print(is_polindrome(text))
# -------------------------------------------------------------------
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# c = list(set(a) & set(b))
# print(c)
# --------------------------------------------------
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# res = [i for i in a if i in b]
# [6, 7, 8, 9, 10, 7, 8, 9, 10, 11, 8, 9, 10, 11, 12]
#
# print(res)
# ------------------------------------------------------
#
# class Salary():
#
#     def __init__(self, zp):
#         self.zp = zp
#     def get_total(self):
#         return self.zp * 12
#
#
# class Employee():
#     def __init__(self, prof, zp, bonus):
#         self.prof = prof
#         self.zp = zp
#         self.bonus = bonus
#         self.salary = Salary(zp)
#
#     def total_salary(self):
#         print(self.salary)
#         return self.salary.get_total() + self.bonus
#
# a = Employee('Слесарь', 100, 50)
# print(a.total_salary())

def multiply(a, b):
    return a * b

print(multiply(1, 2))



