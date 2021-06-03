import os

def folder_file_size(dir_path):
    vocabulary_stat = {

    }
    key_value = 0
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            path_file = os.path.join(root, file) # получаем путь файла
            file_size = os.path.getsize(path_file) # получаем размер файла
            threshold = 10 ** len(str(file_size)) # получаем ключ число
            vocabulary_stat[threshold] = key_value + 1 # создаем ключ и значение в словаре
            key_value = vocabulary_stat.get(threshold)
    print(vocabulary_stat)

folder_file_size('D:\Program Files\PyCharm\pythonProject\my_project')