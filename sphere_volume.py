import math

pi = math.pi #Число Пи. Примерно, равное 3.141592653589793

def calculate_sphere_volume(r):
    try:
        r = float(r)
    except:
        raise ValueError()
    if r < 0:
        return 'Радиус сферы не может быть отрицательным'
    return 4/3*pi*r**3

print(calculate_sphere_volume(3.7))