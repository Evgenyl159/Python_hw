import re


class Data:

    def __init__(self, data: str):
        self.data = data
        if re.compile(r'^(\d{2}[-]){2}\d{4}$').match(data):
            print(data)
        else:
            msg = f'не правильный формат данных {data}\nПример : 21-11-2011'
            raise ValueError(msg)

    @classmethod
    def check_date(cls, date_string):
        if re.compile(r'^(\d{2}[-]){2}\d{4}$').match(date_string):
            day, month, year = map(int, date_string.split('-'))
            print(f'День {day} Месяц {month} Год {year}')
            return day, month, year
        else:
            msg = f'не правильный формат данных {date_string}\nПример : 21-11-2011'
            raise ValueError(msg)

    @staticmethod
    def strong_valid(date_str):
        if re.compile(r'^(\d{2}[-]){2}\d{4}$').match(date_str):
            day, month, year = map(int, date_str.split('-'))
            status = day <= 31 and month <= 12 and year <= 3000
            print(date_str)
            print(f'Корректность данных: {status}')
            return status
        else:
            msg = f'не правильный формат данных {date_str}\nПример : 21-11-2011'
            raise ValueError(msg)


date = Data('21-11-2244')
d, m, y = Data.check_date('21-11-2244')
stat = Data.strong_valid('41-11-2244')
