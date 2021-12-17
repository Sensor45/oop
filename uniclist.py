def get_uniclist(list):

    setlist = set(list)
    if len(list) == len(setlist):
        return 'Все элементы уникальны'
    else:
        return 'Есть одинаковые'

list = [1, 2, 3, 4, 5]
print(get_uniclist(list))
list = [1, 2, 3, 2, 1]
print(get_uniclist(list))