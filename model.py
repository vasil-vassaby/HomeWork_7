import re

phonebook = []
path = ''


def set_file():  # определяем путь к файлу справочника
    global path
    path = 'Phone_Book/database.txt'


def open_file():
    global phonebook
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        phonebook = file.readlines()

    return True


def get_all_contact():
    global phonebook
    return phonebook


def get_contact(contact_id: int):
    global phonebook
    if 0 < contact_id < len(phonebook) + 1:
        return [phonebook[contact_id - 1]]
    return []


def phonebook_open():
    global phonebook

    if phonebook:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга закрыта')
        return False


def new_contact(contacts: list):
    print('------- НОВЫЙ КОНТАКТ ---------')
    name = input('Введите фамилию и имя: ').title()
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    new_con = name + ';' + phone + ';' + comment
    if new_con not in contacts:
        contacts.append(new_con)
    return contacts


def save_file():
    global path
    global phonebook
    new_file = []
    if len(phonebook) > 1:
        for contact in phonebook:
            new_file.append(contact.strip())
    elif len(phonebook) == 1:
        new_file.append(str(phonebook).strip())
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(new_file))


def remove_contact(contacts: list):
    print('------- УДАЛЕНИЕ КОНТАКТА ---------')
    name = input('Введите фамилию и имя: ').strip().title()
    phone = input('Введите телефон: ').strip()
    comment = input('Введите комментарий: ').strip()
    remove_con = name + ';' + phone + ';' + comment + '\n'
    if remove_con in contacts:
        con = remove_con.strip().split(';')
        print(f'Контакт для удаления - это: {" ".join(con)}')
        contacts.remove(remove_con)
    return contacts


def change_contact(contacts: list):
    print('------- ИЗМЕНЕНИЕ КОНТАКТА ---------')
    name = input('Введите фамилию и имя из справочника: ').strip().title()
    phone = input('Введите телефон из справочника: ').strip()
    comment = input('Введите комментарий из справочника: ').strip()
    change_con = name + ';' + phone + ';' + comment + '\n'
    if change_con in contacts:
        con = change_con.strip().split(';')
        print(f'Контакт для изменения - это: {" ".join(con)}')
        name, phone, comment = con[0], con[1], con[2]
        user_input = input('Введите фамилию и имя для замены: ').strip().title()
        name = user_input
        con = name + ';' + con[1] + ';' + con[2]
        contacts.remove(change_con)
        contacts.append(con)
    return contacts
