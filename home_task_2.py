
print("Task No 1")
list_of_types = []
my_list = [48839, 929.2992, "synchronization", "Alas, poor Yorick. I knew him, Horatio...", False, None, [2343, "erosion", True], (3737, 983.039, "#$&%")]
for i in my_list:
    list_of_types.append(type(i))
j = 0
for i in list_of_types:
    print(f"{i} {my_list[j]}")
    j += 1
my_list.clear()


print("Task No 2")
my_list = list('')
j = int(input("Insert the number of elements in the list "))
n = 0
while True:
    my_list.append(input("Insert an element for the list "))
    n += 1
    if n == j:
        break
my_list.append(None)
ind = my_list.index(None)
my_list.pop(ind)
print(my_list)
if ind % 2 != 0:
    ind -= 2
else:
    ind -= 1
t: int = 0
while ind > t:
    m = my_list[t]
    my_list[t] = my_list[t + 1]
    my_list[t + 1] = m
    t += 2
print(my_list)


print("Task 3")
dict_seasons = {12: "winter", 1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer", 8: "summer", 9: "autumn", 10: "autumn", 11: "autumn"}
while True:
    month = int(input("Insert the number of a month "))
    if 0 < month <= 12:
        list_ = dict_seasons.keys()
        for i in list_:
            if i == month:
                print(f"It is {dict_seasons.get(i)}")
        break
    else:
        continue


print("Task 4")
str_1 = input("Insert a string ")
list_1 = str_1.split()
n = 1
for q in list_1:
    b = str(q)
    if len(b) <= 10:
        print(f"{n} {b}")
        n += 1
    else:
        print(f"{n} {b[0:10:]}")
        n += 1

print("Второй вариант")
str_1 = input("Insert a string ")
list_1 = str_1.split(" ")
for i in list_1:
    i_s = str(i)
    if len(i_s) > 10:
        ind = list_1.index(i)
        i = i_s[:10:]
        list_1.pop(ind)
        list_1.insert(ind, i)
for i in enumerate(list_1, 1):
    print(i)

print("Task 5")
rating = [7, 5, 3, 3, 2]
q = 0
while True:
    q += 1
    x = int(input("Insert a number "))
    rating.append(x)
    n0 = rating.count(x)
    for i in rating:
        if x > i:
            rating.insert(rating.index(i), x)
        ind_x = rating.index(x)
        n = rating.count(x)
        if n > n0:
            while n > 0:
                rating.remove(x)
                n -= 1
            while n < n0:
                rating.insert(ind_x, x)
                ind_x += 1
                n += 1
        if rating.index(x) == 0:
            break
    print(rating)
    if q == 5:
        break


print("Task 6")
list_titles = [""]
list_prices = [""]
list_quantity = [""]
list_measurement = [""]
dict_ = {}
tuple_1 = tuple()
tuple_2 = tuple()
tuple_3 = tuple()
tuple_4 = tuple()
dict_analytical = {}
index = 0
while True:
    index += 1
    title = input(f"Please, provide the title of the product No {index} ")
    price = float(input(f"Please, provide the price of the product No {index} "))
    quantity = int(input(f"Please, provide the quantity of the product No {index} "))
    measurement = input(f"Please, provide the measurement unit for the product No {index} ")

    list_titles.append(title)
    list_prices.append(price)
    list_quantity.append(quantity)
    list_measurement.append(measurement)

    m_1 = list_titles[index]
    m_2 = list_prices[index]
    m_3 = list_quantity[index]
    m_4 = list_measurement[index]

    dict_.update({"title": m_1, "price": m_2, "quantity": m_3, "measurement": m_4})
    list_ = [index, dict_]
    if index == 1:
        tuple_1 = tuple(list_)
    elif index == 2:
        tuple_2 = tuple(list_)
    elif index == 3:
        tuple_3 = tuple(list_)
    elif index == 4:
        tuple_4 = tuple(list_)

    goods = [tuple_1, tuple_2, tuple_3, tuple_4]

    if index == 4:
        break

list_titles.pop(0)
list_prices.pop(0)
list_quantity.pop(0)
list_measurement.pop(0)
list_titles = list(set(list_titles))
list_prices = list(set(list_prices))
list_quantity = list(set(list_quantity))
list_measurement = list(set(list_measurement))

dict_analytical.update(
    {"title": list_titles, "price": list_prices, "quantity": list_quantity, "measurement": list_measurement})
print(goods)
print(dict_analytical)