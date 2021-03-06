""" 9. (3 розділ) Описати функцію Fib (N) цілого типу, яка обчислює N-й елемент послідовності
чисел Фібоначчі FK, яка описується наступними формулами:
F1 = 1, F2 = 1, FK = FK-2 + FK-1, K = 3, 4, ....
Використовуючи функцію Fib, знайти п'ять чисел Фібоначчі з даними номерами
N1, N2, ..., N5."""


def fib(n: int) -> int:
    fib1 = fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


def main():
    print(" Добро пожаловать в программу нахожденя значения числа Фибоначчи!")
    choice = None
    while choice != "0":
        print(
            """
        0 - Выйти
        1 - Найти число Фибоначчи по порядковому номеру
        """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            for i in range(5):
                while True:
                    try:
                        n = int(input("Введите порядковый номер элемента последовательности Фибоначчи (больше нуля): "))
                        if n > 0:
                            break
                        else:
                            print("Порядковый номер не может быть меньше нуля!")
                    except ValueError:
                        print("Несоответствие типов!")
                print(f"Элемент под номером {n} равен {fib(n)}.")
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
