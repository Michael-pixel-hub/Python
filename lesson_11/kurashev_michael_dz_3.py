class Numbers(Exception):
    def __init__(self, text):
        self.text = text


list_one = []

while True:
    user_number = input('Введите число для списка (введите "stop" для завершения): ')
    try:
        if user_number == 'stop':
            break
        elif not user_number.isdigit():
            raise Numbers('Вы ввели не число')
        elif user_number.isdigit():
            list_one.append(int(user_number))
    except Numbers as n:
        print(n)
print(list_one)