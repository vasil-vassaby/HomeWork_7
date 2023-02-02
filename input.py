import colorama
from colorama import Fore, Style

import output

colorama.init()


def input_contact_id():
    while True:
        try:
            contact_id = int(input('Введите ID контакта: '))
            return contact_id
        except ValueError:
            output.print_error(Fore.RED + 'Введите целое число!')
            print(Style.RESET_ALL)


def input_command():
    user = int(input('Введите команду: '))
    return user


def input_name():
    name = input('Введите фамилию и имя: ').strip().title()
    if not name.isdigit():
        return name


def input_phone():
    phone = input('Введите телефон: ').strip()
    if phone.isdigit():
        return phone


def input_comment():
    comment = input('Введите комментарий: ').strip()
    return comment


def save_contact():
    return input('Сохранить контакт в телефонный справочник? да/нет >>> ')


def remove_contact():
    return input('Удалить контакт из телефонного справочника? да/нет >>> ')


def change_contact():
    return input('Изменить контакт в телефонном справочнике? да/нет >>> ')


def user_input(message: str):
    user_inp = input(message)
    if not user_inp.isdigit():
        return user_inp
