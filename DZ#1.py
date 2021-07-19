class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        res = ''
        for i in self.matr:
            res += f'{" ".join(map(str, i))}\n'
        return res

    def __add__(self, other):
        result = []
        if len(self.matr) != len(other.matr):
            raise ValueError('Nope')

        for i, y in zip(self.matr, other.matr):
            if len(i) != len(y):
                raise ValueError('Nope')
            result.append([a + j for a, j in zip(i, y)])
        return Matrix(result)


a = Matrix([[2, 4, 2], [5, 7, -3]])
print(a)
b = Matrix([[5, 9, 2], [7, 3, 6]])
c = a + b
print(c)
