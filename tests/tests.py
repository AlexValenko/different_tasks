
# a = int(input())
# b = int(input())
# c = int(input())
# print((a ** c + b ** c) ** (a * b))
'''
time_mins = int(input()) # – количество минут, которое пользователь провел на сайте
start_hours = int(input()) # – время в часах, когда пользователь зашел на сайт
start_mins = int(input()) # – время в минутах, когда пользователь зашел на сайт

out_time_hour = ((start_hours * 60 + start_mins + time_mins) // 60) % 24
out_time_min = (start_mins + time_mins) % 60

print(out_time_hour, out_time_min)
'''
# a = 33 #– количество минут
# b = 54 #– количество секунд
# n = 5 #– количество дней
#
# full_seconds = ((a * 60) + b) * n
# print(full_seconds)
# print(full_seconds//3600, (full_seconds//60) % 60, full_seconds % 60)
"""
a = int(input()) # Стоимость квартиры
y = int(input()) # Процентная ставка
x = int(input()) # Первоначальный взнос
b = int(input()) # Ежегодный платеж

credit = a - x
for i in range(3):
    rem = int((credit - b) * (1 + y / 100))
    credit = rem
    print(rem)
"""
# a, b, c = (float(input()) for i in range(3))
# print((a ** 3 + b ** (1/2)) / c)


#Дано дробное число x. Выведите вторую цифру после точки.
# x = float(input())
# print(int(abs(x) * 100) % 10)

"""
# Жесткая задача с округлением копеек
salary_1, salary_2 = (float(input()) for i in range(2))
income = int((salary_1 * 100) + (salary_2 * 100))

vacation = int(income * 0.1) 
print(f'Отпуск: {vacation // 100} руб. {vacation % 100} коп.')

food = int(income * 0.3)
print(f'Пропитание и еда: {food // 100} руб. {food % 100} коп.')

pays = int(income * 0.05)
print(f'Коммунальные платежи: {pays // 100} руб. {pays % 100} коп.')

hobby = int(income * 0.15)
print(f'Досуг: {hobby // 100} руб. {hobby % 100} коп.')

savings = income - vacation - food - pays - hobby
print(f'Накопления: {savings // 100} руб. {savings % 100} коп.')
"""
print(23039.40 + 6719.78)