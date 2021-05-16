def thesaurus(*name_employee):
    list_finish = {} #создаем словарь
    letters = [] #создаем массив, в котором будем хранить первые буквы имен
    index = 0 #создаем индекс для работы с массивом
    for i in name_employee:
        letters.append(i[0]) #добавляем первую букву имени в массив
        list_finish.setdefault(letters[index], []) #добавляем и используем буквы из массива в словарь как ключ
        list_finish[letters[index]].append(i) #добавляем значение к ключу
        index += 1
    print(list_finish)

thesaurus("Мися", "Мама", "Влядя")