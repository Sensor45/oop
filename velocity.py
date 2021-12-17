# Напишите тесты для следующей функции
# Тесты должны проверять правильный ли результат отдаёт функция. Принимает ли функция правильные аргументы.

def calculate_average_velocity(*args):
    velocity_sum = 0
    other_type = 0
    for i in args:
        try:
            velocity_sum += i
        except TypeError:
            other_type += 1
            continue
    return velocity_sum / (len(args)-other_type)

print(calculate_average_velocity(100,200,300,400))