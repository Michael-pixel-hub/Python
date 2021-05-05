list_namber = []

for i in range(1, 1001, 2):
    list_namber.append(i**3) #сделал список нечетных чисел, возведенных в 3 степень (от 1 до 1000)

sum_total = 0

for i in list_namber:
    sum_namber = 0
    new_namber = i
    while new_namber > 0: #делю число на составляющие числа и складываю их
        a = new_namber % 10
        sum_namber = sum_namber + a
        new_namber = new_namber // 10
        if sum_namber % 7 == 0: #проверяю число на деление нацело на 7 и суммирую это число с итоговым
            sum_total = sum_total + i

print(sum_total)

sum_total = 0 #обнуляю переменную

for i in list_namber:
    sum_namber = 0
    new_namber = i + 17 #прибавляю к каждому элементу списка 17
    while new_namber > 0: #делю число на составляющие числа и складываю их
        a = new_namber % 10
        sum_namber = sum_namber + a
        new_namber = new_namber // 10
        if sum_namber % 7 == 0: #проверяю число на деление нацело на 7 и суммирую это число с итоговым
            sum_total = sum_total + i

print(sum_total)



