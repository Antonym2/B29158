f_num = int(input('Введите число 1: '))
s_num = int(input('Введите число 2: '))
while True:
    print(f"(число 1) {f_num}")
    print(f"(число 2) {s_num}")
    num1 = 0
    num2 = 0
    result = 0
    v = int(input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n 5 Замена чисел \n 6 Выход \n'))

    if v == 1:
        result = f_num + s_num
        print('Результат сложения = ', result)
    if v == 2:
        result = f_num - s_num
        print('Результат вычитания = ', result)
    if v == 3:
        if s_num != 0:
            result = float(f_num / s_num)
            print('Результат деления = ', result)
        else:
            print("на ноль делить нельзя")
            num2 = int(input("давайте заменим число (2) "))
            s_num = num2
    if v == 4:
        result = f_num * s_num
        print('Результат умножения = ', result)
    if v == 5:
        num1 = int(input("введите новое число (1) "))
        num2 = int(input("введите новое число (2) "))
        f_num = num1
        s_num = num2
    if v == 6:
        print("надеюсь вам понравился мой калькулятор")
        break

