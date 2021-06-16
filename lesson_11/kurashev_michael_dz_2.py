class Zero(Exception):
    def __init__(self, text):
        self.number = text


user_number = int(input('Введите положительное число: '))

try:
    if user_number == 0:
        raise Zero('Деление на нуль')
except Zero as z:
    print(z)
