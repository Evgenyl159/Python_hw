import time


class TrafficLight:
    __color = {'red': 7, 'yellow': 2, 'green': 5}

    def running(self):
        for light in self.__color:
            print(light)
            time.sleep(self.__color[light])


obj = TrafficLight()
obj.running()