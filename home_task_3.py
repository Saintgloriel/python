
print('Задание № 1')
_sum: float = 0


def div_(a, b):
    try:
        global _sum
        _sum = a / b
        print(f"Частное {a} и {b} = {_sum}")
    except ValueError and ZeroDivisionError:
        print("Error")
        return


a = float(input("Введите число "))
b = float(input("Введите другое число "))
div_(a, b)

print('Задание № 2')


def info_1(s, n, y, c, t, e):
    for i in [s, n, y, c, t, e]:
        print(f"{i} ", end='')
    print()


info_1(s=input("Фамилия: "), n=input("Имя: "), y=input("Год рождения: "), c=input("Город проживания: "),
       t=input("Телефон: "), e=input("e-mail: "))

print('Задание № 2. Второй вариант')


def info_2(**kwargs):
    kwargs = {"Фамилия": input("Фамилия: "), "Имя": input("Имя: "), "Год рождения": input("Год рождения: "),
              "Город проживания": input("Город проживания: "), "Телефон": input("Телефон: "),
              "e-mail": input("e-mail: ")}
    print(kwargs)


info_2()

print('Задание № 3')


def my_func(p, q, j):
    d = [p, q, j]
    s = max(d) + (sum(d) - max(d) - min(d))
    return s


p = int(input("Введите число: "))
q = int(input("Введите еще одно число: "))
j = int(input("Введите последнее число: "))
print(f"Сумма двух наибольших чисел = {my_func(p, q, j)}")

print('Задание № 4')


def _func():
    while True:
        x = float(input("Введите положительное действительное число: "))
        y = int(input("Введите целое отрицательное число: "))
        if x > 0 and y < 0:
            r = x ** y
            print(r)
            break
        else:
            continue


_func()

print('Задание № 4. Второй вариант')


def _func():
    while True:
        x = float(input("Введите положительное действительное число: "))
        y = int(input("Введите целое отрицательное число: "))
        if x > 0 and y < 0:
            r = x
            while y != -1:
                r = r * x
                y += 1
            print(1 / r)
            break
        else:
            continue


_func()



print('Задание № 5')


def func_t():
    global s
    s = 0
    flag = False
    while True:
        str_1 = input("Введите строку чисел, разделитель - пробел: ")
        l_1 = str_1.split(' ')
        l_2 = list()
        l_3 = list()
        for i in l_1:
            if i.isdigit():
                i0 = abs(int(i))
                l_2.append(i0)
            else:
                i = list(i)
                for j in i:
                    if j == "$":
                        flag = True
                        break
                    elif j.isdigit():
                        l_3.append(j)
                if bool(l_3) is True:
                    i0 = abs(int((''.join(l_3))))
                    l_3 = []
                    l_2.append(i0)
        print(l_2)
        s += sum(l_2)
        if flag:
            print(f'Сумма введенных чисел = {s}')
            break
        else:
            print(f'Сумма введенных чисел = {s}. Для завершения введите "$"')


func_t()

print('Задание № 6')
int_func = lambda str_l: str_l.title()
str_l = input("Введите строку из строчных латинских букв: ")
print(int_func(str_l))
