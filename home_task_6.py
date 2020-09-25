import time
import colorama
import random

print("Задание №1")


class TrafficLight:
    __color = ["красный", "желтый", "зеленый"]

    def __init__(self, t):
        self.t = t

    def running(self):
        tm = [7, 3, 5]
        colors = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN]
        print(f"Светофор будет работать {self.t} секунд")
        while self.t > 0:
            for i in range(4):
                if i > 2:
                    i = i - 2 * (i - 2)
                print(colors[i] + self.__color[i])
                time.sleep(tm[i])
                self.t -= tm[i]


a = TrafficLight(random.randint(30, 60))
a.running()


print(colorama.Style.RESET_ALL)
print("\n")
print("Задание №2")
print("\n")


class Road:

    def __init__(self, _length, _width):
        self._length = abs(_length)
        self._width = abs(_width)

    def m(self, m1=25, d=5):
        m = self._width * self._length * abs(m1) * abs(d)
        print(
            f"Масса асфальта для покрытия дорожного полотна длиной {self._length} м, шириной {self._width} м и толщиной {abs(d)} см = {round(m / 1000)} т")


while True:
    n1 = int(input("Введите длину дорожного покрытия: "))
    n2 = int(input("Введите ширина дорожного покрытия: "))
    if n1 != 0 and n2 != 0:
        break
    elif ValueError:
        print("Error")
r = Road(n1, n2)
r.m(20, 7)


print("\n")
print("Задание №3")
print("\n")


class Worker:
    name = "Adam"
    surname = "Smith"
    position = "lead developer"
    _income = {"wage": random.randrange(60000, 90000, 5000), "bonus": random.randrange(60000, 80000, 5000)}

    def __init__(self):
        self.name = Worker.name
        self.surname = Worker.surname
        self.position = Worker.position
        self._income = Worker._income


class Position(Worker):
    def __init__(self):
        super().__init__()

    def get_full_name(self):
        print(self.name + " " + self.surname)

    def get_total_income(self):
        h = self._income.get("wage") + self._income.get("bonus")
        print(f"Полный доход = {h}")


b = Position()
b.get_full_name()
b.get_total_income()


print("\n")
print("Задание №4")
print("\n")


class Car:
    x = 0
    y = 0
    dir_x = False
    dir_y = True
    mode_x = 1
    mode_y = 1

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.x = Car.x
        self.y = Car.y
        self.dir_x = Car.dir_x
        self.dir_y = Car.dir_y
        self.mode_x = Car.mode_x
        self.mode_y = Car.mode_y

    def go(self):
        if self.speed == 0:
            self.speed += 1
        if self.speed > 200:
            self.speed = 200
        if self.dir_x:
            self.x = self.x + self.speed * self.mode_x
            self.speed *= 1.5
        elif self.dir_y:
            self.y = self.y + self.speed * self.mode_y
            self.speed *= 1.5

    def stop(self):
        if self.dir_x:
            self.speed /= 3
            self.x = self.x + self.speed * self.mode_x
            if self.speed < 0.01:
                self.speed = 0
        elif self.dir_y:
            self.speed /= 3
            self.y = self.y + self.speed * self.mode_y
            if self.speed < 0.01:
                self.speed = 0

    def turn(self, direction):
        if direction == "right" and self.dir_y:
            print("Поворот направо")
            self.dir_x = True
            self.dir_y = False
            if self.mode_y == 1:
                self.mode_x = 1
            if self.mode_y == -1:
                self.mode_x = -1
        elif direction == "left" and self.dir_y:
            print("Поворот налево")
            self.dir_x = True
            self.dir_y = False
            if self.mode_y == 1:
                self.mode_x = -1
            if self.mode_y == -1:
                self.mode_x = 1
        elif direction == "right" and self.dir_x:
            print("Поворот направо")
            self.dir_y = True
            self.dir_x = False
            if self.mode_x == 1:
                self.mode_y = -1
            if self.mode_x == -1:
                self.mode_y = 1
        elif direction == "left" and self.dir_x:
            print("Поворот налево")
            self.dir_y = True
            self.dir_x = False
            if self.mode_x == 1:
                self.mode_y = 1
            if self.mode_x == -1:
                self.mode_y = -1
        elif direction == "U-turn":
            print("Разворот")
            if self.dir_x:
                self.mode_x = - self.mode_x
            if self.dir_y:
                self.mode_y = - self.mode_y

    def show_speed(self):
        print(f"Ваша скорость = {self.speed}")

    def show_characteristics(self):
        print(f"Марка машины - {self.name}, цвет - {self.color}")


class TownCar(Car):
    def __init__(self):
        super().__init__(15, "blue", "Volvo", False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость превышена, {self.speed}")
        else:
            Car.show_speed(self)


class WorkCar(Car):
    def __init__(self):
        super().__init__(5, "green", "Lada", False)

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость превышена, {self.speed}")
        else:
            Car.show_speed(self)


class SportCar(Car):

    def __init__(self):
        super().__init__(40, "red", "Lamborgini", False)


class PoliceCar(Car):
    def __init__(self):
        super().__init__(20, "white", "Audi", True)

    def show_characteristics(self):
        print(f"Марка машины - {self.name}, цвет - {self.color}")
        print("Полицейская машина")


a = TownCar()
a.go()
print(a.x, a.y)
a.turn("left")
a.go()
a.show_speed()
print(a.x, a.y)
a.go()
a.go()
a.turn("right")
a.go()
a.show_speed()
a.stop()
print(a.x, a.y)
a.go()
a.turn("left")
a.go()
print(a.x, a.y)
a.stop()
a.stop()
a.stop()
print(a.x, a.y)
a.turn("U-turn")
a.go()
print(a.x, a.y)
a.go()
a.go()
a.show_speed()
a.show_characteristics()
b = WorkCar()
b.show_characteristics()
c = SportCar()
c.show_characteristics()
d = PoliceCar()
d.show_characteristics()

print("\n")
print("Задание №5")
print("\n")


class Stationery:
    title = ["ручка", "карандаш", "маркер"]

    def __init__(self):
        self.title = Stationery.title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self):
        super().__init__()
        self.title = self.title[0]

    def draw(self):
        print(f"В отрисовке нам поможет {self.title}")


class Pencil(Stationery):
    def __init__(self):
        super().__init__()
        self.title = self.title[1]

    def draw(self):
        print(f"Нет ничего лучше для рисования, чем {self.title}")


class Handle(Stationery):
    def __init__(self):
        super().__init__()
        self.title = self.title[2]

    def draw(self):
        print(f"А {self.title} пригодится, если что-то надо выделить")


q = Pen()
q.draw()
w = Pencil()
w.draw()
e = Handle()
e.draw()
