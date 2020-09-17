import itertools
from random import shuffle
from functools import reduce
import math

print("Задание № 2")
l = [300, 2, 12, 44, 1, 1, 4, 10, 7, 78, 123, 55]
shuffle(l)

print(l)
print([l[i] for i in range(len(l)) if l[i] > l[i - 1] and i > 0])


print()
print("Задание № 3")
print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])



print("Задание № 4")
n = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([i for i in n if n.count(i) == 1])


print()
print("Задание № 5")
n = [i for i in range(100, 1001) if i % 2 == 0]
print(f"Произведение = {reduce(lambda i1, i2: i1 * i2, n)}")

print()
print("Задание № 6")
m = abs(int(input("Введите число: ")))
mm = []
lim = 0
while lim <= m:
    lim = abs(int(input("Введите ограничитель ")))
for i in itertools.count(m):
    if i >= lim:
        break
    else:
        mm.append(i)
        print(i, end=' ')

lim = (lim - m) * 3
print(" ")

for i in itertools.cycle(mm):
    if lim < m:
        break
    print(i, end=' ')
    m += 1


print()
print("Задание № 7")
n = 0
while n < 1:
    n = int(input("Введите натуральное число: "))


def r():
    for i in range(1, reduce(lambda i1, i2: i1 * i2, range(1, n + 1)) + 1):
        yield i


if reduce(lambda i1, i2: i1 * i2, range(1, n + 1)) == math.factorial(n):
    r = r()
    print(r)
    for i in r:
        print(i, end=' ')
