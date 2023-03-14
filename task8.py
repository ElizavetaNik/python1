n = int(input("1-й размер "))
m= int(input("2-й размер"))
k = int(input("количество долек "))
if k%n == 0 or k%m == 0:
    print('можно')
else: 
    print('нельзя')

