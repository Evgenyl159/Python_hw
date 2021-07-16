class Stationery:

    def __init__(self, title='канцелярская принадлежность'):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Привет , это ручка..")


class Pencil(Stationery):
    def draw(self):
        print("Привет , это карандаш..")


class Handle(Stationery):
    def draw(self):
        print("Привет , а это маркер..")


start = Stationery()
start.draw()

pen = Pen()
nahdle = Handle()

pen.draw()
nahdle.draw()
