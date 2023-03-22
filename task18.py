import random
my_list = [random.randint(0,20) for _ in range(20)]
print(my_list)
X = int(input('Введите число X: '))
min = X - my_list[0]
index = 0
for i in range(20):
    count = X - my_list[i]
    if count < min:
         min = count
         index = i    
print(f"Число {my_list[index]}  наиболее  к числу {X}")