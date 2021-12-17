'''Здесть документация на модуль'''

class Salary:

    '''Здесь документация на класс'''

    def __init__(self,pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Employee:

    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(pay=self.pay)

    def annual_selary(self):
        return f'Total {self.salary.get_total() + self.bonus}'



employee = Employee(10,100)
print(employee.annual_selary())
