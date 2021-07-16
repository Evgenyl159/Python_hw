class Road:
    mass = 25
    fat = 5

    def __init__(self, length, width):
        self.length = length
        self.width = width
        if length < 0 or width < 0:
            msg = 'Некорректное значение'
            raise ValueError(msg)

    def road_cover(self):
        result = (self.length * self.width * Road.mass * Road.fat) / 1000
        if result < 0.99:
            print(f'{round(result * 1000, 2)} кг')
        else:
            print(f'{round(result, 2)} т')


obj = Road(100, 5000)
obj.road_cover()
