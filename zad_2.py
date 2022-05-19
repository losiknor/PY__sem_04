# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# *пользователь вводит А, В, С
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

#Вариант 1
# import math

# print("Введите коэффициенты для уравнения")
# print("ax^2 + bx + c = 0:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))

# discr = b ** 2 - 4 * a * c
# print("Дискриминант D = %.2f" % discr)

# if discr > 0:
#     x1 = (-b + math.sqrt(discr)) / (2 * a)
#     x2 = (-b - math.sqrt(discr)) / (2 * a)
#     print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
#     x = -b / (2 * a)
#     print("x = %.2f" % x)
# else:
#     print("Корней нет")

# Вариант 2
from re import X


a = int(input('Введите число A '))
b = int(input('Введите число B '))
c = int(input('Введите число C '))

def diskr(a, b, c):
    d = b ** 2 - 4 * a * c
    return d

def sqrt_(a, b, c):
    d = diskr(a, b, c)
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        return False
print(sqrt_(a, b, c))