import sys
user_list = sys.argv[1:]
with open('bakery.csv', 'r', encoding='utf-8') as file_1:
    if len(user_list) == 2: #создаем условие, если человек ввел два значения
        user_number_start = int(user_list[0]) #с какого числа нужно показывать элементы файла
        user_number_end = int(user_list[1]) #по какое число нужно показывать элементы файла
        for i in range(user_number_start - 1): #читаем файл до точки, с которой нужно показывать значения файла
            file_1.readline()
        list_user = file_1.readlines()[:user_number_end-1] #создаем список значений файла, которые нужно показать
        list_user = ''.join(list_user) #соединяем список в нужный формат
        print(list_user) #выводим информацию
    elif len(user_list) == 1: #создаем условие, если человек ввел одно значение
        user_number_start = int(user_list[0])
        for i in range(user_number_start - 1):
            file_1.readline()
        print(file_1.read())
    elif len(user_list) == 0: #создаем условие, если человек ввел 0 условий
        print(file_1.read())
    else: #ничего не происходит, если ввел что-то другое
        pass



