import random
import json

print("Задание №1")
f_1 = open("file_1.txt", 'a')
while True:
    data = input('Введите данные, для завершения используйте пустую строку: ')
    if data == "":
        break
    f_1.write(data + '\n')

f_1.close()

print("Задание №2")
count_1 = 0
count_2 = 0
with open("file_2.txt", "r") as f_2:
    try:
        for line in f_2:
            count_1 += 1
            for i in line.split(" "):
                if i != " ":
                    count_2 += 1
            print(f"Количество слов в строке №{count_1}: {count_2}")
            count_2 = 0
    except IOError:
        print("Error")
print(f"Количество строк в файле: {count_1}")

print("Задание №3")
income_avg = 0
families = list()
income = list()
with open("file_3.txt", "r") as f_3:
    li = f_3.read()
    for i in li.split("\n"):
        for j in i.split(" "):
            if j[0:1].isdigit():
                income.append(float(j))
            else:
                families.append(j)
print("Сотрудники с доходом менее 20000:")
for i in range(len(income)):
    if income[i] < 20000:
        print(f"{families[i]}")
income_avg = sum(income) / len(income)
print(f"Средний доход = {income_avg:.2f}")


print("Задание №4")
with open("file_4.txt", "r") as f_4:
    for line in f_4:
        for i in line.split():
            if i == "One":
                i1 = "Один"
            elif i == "Two":
                i1 = "Два"
            elif i == "Three":
                i1 = "Три"
            elif i == "Four":
                i1 = "Четыре"
            elif i == "-":
                i2 = i
            else:
                i3 = i
        line = " ".join([i1, i2, i3])
        with open("file_5.txt", "a") as f_5:
            f_5.write(f'{line}\n')
#os.remove("file_5.txt")


print("Задание №5")
l = list()
n = 0
p = 1
while n < 20:
    x = random.randrange(1, 100)
    l.append(str(x))
    n += 1
s = " ".join(l)
with open("file_6.txt", "w+") as f_6:
    f_6.write(s)
    f_6.seek(0)
    t = f_6.read()
    for i in t.split(" "):
        i = int(i)
        p *= i
print(f"Произведение чисел в файле {f_6.name} = {p}")

print("Задание №6")
q = list()
s = 0
c = list()
sigma = 0
con = dict()
with open("file_7.txt", "r") as f_7:
    for line in f_7:
        for i in line.split(" "):
            if i.isalpha:
                if i.find(":") != -1:
                    name = i[:i.find(":")]
            for j in i:
                if j.isdigit():
                    q.append(int(j))
            for v in range(len(q)):
                s += int(q[v] * 10 ** (len(q) - v - 1))
            c.append(s)
            q.clear()
            s = 0
        sigma = sum(c)
        con.update({name: sigma})
        c.clear()
print(con)

print("Задание №7")
stat = list()
d = dict()
gen = list()
gen_sum = 0
n = 0
with open("file_8.txt", "r") as f_8:
    content = f_8.read()
    for line in content.split("\n"):
        for i in line.split(" "):
            if not i.isupper():
                if i.isdigit():
                    stat.append(i)
                elif i.isalpha:
                    title = i
        s = float(stat[0]) - float(stat[1])
        if s >= 0:
            gen_sum += s
            n += 1
        stat.clear()
        d.update({title: s})
avg_profit = gen_sum / n
gen = [d, {"average_profit": avg_profit}]
print(gen)

with open("results.json", "w") as results:
    json.dump(gen, results)