class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': wage, 'bonus': bonus}
        print(f'{position}')


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f"{sum(self.income.values())}"


Taxist = Position('Рамзан', 'Пармезан', 'Таксист', 15000, 500000)
print(Taxist.get_full_name())
print(Taxist.get_total_income())