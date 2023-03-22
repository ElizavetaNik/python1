import random
my_list = [random.randint(0,20) for _ in range(20)]
print(my_list)
X = int(input('Введите число X: '))
count = 0
for i in range(20):
    if my_list[i] == X:
        count += 1
print(f'Число {X} встречается {count} раз') 
    