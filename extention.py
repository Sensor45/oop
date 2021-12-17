import os

def get_extention(dir):
    result_dict = {}
    list_files = []
    for i in dir:
        for j in i[2]:
            list_files.append(j)

    for i in list_files:
        name_file = os.path.splitext(i)
        result = name_file[1].replace('.','')
        if result == '':
            result = 'расширение отсутствует'

        result_dict[i] = result
    return result_dict

dir = os.walk('C:/Users/User/OneDrive/Desktop/oop/test/')
print(get_extention(dir))