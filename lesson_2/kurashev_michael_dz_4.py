list_one = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
            'директор аэлита']
i = 0
while i < len(list_one):
    split_list = list_one[i].split()
    cut_list = split_list.pop(-1)
    cut_list = cut_list.capitalize()
    print(f'Привет, {cut_list}')
    i = i + 1
