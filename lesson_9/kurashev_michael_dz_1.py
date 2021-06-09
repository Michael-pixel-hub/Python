from time import sleep

class TrafficLight:
    __color = 'red'

    def running(self):
        self.__color = 'red'
        print(self.__color)
        self.__color = 'yellow'
        sleep(7)
        print(self.__color)
        self.__color = 'green'
        sleep(2)
        print(self.__color)


traffic_light = TrafficLight()
traffic_light.running()

