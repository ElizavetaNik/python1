x = int(input('Введите первое натуральное число X '))
y = int(input('Введите второе натуральное число Y '))
S = x + y
P = x * y
y1 = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
x1 = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
print(x1, y1)