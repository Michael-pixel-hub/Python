list_one = []
i = 1
while i < 21:
    a = input(f'Введите цену на товар № {i}: ')
    list_one.append(a)
    i = i + 1
print(', '.join(list_one))
