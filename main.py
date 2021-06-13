grades = {}
grade_list = []
key = grades.keys()


def decorator(func):
    def wrapp():
        print('=======================')
        func()
        print('=======================')
    return wrapp


def add_subject():
    print(F'Lista przedmiotów:{list(key)}')
    i = input('Wpisz nazwę przedmiotu: ')
    if i in grades:
        print('Podany przedmiot już istnieje!')

    else:
        grades[i] = 'BO'
        print(F'Pomyślnie dodano nowy przedmiot! - {i}\n')


def add_grade():
    while True:
        grade_input = int(input('Wpisz ocenę: '))
        if 1 <= grade_input <= 6:
            grade_list.append(grade_input)

        elif grade_input == 0:
            return grade_list

        else:
            print('Nie ma takiej oceny!')
            continue


def add_grades(add_grade):
    print('Lista przedmiotów:', list(key))
    i = input('Wybierz przedmiot: ')
    add_grade()
    grades[i] = grade_list


def check_subject():
    print(key)
    i = str(input('Wybierz przedmiot: '))
    if i in grades:
        print(grades[i])
    else:
        print('Nie znaleziono przedmiotu')


def avarage_grades(func):
    print(key)
    i = input('Wybierz przedmiot: ')
    if i in grades:
        value = list(grades[i])
        result = sum(value) / len(value)
        print(result)

    else:
        print('Wpisz poprawną nazwe przedmitu')
        func()


def pick(func):
    print('Czy chcesz kontynuować?: Y/N')
    i = str(input().upper())
    if i == 'N':
        menu()

    elif i == 'Y':
        func()

    else:
        print('Wybierz z posród podanych!\n')
        pick(func)


@decorator
def menu():
    print('Dziennik elektroniczny\n'.upper())
    print('1. Dodaj przedmiot')
    print('2. Dodaj oceny')
    print('3. Oceny')
    print('0. Wyjdz')


@decorator
def menu_grades():
    print('\nOceny\n'.upper())
    print('1. Średnia ocen')
    print('2. Oceny cząstkowe')


def subject():
    print('\nDodaj przedmiot\n'.upper())
    add_subject()
    pick(subject)


def grade():
    print('\nDodaj oceny\n'.upper())
    add_grades(add_grade)
    pick(grade)


def check():
    menu_grades()
    insert = int(input('Wybierz pozycje'))
    if insert == 1:
        avarage_grades(check_subject)

    elif insert == 2:
        check_subject()

    else:
        print('Niepoprawne dane!')
    pick(check_subject)


def main_loop():
    insert = -1
    menu()
    while insert != 0:
        if insert == 1:
            subject()

        if insert == 2:
            grade()

        if insert == 3:
            check()

        try:
            insert = int(input('Wybierz pozycje: '))
            if insert >= 4:
                print('Niewłaściwa wartość\n')

        except ValueError:
            print('Wprowadz liczbę\n')

    print('Do zobaczenia!')


main_loop()
