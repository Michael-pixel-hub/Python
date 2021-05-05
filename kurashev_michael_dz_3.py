user_percent = int(input("Задайте процент: "))
if user_percent == 1:
    print(f'{user_percent} процент')
elif user_percent > 1 and user_percent <= 4:
    print(f'{user_percent} процента')
elif user_percent > 4 and user_percent <= 20:
    print(f'{user_percent} процентов')