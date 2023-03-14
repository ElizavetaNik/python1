n = int(input("Введите число: "))
tiket2 = n%1000
tiket1 = n//1000
summa1 = 0
while tiket2>0:
    x = tiket2%10
    summa1=x+summa1
    tiket2=tiket2//10
summa2=0
while tiket1>0:
    x = tiket1%10
    summa2=x+summa2
    tiket1=tiket1//10

happy = summa1 == summa2
print(f'ЭТО СЧАТЛИВЫЙ БИЛЕТ - {happy}')

