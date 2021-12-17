class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):

        if isinstance(self.a, str) or isinstance(self.b, str) or isinstance(self.c, str):
            return "Нужно вводить только числа!"

        elif self.a < 0 or self.b < 0 or self.c < 0:
            return "С отрицательными числами ничего не выйдет!"

        elif self.a + self.b < self.c or self.a + self.c < self.b or self.b + self.c < self.a:
            return "Жаль, но из этого треугольник не сделать"

        elif self.a > 0 and self.b > 0 and self.c > 0:
            return "Ура, можно построить треугольник!"

triangle1 = TriangleChecker(a=5, b=5, c=5)
triangle2 = TriangleChecker(a=-5, b=-5, c=-5)
triangle3 = TriangleChecker(a='r', b='r', c='t')
triangle4 = TriangleChecker(a=5, b=200, c=5)


print(triangle1.is_triangle())

print(triangle2.is_triangle())

print(triangle3.is_triangle())

print(triangle4.is_triangle())



