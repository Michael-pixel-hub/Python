import os


def creating_folder_structure():
    starter = """|--my_project:
   |--settings:
      |--__init__.py
      |--dev.py
      |--prod.py
   |--mainapp:
      |--__init__.py
      |--models.py
      |--views.py
      |--templates:
         |--mainapp:
            |--base.html
            |--index.html
   |--authapp:
      |--__init__.py
      |--models.py
      |--views.py
      |--templates:
         |--authapp:
            |--base.html
            |--index.html"""

    with open('config.yaml', 'w', encoding='utf-8') as file_1:
        file_1.write(starter)

    with open('config.yaml', 'r', encoding='utf-8') as file:
        current_folder_path = os.path.abspath('')
        # создаем путь к текущей директории, чтобы создавать папки и файлы
        past_nest = 0
        # отслеживаем глубину директорий и файлов, чтобы понимать где мы находились в прошлый раз
        for line in file:
            # создаем цикл чтения по строчно
            folder_file_name = line.strip(' |-\n:')
            # создаем полноценное имя папки или файла
            current_nest = line.index('|')
            # отслеживаем глубину директорий и файлов, чтобы понимать где мы находимся в данный момент
            if line.endswith(':\n'):
                # определяем папка это или файл (папка)
                if current_nest == past_nest * 3:
                    # если не двигаемся по иерархии
                    if current_nest > 0:
                        current_folder_path = '\\'.join(current_folder_path.split('\\')[:-1])
                    current_folder_path = '\\'.join((current_folder_path, folder_file_name))
                elif current_nest > past_nest * 3:
                    # если двигаемся вниз
                    current_folder_path = '\\'.join((current_folder_path, folder_file_name))
                    past_nest += 1
                else:
                    # если двигаемся вверх
                    past_nest = int(current_nest / 3)
                    # получили индекс
                    current_folder_path = '\\'.join(current_folder_path.split('\\')[:-current_nest])
                    # получили адрес нашей глубины директории
                    current_folder_path = '\\'.join((current_folder_path, folder_file_name))
                    # получили готовый адрес
                if not os.path.exists(current_folder_path):
                    # создаем проверку
                    os.mkdir(current_folder_path)
            else:
                # определяем папка это или файл (файл)
                name_file = '\\'.join((current_folder_path, folder_file_name))
                # создаем путь к файлу
                if not os.path.exists(name_file):
                    open(name_file, 'w').close()
                    # делаем проверку и создаем файл


if __name__ == '__main__':
    creating_folder_structure()
