from sys import argv

script_name, work_time, rate, bonus = argv

print("Имя скрипта ", script_name)
print("Выработка в часах", work_time)
print("Ставка в час", rate)
print("Премия", bonus)
wages = int(work_time) * int(rate) + int(bonus)
print("Зарплата = ", wages)
