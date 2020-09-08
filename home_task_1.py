
print("Task No 1")

i1 = 42
str1 = "Everything goes just as planned"
print(i1)
print(str1)
str2 = input("Insert your message ")
i2 = int(input("Insert any number "))
print(f"Your message: {str2}")
print(f"The inserted number is {i2}")

print("Task No 2")
time = abs(int(input("Insert the current time in seconds: ")))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time - hours * 3600 - minutes * 60
if hours > 23:
    hours = hours % 24
if hours < 10:
    if minutes < 10:
        if seconds < 10:
            print(f"0{hours}:0{minutes}:0{seconds}")
        else:
            print(f"0{hours}:0{minutes}:{seconds}")
    else:
        if seconds < 10:
            print(f"0{hours}:{minutes}:0{seconds}")
        else:
            print(f"0{hours}:{minutes}:{seconds}")
else:
    if minutes < 10:
        if seconds < 10:
            print(f"{hours}:0{minutes}:0{seconds}")
        else:
            print(f"{hours}:0{minutes}:{seconds}")
    else:
        if seconds < 10:
            print(f"{hours}:{minutes}:0{seconds}")
        else:
            print(f"{hours}:{minutes}:{seconds}")


print("Task No 3")

n = int(input("Insert the number: "))
num2 = int(f"{n}{n}")
num3 = int(f"{n}{n}{n}")
sum_n = n + num2 + num3
print(sum_n)

print("Task No 4")

n1 = int(input("Insert the number "))
if n1 > 10:
    q1 = n1 // 10
    n2 = 2
    while q1 >= 10:
        q1 = q1 // 10
        n2 = n2 + 1
    q = n1 - q1 * (10 ** (n2 - 1))
    n2 = n2 - 1
    q2 = 0
    while n2 > 0 and q2 < 10:
        q2 = q // (10 ** (n2 - 1))
        q = q - q2 * (10 ** (n2 - 1))
        n2 = n2 - 1
        if q2 > q1:
            q1 = q2
    print(q1)
else:
    print(n1)

print("Task No 5")

rev = float((input("The revenue of the company = ")))
exp = float((input("The expenses of the company = ")))
profit = rev - exp
if profit > 0:
    print("The company is profitable")
    profitability = (profit / rev) * 100
    print(f"Profitability = {profitability:.2f}%")
    pers_number = int(input("The number of its personnel = "))
    profit_per_capita = profit / pers_number
    print(f"Profit per capita = {profit_per_capita:.2f}")
elif profit < 0:
    print("The company is not profitable")

print("Task No 6")

a = int(input("The result of the first day = "))
b = int(input("The limit for the final result = "))
t = a
n_d = 1
if b > a:
    while t < b:
        t = t + t * 0.1
        n_d += 1
    print(f"The number of days = {n_d}")
else:
    print("Task is incorrect")
