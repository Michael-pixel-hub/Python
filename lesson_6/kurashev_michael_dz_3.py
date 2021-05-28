def split_g(list_split, division_end, division_beginning=0):
    if division_beginning == 0:
        split_one = list_split.split(division_end, 1)
        final_result = split_one.pop(0)
        return final_result
    else:
        split_one = list_split.split(division_end, 1)
        split_two = split_one[0].split(division_beginning, 1)
        final_result = split_two.pop()
        return final_result

user_name = """Иванов,Иван,Иванович
Петров,Петр,Петрович
Михаилов,Михаил,Михайлович"""
user_hobby = """Скалолазание,охота"""

#создаем файлы

with open('users.csv', 'w', encoding='utf-8') as file_1:
    file_1.write(user_name)
with open('hobby.csv', 'w', encoding='utf-8') as file_2:
    file_2.write(user_hobby)

#читаем файлы

with open('users.csv', 'r', encoding='utf-8') as file_1:
    content = file_1.read()
    content = content.replace(',', ' ')
    content = content.replace('\n', ',')
    list_name = content.split(',')
    print(list_name)
with open('hobby.csv', 'r', encoding='utf-8') as file_2:
    content = file_2.read()
    list_hobby = content.split(',')
    print(list_hobby)

#создаем словарь

dictionary_name = {

    }

for i in range(len(list_name)):
    if len(list_name) < len(list_hobby):
        print('1')
    else:
        if i < len(list_hobby):
            dictionary_name[list_name[i]] = list_hobby[i]
        else:
            dictionary_name[list_name[i]] = None

print(dictionary_name)

