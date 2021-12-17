import os

def get_dirfiles(dir):
    result_dict = {}
    list_files = []
    for i in dir:
        for j in i[2]:
            list_files.append(j)

    return list_files

dir = os.walk('C:/Users/User/OneDrive/Desktop/oop/test/')
print(get_dirfiles(dir))