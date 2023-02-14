# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

a = int(input('Введите число A\n'))
b = int(input('Введите число B\n'))

def deg(a, b) :
    if a == 0 and b == 0:
        print('решений нет')
    if a != 0 and b == 0:
        return 1
    else :
        return deg(a, b - 1) * a
print('A в степени B равно', deg(a, b))