
    # user_input = int(input('Введите команду: >>> '))
    # # TODO сделать проверку
    # return user_input


def show_all(db: list):
    if db_success(db):
        for j in range(len(db)):
            user_id = j + 1
            print(f'\t{user_id}', end=' ')
            for v in db[j].values():
                print(v, end=' ')
            print()


def db_success(db: list):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга закрыта')
        return False


def exit_program():
    print('Завершение программы')
    exit()


def new_contact():
    print('Создание нового контакта:')
    new_dict = {'lastname': input('Введите фамилию: '), 'firstname': input('Введите имя: '),
                'phone': input('Введите телефон: '), 'comment': input('Введите комментарий: ')}
    return new_dict
