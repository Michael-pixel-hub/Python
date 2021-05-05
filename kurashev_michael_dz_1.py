user_number = int(input('Введите кол-во секунд: '))

year = user_number // 31040000
user_number = user_number - year * 31040000
month = user_number // 2592000
user_number = user_number - month * 2592000
day = user_number // 86400
user_number = user_number - day * 86400
hour = user_number // 3600
user_number = user_number - hour * 3600
minutes = user_number // 60
user_number = user_number - minutes * 60

print(f'{year} лет {month} мес {day} дн {hour} час {minutes} мин {user_number} сек')
print(8%7)