"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
number = int(input("Введите число n- "))
number_sum = (number + int(str(number) + str(number)) + int(
    str(number) + str(number) + str(number)))
print(f"Сумма чисел n + nn + nnn -  {number_sum}")
