list_namber = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}
def num_translate(namber):
    if namber[0].isupper() and namber[1:].islower():
        a = list_namber.get(namber.lower())
        print(a.capitalize())
    elif namber.islower() and namber in list_namber:
        print(list_namber.get(namber))
    else:
        print("Неправильно ввели значение")

num_translate("Ten")
