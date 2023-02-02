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
        return True
    else:
        return False


def new_contact(contacts: list, name, phone, comment: str):
    new_con = name + ';' + phone + ';' + comment
    if new_con not in contacts:
        contacts.append(new_con)
    else:
        return False
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


def remove_contact(contacts: list, name, phone, comment: str):
    remove_con = name + ';' + phone + ';' + comment + '\n'
    if remove_con in contacts:
        con = remove_con.strip().split(';')
        contacts.remove(remove_con)
    else:
        return False
    return contacts


def change_contact(contacts: list, name, phone, comment, user_input: str):
    change_con = name + ';' + phone + ';' + comment + '\n'
    if change_con in contacts:
        con = change_con.strip().split(';')
        name, phone, comment = con[0], con[1], con[2]
        name = user_input
        con = name + ';' + con[1] + ';' + con[2]
        contacts.remove(change_con)
        contacts.append(con)
    else:
        return False
    return contacts
