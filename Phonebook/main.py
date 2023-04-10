from function_file import *

choice = show_menu()
phone_book = read_csv("Phonebook/phonebook.csv")

while (choice != 8):
    if choice == 1:
        print_result(phone_book)

    elif choice == 2:
        find_lastname(phone_book)

    elif choice == 3:
        find_number(phone_book)

    elif choice == 4:
        add_user(phone_book)

    elif choice == 5:
        change_user(phone_book)

    elif choice == 6:
        delete_user(phone_book)

    elif choice == 7:
        save_changes(phone_book)

    choice = show_menu()