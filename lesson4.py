class Shape:

    def __init__(self, name):
        self.name = name

    def calc_area(self):
        pass

class Triangle(Shape):
    def __init__(self, a, b, c, h):
        super(Triangle, self).__init__('Triangle')
        self._a = a if a > 0 else 1
        self._b = b if a > 0 else 1
        self._c = c if a > 0 else 1
        self._h = h if a > 0 else 1

    def calc_area(self):
        return (1/2)*self._a*self._h

triangle = Triangle(a=1, b=4, c=7, h=3)
print(triangle.calc_area())


