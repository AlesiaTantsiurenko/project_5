"""9. (2 розділ) Описати функцію Even (K) логічного типу, яка повертає True, якщо цілий параметр K
є парним, і False в іншому випадку. З її допомогою знайти кількість парних чисел в
наборі з 10 цілих чисел"""


def even(k: int) -> bool:
    if k % 2 == 0:
        return True
    else:
        return False


def main():
    print(" Добро пожаловать в программу нахожденя парных чисел!")
    choice = None
    while choice != "0":
        print(
            """
        0 - Выйти
        1 - Найти количество парных чисел
        """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            kol = 0
            for i in range(10):
                while True:
                    try:
                        k = int(input(f"Введите целое число k{i + 1}= "))
                        break
                    except ValueError:
                        print("Несоответствие типов!")
                if even(i):
                    kol += 1
            print(f"Количество парных чисел равно {kol}")
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
