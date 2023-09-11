
#Задача 2
"""
num = int(input("Введите 3х-значное число: "))
sum = 0
for i in range(1,4):
    sum = sum + num%10
print(sum)
"""

#Задача 4
"""
numBird = int(input("Введите общее количество журавликов: "))
if numBird%4 != 0:
    print("А точно детишки делали журавликов?")
x = int(numBird/4)
print(f"Петя сделал {x} журавликов")
print(f"Вася сделал {x} журавликов")
print(f"Катя сделала {x*2} журавликов")
"""
"""
ticketNumber = int(input("Введите шестизначный номер билета: "))
sumOne = 0
sumTwo = 0 

for i in range (1,7):
    if i<4: 
        sumOne = sumOne + ticketNumber%10
        ticketNumber = int(ticketNumber/10)
    else:
        sumTwo = sumTwo + ticketNumber%10
        ticketNumber = int(ticketNumber/10)

if sumOne == sumTwo:
    print("yes")
else: 
    print ("no")
"""

#Задача 8
"""
n = int(input("Введите размер шоколадки n "))
m = int(input("Введите размер шоколадки m "))
k = int(input("Введите количество долек k "))

if k < m*n and (k%m==0 or k%n==0):
    print("Можно")
else:
    print("Нельзя")
    """