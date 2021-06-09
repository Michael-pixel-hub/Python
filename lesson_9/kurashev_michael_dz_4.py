class Car:
    speed = 61
    color = 'red'
    name = 'BMW'
    is_police = True
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self, direction):
        print(f'Машина повернула {direction}')
    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    if Car.speed > 60:
        def show_speed(self):
            print("Вы превысили скорость")


class SportCar(Car):
    pass


class WorkCar(Car):
    if Car.speed > 40:
        def show_speed(self):
            print("Вы превысили скорость")


class PoliceCar(Car):
    pass


car = Car()
town_car = TownCar()
sport_car = SportCar()
work_car = WorkCar()
police_car = PoliceCar()

print(car.speed)
print(car.color)
print(car.name)
print(car.is_police)
car.go()
car.stop()
car.turn('направо')
car.show_speed()
town_car.show_speed()
work_car.show_speed()
