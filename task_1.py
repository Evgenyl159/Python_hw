import random


class Matrix:

    def __init__(self, count_X, count_Y):
        self.count_X = count_X
        self.count_Y = count_Y
        self.full_list = []
        for i in range(self.count_Y):
            generate_list = [random.randint(10, 49) for v in range(self.count_X)]
            self.full_list.append(generate_list)

    def __str__(self):
        return '\n'.join(map(str, self.full_list)).replace('[', '').replace(']', '').replace(',', '')

    def __add__(self, other):
        sum_matrix = []
        for i in range(len(self.full_list)):
            sum_matrix.append([])
            for j in range(len(self.full_list[0])):
                sum_matrix[i].append(self.full_list[i][j] + other.full_list[i][j])
        return '\n'.join(map(str, sum_matrix)).replace('[', '').replace(']', '').replace(',', '')


a = Matrix(5, 5)
b = Matrix(5, 5)
print(a, '\n')
print(b, '\n')
print(a + b)