# Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
# двух целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1.Также нельзя использовать циклы.

a = int(input('Введите целое неотрицательное число a: \n'))
b = int(input('Введите целое неотрицательное число b: \n'))

def sum(a, b):
    if b == 0 :
        return a
    elif b > 0 :
        return sum(a + 1, b - 1)
    else : sum(a - 1, a + 1)

print('Сумма чисел a и b ', sum(a, b))