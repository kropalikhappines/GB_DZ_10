class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num > 0 and other.num > 0:
            return Cell(self.num - other.num)
        else:
            raise ValueError('Nope')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __floordiv__(self, other):
        return Cell(self.num / other.num)

    def  __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, n):
        nr = self.num // n
        res = self.num % n
        return '\n'.join(['*' * n] * nr + ['*' * res])



cell_1 = Cell(13)
cell_2 = Cell(7)
cell_3 = cell_1 - cell_2
print(cell_3.num)
cell_4 = cell_1 + cell_2
print(cell_4.num)
cell_5 = cell_1 * cell_2
print(cell_5.num)
cell_6 = cell_1 / cell_2
print(cell_6.num)
cell_7 = cell_1 // cell_2
print(cell_7.num)
print(cell_1.make_order(5))