""" 9. (5 розділ) Описати функцію Replace1(P, R, Q) - заміни підслова P на слово R в слові Q. Скласти
програму, яка робить в рядку пошук і заміну підслова P на слово R в слові Q до тих
пір, поки це можливо."""


def replace_1(q: str, p: str, r: str) -> str:
    if q.find(p) != 0:
        a = q.replace(p, r)
        return a
    else:
        return f"Подстроки {p} нету в слове {q}"


def main():
    print(" Добро пожаловать в программу перевоплощения слова!")
    choice = None
    while choice != "0":
        print(
            """
        0 - Выйти
        1 - Преобразить слово
        """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    q = input("Введите слово, состоящее из букв ")
                    if q.isalpha() and q != "":
                        break
                    else:
                        print("Слово должно состоять из букв!")
                except ValueError:
                    print("Несоответствие типов!")
            while True:
                try:
                    p = input("Введите подслово, состоящее из букв ")
                    if p.isalpha() and p != "":
                        break
                    else:
                        print("Слово должно состоять из букв!")
                except ValueError:
                    print("Несоответствие типов!")
            while True:
                try:
                    r = input("Введите новое подслово, состоящее из букв ")
                    if r.isalpha() and r != "":
                        break
                    else:
                        print("Слово должно состоять из букв!")
                except ValueError:
                    print("Несоответствие типов!")

            print(replace_1(q, p, r))


main()
