import os

def get_dirfiles(dir):
    result_dict = {}
    list_files = []
    for i in dir:
        for j in i[2]:
            list_files.append(j)

    return list_files

find_files = 'dict.xlsx'
dir = os.walk('C:/Users/User/OneDrive/Desktop/oop/test/')

print(list(filter(lambda x: find_files == x, get_dirfiles(dir))))
