
def get_sum(number):

    new_str = str(number)
    new_list = list(new_str)
    sum_number = 0

    for i in new_list:
        sum_number += int(i)

    return sum_number

number = 35732
print(f'Сумма чисел равна: {get_sum(number)}')