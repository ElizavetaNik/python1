n = int(input("Введите число: "))
summa = 0
while n>0:
    x = n%10
    summa=x+summa
    n=n//10
print(summa)