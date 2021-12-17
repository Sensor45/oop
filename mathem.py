class Mathem:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def substruction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

mathem = Mathem(10, 2)

print(f'{mathem.a} + {mathem.b} = {mathem.addition()}')
print(f'{mathem.a} - {mathem.b} = {mathem.substruction()}')
print(f'{mathem.a} * {mathem.b} = {mathem.multiplication()}')
print(f'{mathem.a} / {mathem.b} = {mathem.division()}')