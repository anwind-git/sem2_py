from fractions import Fraction
"""
Напишите программу банкомат.
- Начальная сумма равна нулю
- Допустимые действия: пополнить, снять, выйти
- Сумма пополнения и снятия кратны 50 у.е.
- Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
- После каждой третей операции пополнения или снятия начисляются проценты - 3%
- Нельзя снять больше, чем на счёте
- При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией
- Любое действие выводит сумму денег

Выполнять без применения функций!
"""
"""
summa = 0
number_operations = 0
percent = 0.015
interest_wealth = 0.100
max_fee = 600
min_fee = 30
while True:
    num = input("Выберете действие (пополнить - 1, снять - 2, выход - 3): ")
    if num == '1':
        try:
            replenishment_amount = int(input("Внесите сумму: "))
            if replenishment_amount % 50 == 0:
                summa += replenishment_amount
                number_operations += 1
                if number_operations == 3:
                    summa *= 0.97
                    number_operations = 0
                    print("Сняты 3% за 3-и проведенных операции")
                if summa > 5000000:
                    summa -= summa * 0.1
                    print("вычит налога на богатство 10 %")
                print(f"Баланс пополнен, на вашем счете {summa} y.e")
            else:
                print(f"Ошибка пополнения: сумма должна быть кратна 50 у.е. "
                      f"Баланс не пополнен. На вашем счете: {summa} y.e.")
        except ValueError:
            print(f"Ошибка: вы ввели не число! На вашем счете: {summa} y.e")
    elif num == '2':
        try:
            withdrawal_amount = int(input("Сумма снятия: "))
            fee = max(min(withdrawal_amount * percent, max_fee), min_fee)
            if withdrawal_amount % 50 == 0 and fee < summa:
                summa -= fee
                number_operations += 1
                if number_operations == 3:
                    summa *= 0.97
                    number_operations = 0
                    print("Сняты 3% за 3-и проведенных операции")
                if summa > 5000000:
                    summa -= summa * 0.1
                    print("вычит налога на богатство 10 %")
                print(f"Снятие наличных выполнено. Баланс счета: {summa} y.e.")
            else:
                print(f"Ошибка снятя: Баланс счета: {summa} y.e.")
        except ValueError:
            print(f"Ошибка: вы ввели не число! На вашем счете: {summa} y.e")
    elif num == '3':
        print(f"Баланс счета: {summa} y.e.")
        break
"""
"""
Напишите программу, которая получает целое 
число и возвращает его шестнадцатеричное 
строковое представление. Функцию hex 
используйте для проверки своего результата.
"""
"""
num = int(input("Введите целое число: "))
hex_num = hex(num)
print("Шестнадцатеричное представление числа:", hex_num)
"""
"""
Напишите программу, которая принимает две строки 
вида “a/b” — дробь с числителем и знаменателем. 
Программа должна возвращать сумму 
и *произведение дробей. Для проверки своего 
кода используйте модуль fractions.
"""
frac1 = input("Введите первую дробь в формате a/b: ")
frac2 = input("Введите вторую дробь в формате a/b: ")

num1, den1 = frac1.split('/')
num2, den2 = frac2.split('/')

f1 = Fraction(int(num1), int(den1))
f2 = Fraction(int(num2), int(den2))

sum_frac = f1 + f2
mult_frac = f1 * f2

print("Сумма дробей:", sum_frac)
print("Произведение дробей:", mult_frac)
