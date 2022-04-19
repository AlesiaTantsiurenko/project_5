""" 9. (1 розділ) Описати функцію AddLeftDigit (D, K), що додає до цілого позитивного числа K
ліворуч цифру D (D - вхідний параметр цілого типу, що лежить в діапазоні 1-9, K -
параметр цілого типу, який є одночасно вхідним і вихідним). За допомогою цієї
функції послідовно додати до цього числа K ліворуч дані цифри D1 і D2, виводячи
результат кожного додавання."""


def add_left_digit(d: int, k: int) -> int:
    n = len(str(k))
    k = d * 10 ** n + k
    return k


def main():
    print(" Добро пожаловать в программу перевоплощения числа!")
    choice = None
    while choice != "0":
        print(
            """
        0 - Выйти
        1 - Преобразить число
        """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    k = int(input("Введите целое число: "))
                    if k > 0:
                        break
                    else:
                        print("Параметр k должен быть больше нуля!")
                except ValueError:
                    print("Несоответствие типов!")
            for i in range(2):
                while True:
                    try:
                        d = int(input(f"Введите целое число  d{i + 1} в диапазоне [1;9]: "))
                        if 0 < d < 10:
                            break
                        else:
                            print("Число должно находиться в диапазоне [1;9]!")
                    except ValueError:
                        print("Несоответствие типов!")
                print("K: ", add_left_digit(d, k))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
