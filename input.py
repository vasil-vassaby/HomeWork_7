import output


def input_contact_id():
    while True:
        try:
            contact_id = int(input('Введите ID контакта: '))
            return contact_id
        except ValueError:
            output.print_error('Введите целое число!')


def input_command():
    user = int(input('Введите команду: '))
    return user


def save_contact():
    return input('Сохранить контакт в телефонный справочник? да/нет >>>')


def remove_contact():
    return input('Удалить контакт из телефонного справочника? да/нет >>>')


def change_contact():
    return input('Изменить контакт из телефонного справочника? да/нет >>>')
