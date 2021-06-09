class Stationery:
    title = "Ножницы"
    def drow(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def drow(self):
        print('Запуск отрисовки ручка')

class Pancil(Stationery):
    def drow(self):
        print('Запуск отрисовки карандаш')

class Handle(Stationery):
    def drow(self):
        print('Запуск отрисовки маркер')

stationery = Stationery()
pen = Pen()
pancil = Pancil()
handle = Handle()
stationery.drow()
pen.drow()
pancil.drow()
handle.drow()
