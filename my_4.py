""" 9. (4 розділ) Описати функцію Power4 (x, a, ε) дійсного типу (параметри x, a, ε - дійсні, | x | <1; a,
ε> 0), знаходить наближене значення функції (1 + x) a
:
(1 + x) a
= 1 + a · x + a · (a-1) · x2
/ (2!) + ... + a · (a-1) · ... · (a-n + 1) · xn
/ (n!) + ....
В сумі враховувати всі складові, модуль яких більше ε. За допомогою Power4
знайти наближене значення (1 + x) a
для даних x і a при шести даних ε."""


def power4(x: float, a: float, e: float) -> float:
    y = a * x
    f = 1 + y
    i = 2
    while abs(y) > e:
        y *= (a - i + 1) * x / i
        i += 1
        if abs(y) > e:
            f += y
    return f


def main():
    print(" Добро пожаловать в программу нахождения приближенного значения выраженя (1 + x)^a!")
    choice = None
    while choice != "0":
        print(
            """
        0 - Выйти
        1 - Найти приближенное значение функции
        """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    x = float(input("Введите вещественное число, модуль которого меньше 1, x = "))
                    if abs(x) < 1:
                        break
                    else:
                        print("Модуль числа должени быть меньше 1!")
                except ValueError:
                    print("Несоответствие типов!")
            while True:
                try:
                    a = float(input("Введите вещественное число (степень), больше нуля a = "))
                    if a > 1:
                        break
                    else:
                        print("Число должно быть больше нуля!")
                except ValueError:
                    print("Несоответствие типов!")
            for i in range(6):
                while True:
                    try:
                        e = float(input(f"Введите число больше нуля e{i + 1} = "))
                        if e > 0:
                            break
                        else:
                            print("Число должно быть больше нуля!")
                    except ValueError:
                        print("Несоответствие типов!")
                print(f"Значение выражения (1+x)^a, учитывя только слогаемые, которые больше e={e} : {power4(x, a, e)}")
                print(f"Исходное значение: {(1 + x) ** a}.")
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()