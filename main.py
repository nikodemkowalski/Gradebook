grades = {}
grade_list = []
subjects = grades.keys()


def separate(func):
    def wrapp():
        print('=======================')
        func()
        print('=======================')
    return wrapp


def add_subject():
    i = input('Wpisz nazwę przedmiotu: ').capitalize()
    if i in grades:
        print('Podany przedmiot już istnieje!')
    else:
        grades[i] = 'BO'
        print(F'Pomyślnie dodano nowy przedmiot! - {i}\n')


def collect_grade():
    while True:
        grade_input = int(input('Wpisz ocenę: '))
        if 1 <= grade_input <= 6:
            grade_list.append(grade_input)
        elif grade_input == 0:
            return grade_list
        else:
            print('Nie ma takiej oceny!')
            continue


def assign_grades():
    print('Lista przedmiotów:', subjects)
    i = input('Wybierz przedmiot: ')
    collect_grade()
    grades[i] = grade_list
    print(grade_list)


def continue_inquiry(func):
    print('Czy chcesz kontynuować?: Y/N')
    i = str(input().upper())
    if i == 'N':
        menu()

    elif i == 'Y':
        func()

    else:
        print('Wybierz z posród podanych!\n')
        continue_inquiry(func)


@separate
def menu():
    print('Dziennik elektroniczny\n'.upper())
    print('1. Dodaj przedmiot')
    print('2. Dodaj oceny')
    print('3. Oceny')
    print('0. Wyjdz')


@separate
def menu_grades():
    print('\nOceny\n'.upper())
    print('1. Średnia ocen')
    print('2. Oceny cząstkowe')


def check_grades():
    menu_grades()
    insert = int(input('Wybierz pozycje: '))
    if insert == 1:
        avarage_grades()

    elif insert == 2:
        check_subject()

    else:
        print('Niepoprawne dane!')


def check_subject():
    print(subjects)
    i = str(input('Wybierz przedmiot: '))
    if i in grades:
        print(grades[i])
    else:
        print('Nie znaleziono przedmiotu')


def calculate_avarage():
    print(subjects)
    i = input('Wybierz przedmiot: ')
    if i in grades:
        value = list(grades[i])
        print(sum(value) / len(value))

    else:
        print('Wpisz poprawną nazwe przedmitu')
        check_subject()


def main_loop():
    insert = -1
    menu()
    while insert != 0:
        if insert == 1:
            print('\nDodaj przedmiot\n'.upper())
            print(F'Lista przedmiotów:{subjects}')
            add_subject()
            continue_inquiry(add_subject)

        if insert == 2:
            print('\nDodaj oceny\n'.upper())
            calculate_avarage()
            continue_inquiry(assign_grades)

        if insert == 3:
            check_grades()
            continue_inquiry(check_grades)
        try:
            insert = int(input('Wybierz pozycje: '))
            if insert >= 4:
                print('Niewłaściwa wartość\n')

        except ValueError:
            print('Wprowadz liczbę\n')

    print('Do zobaczenia!')


main_loop()
