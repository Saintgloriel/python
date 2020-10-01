from abc import ABC, abstractmethod
import random

print("Задание №1")
a = [[random.randint(0, 9), random.randint(-7, 9)], [random.randint(-3, 15), random.randint(-1, 9)], [random.randint(0, 19), random.randint(-8, 6)]]
b = [[random.randint(-7, 9), 1], [random.randint(0, 12), random.randint(0, 9)], [22, random.randint(-1, 9)]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return "\n".join("\t".join([str(j) for j in i]) for i in self.lists)

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return "\n".join("\t".join([str(j) for j in i]) for i in c)


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(matrix_1)
print("\n")
print(matrix_2)
print("\n")
print(matrix_1 + matrix_2)
print("\n")


print("Задание №2")


class Clothes(ABC):
    def __init__(self, p):
        self.p = p

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.p / 6.5) + 0.5


class Suit(Clothes):
    @property
    def consumption(self):
        return (self.p * 2 + 0.3) / 100


coat = Coat(46)
suit = Suit(178)
print(coat.consumption)
print(suit.consumption)
print(coat + suit)
print("\n")

print("Задание №3")


class Cell:
    def __init__(self, n):
        self.n = n

    def make_order(self, l):
        return '\n'.join(["*" * l for _ in range(self.n // l)]) + '\n' + "*" * (self.n % l)

    def __str__(self):
        return self.n

    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        return self.n - other.n if self.n > other.n else print("Error")

    def __mul__(self, other):
        return self.n * other.n

    def __truediv__(self, other):
        return round(self.n / other.n)

    def __floordiv__(self, other):
        return self.n // other.n


cell_1 = Cell(15)
cell_2 = Cell(24)
cell_3 = Cell(88)
cell_4 = Cell(4)
print(cell_4 + cell_1)
print(cell_3 * cell_2)
print(cell_3 - cell_1)
print(cell_2 // cell_1)
print(cell_3 / cell_2)
print(cell_1.make_order(4))
print(cell_3.make_order(9))