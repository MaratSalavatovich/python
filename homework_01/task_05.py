"""
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)

"""

n = int(input("Введите трехзначное положительное число n- "))
a = n // 100
b = n % 100 // 10
c = n % 10
print(f'Сумма чисел равна: {a + b + c} ({a} + {b} + {c})')
