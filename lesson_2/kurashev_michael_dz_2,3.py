list_one = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(list_one):
    if list_one[i].isdigit() == True:
        list_one[i] = list_one[i].zfill(2)
        list_one.insert(i, '"')
        list_one.insert(i + 2, '"')
        i = i + 2
    elif list_one[i][:1] in "+-":
        list_one[i] = list_one[i][0] + list_one[i][1:].zfill(2)
        list_one.insert(i, '"')
        list_one.insert(i + 2, '"')
        i = i + 2
    i = i + 1
print(' '.join(list_one))

