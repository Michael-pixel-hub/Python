def generator_list(list_one, list_two):
    for i in range(len(list_one)):
        if len(list_two) > i:
            yield (list_one[i], list_two[i])
        else:
            yield (list_one[i], None)

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '9В', '8Б']

final_list = generator_list(tutors, klasses)
for i in range(len(tutors)):
    print(next(final_list))
print(type(final_list))