def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить данные абонента\n"
          "6. Удалить абонента из справочника\n"
          "7. Сохранить справочник в текстовом формате\n"
          "8. Закончить работу")
    choice = int(input())
    return choice


def read_csv(filename: str):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def print_result(data):
    for i in data:
        for k, v in i.items():
            print(f"{k} : {v}")
        print()
    input("Для возврата в главное меню нажмите клавишу Enter")


def find_lastname(data):
    lastname = input("Введите фамилию: ")
    count = 0
    list_of_results = []
    for i in data:
        if lastname in i["Фамилия"]:
            count += 1
            list_of_results.append(i)
    if count == 0:
        print("Пользователь не найден")
    if count > 0:
        for i in list_of_results:
            for k, v in i.items():
                print(f"{k:10} : {v}")
            print()
    input("Для продолжения нажмите клавишу Enter")


def find_number(data):
    number = input("Введите номер телефона: ")
    count = 0
    list_of_results = []
    for i in data:
        if number in i["Телефон"]:
            count += 1
            list_of_results.append(i)
    if count == 0:
        print("Пользователь не найден")
    if count > 0:
        for i in list_of_results:
            for k, v in i.items():
                print(f"{k:10} : {v}")
            print()
    input("Для продолжения нажмите клавишу Enter")


def add_user(data):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    list_1 = []
    list_1.append(input("Введите фамилию: "))
    list_1.append(input("Введите имя: "))
    list_1.append(input("Введите номер: "))
    list_1.append(input("Введите описание: "))
    new_user = dict(zip(fields, list_1))
    data.append(new_user)
    print("Вы добавили нового пользователя")
    for k, v in new_user.items():
        print(f"{k} : {v}")
    print()
    input("Для возврата в главное меню нажмите клавишу Enter")


def change_user(data):
    name = input("Введите имя или фамилию пользователя: ")
    count = 0
    list_of_results = []
    for i in data:
        if name in i["Фамилия"] or name in i["Имя"]:
            count += 1
            list_of_results.append(i)
            if count == 1:
                change = i
            if count > 1:
                print("Найдено несколько пользователей, подходящих под условия. Выберите номер нужного.")
                for i in data:
                    if i in list_of_results:
                        print(f"№{data.index(i) + 1}")
                        for k, v in i.items():
                            print(f"{k:10} : {v}")
                        print()
                change = data[int(input()) - 1]
    if count == 0:
        print("Пользователь не найден")
    if count > 0:
        print("\nВыберите что вы хотите изменить:\n"
          "1. Фамилию\n"
          "2. Имя\n"
          "3. Номер телефона\n"
          "4. Описание")
        choice = int(input())
        if choice == 1:
            change["Фамилия"] = input("Введите новую фамилию: ")
        elif choice == 2:
            change["Имя"] = input("Введите новое имя: ")
        elif choice == 3:
            change["Телефон"] = input("Введите новый номер телефона: ")
        elif choice == 4:
            change["Описание"] = input("Введите новое описание: ")
        print(f'Пользователь {change["Фамилия"]} {change["Имя"]} изменен')
    input("Для возврата в главное меню нажмите клавишу Enter")


def delete_user(data):
    name = input("Введите имя или фамилию пользователя: ")
    count = 0
    list_of_results = []
    for i in data:
        if name in i["Фамилия"] or name in i["Имя"]:
            count += 1
            list_of_results.append(i)
            if count == 1:
                delete = i
            if count > 1:
                print("Найдено несколько пользователей, подходящих под условия. Выберите номер нужного.")
                for i in data:
                    if i in list_of_results:
                        print(f"№{data.index(i) + 1}")
                        for k, v in i.items():
                            print(f"{k:10} : {v}")
                        print()
                delete = data[int(input()) - 1]
    if count == 0:
        print("Пользователь не найден")
    if count > 0:
        print(f'Пользователь {delete["Фамилия"]} {delete["Имя"]} удален')
        data.remove(delete)
    input("Для возврата в главное меню нажмите клавишу Enter")

def save_changes(data):
    with open("Phonebook/phonebook.csv", 'w', encoding='utf-8') as new_file:
        for i in data:
            str_i = ""
            for v in i.values():
                str_i += v + ","
            str_i = str_i[:-1]
            new_file.write(str_i + "\n")
        print("Данные сохранены!")
    input("Для возврата в главное меню нажмите клавишу Enter")
