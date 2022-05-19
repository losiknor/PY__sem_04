# Задайте два числа. Напишите программу, которая найдёт НОК этих двух чисел.

# Вариант 1
# a = int(input('a= '))
# b = int(input('b= '))
# c = max(a, b)

# while ((c % b !=0) and (c % a !=0)) or ((c % b ==0) and (c % a !=0)) or ((c % b !=0) and (c % a ==0)):
#     c +=1
# print(c)

# Вариант 2
a = int(input('a= '))
b = int(input('b= '))
c = max(a, b)
k = 1
while True:
    if ((c * k) % a == 0 and (c * k) % b == 0):
        print(c * k)
        break
    k += 1
