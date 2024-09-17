class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print( f"Создана машина {self.name}\nЦвет {self.name} : {self.color}\nСкорость : {self.speed}\nполиция? - {is_police}\n")

    def go(self):
        print(f" {self.name} : Машина поехала")

    def stop(self):
        print(f"{self.name} : Машина остановилась")

    def turn(self, direction):
        if direction == 0:
            print(f"{self.name} машина повернула направо")
        elif direction == 1:
            print(f"{self.name} машина повернула налево")
        else:
            print(f"{self.name} машина едет прямо")

    def show_speed(self):
        print(f"Скорость {self.name} : {self.speed}")


class TownCar(Car):
    @property
    def show_speed(self):
        if self.speed > 60:
            return f"{self.name} : Превышение скорости на {self.speed - 60}.\nСкорость {self.name} : {self.speed}\n" \
                   f"Допустимая скорость : 60 "
        else:
            return f"Скорость {self.name} : {self.speed}"


class SportCar(Car):
    # ракета
    pass


class WorkCar(Car):
    @property
    def show_speed(self):
        if self.speed > 40:
            return f"{self.name} : Превышение скорости на {self.speed - 40}.\nСкорость {self.name} : {self.speed}\n" \
                   f"Допустимая скорость : 40 "
        else:
            return f"Скорость {self.name} : {self.speed}"


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


bmw = SportCar(290, 'black', 'BMW', False)
bmw.show_speed()

ford_police = PoliceCar(190, 'half white, half blue', 'Ford', True)

town = TownCar(110, 'white', 'Kia', False)
print(town.show_speed)