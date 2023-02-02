import colorama
from colorama import Fore, Style

colorama.init()

menu = [
    'Открыть файл',
    'Показать все контакты',
    'Найти контакт',
    'Создать контакт',
    'Изменить контакт',
    'Удалить контакт',
    'Выход'
]


def print_menu():
    global menu
    print('____ ТЕЛЕФОННЫЙ СПРАВОЧНИК ____')
    print('======== ГЛАВНОЕ МЕНЮ ========')
    for i in range(len(menu)):
        print(f'\t{i + 1}. {menu[i]}')


def print_contact(contacts: list):
    if len(contacts) > 1:
        print('----------- СПИСОК ВСЕХ КОНТАКТОВ -----------')
        for contact in contacts:
            contact = contact.strip().split(';')
            print(f'{contact[0]:20} {contact[1]:15} {contact[2]:8}')
    elif len(contacts) == 1:
        print('----------- ДАННЫЕ КОНТАКТА -----------')
        contacts = contacts[0].strip().split(';')
        print(f'{contacts[0]:20} {contacts[1]:15} {contacts[2]:8}')
    else:
        print('----------- ЗАПРОС КОНТАКТА -----------')
        print('Контакт не найден!')


def print_error(message: str):
    print(message)


def print_info(message: str):
    print(message)


def print_new_contact():
    print('------- НОВЫЙ КОНТАКТ ---------')


def print_exit():
    print(Fore.RED + 'Телефонный справочник закрыт')
    print(Style.RESET_ALL)
