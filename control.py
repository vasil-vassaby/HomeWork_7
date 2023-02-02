import model
import output
import input
import colorama
from colorama import Fore, Style

colorama.init()

name, phone, comment, user_input = '', '', '', ''


def handler(inp: int):
    global name, phone, comment, user_input
    match inp:
        case 1:
            model.set_file()
            model.open_file()
            output.print_info(Fore.GREEN + 'Телефонная книга открыта')
            print(Style.RESET_ALL)
        case 2:
            if model.phonebook_open():
                contacts = model.get_all_contact()
                output.print_contact(contacts)
            else:
                output.print_info(Fore.RED + 'Телефонная книга закрыта')
                print(Style.RESET_ALL)
        case 3:
            if model.phonebook_open():
                contact_id = input.input_contact_id()
                output.print_contact(model.get_contact(contact_id))
            else:
                output.print_info(Fore.RED + 'Телефонная книга закрыта')
                print(Style.RESET_ALL)
        case 4:
            if model.phonebook_open():
                output.print_new_contact()
                name = input.input_name()
                phone = input.input_phone()
                comment = input.input_comment()
                contact = model.new_contact(model.get_all_contact(), name, phone, comment)
                output.print_contact(contact)
                user_answer = input.save_contact()
                if user_answer == 'да':
                    model.set_file()
                    model.save_file()
                    output.print_info(Fore.GREEN + 'Контакт успешно создан!')
                    print(Style.RESET_ALL)
                elif user_answer != 'да' or user_answer != 'нет':
                    output.print_error(Fore.RED + 'Напишите "да" или "нет"!')
                    print(Style.RESET_ALL)
                else:
                    output.print_error(Fore.RED + 'Контакт не сохранен!')
                    print(Style.RESET_ALL)
            else:
                output.print_info(Fore.RED + 'Телефонная книга закрыта')
                print(Style.RESET_ALL)
        case 5:
            if model.phonebook_open():
                output.print_change_contact()
                name = input.input_name()
                phone = input.input_phone()
                comment = input.input_comment()
                user_input = input.user_input('Введите фамилию и имя для замены: ').strip().title()
                try:
                    contact = model.change_contact(model.get_all_contact(), name, phone, comment, user_input)
                    if contact:
                        output.print_contact(contact)
                        user_answer = input.change_contact()
                        if user_answer == 'да':
                            model.set_file()
                            model.save_file()
                            output.print_info(Fore.GREEN + 'Контакт успешно изменен!')
                            print(Style.RESET_ALL)
                        elif user_answer != 'да' or user_answer != 'нет':
                            output.print_error(Fore.RED + 'Напишите "да" или "нет"!')
                            print(Style.RESET_ALL)
                        else:
                            output.print_error(Fore.RED + 'Контакт не изменен!')
                            print(Style.RESET_ALL)
                    else:
                        output.print_error(Fore.RED + 'Контакт из справочника для замены не найден!')
                        print(Style.RESET_ALL)
                except TypeError:
                    output.print_error(Fore.RED + 'Проверьте правильность ввода данных!')
                    print(Style.RESET_ALL)
            else:
                output.print_info(Fore.RED + 'Телефонная книга закрыта')
                print(Style.RESET_ALL)
        case 6:
            if model.phonebook_open():
                output.print_remove_contact()
                name = input.input_name()
                phone = input.input_phone()
                comment = input.input_comment()
                try:
                    contact = model.remove_contact(model.get_all_contact(), name, phone, comment)
                    if contact:
                        output.print_contact(contact)
                        user_answer = input.remove_contact()
                        if user_answer == 'да':
                            model.set_file()
                            model.save_file()
                            output.print_info(Fore.GREEN + 'Контакт успешно удален!')
                            print(Style.RESET_ALL)
                        elif user_answer != 'да' or user_answer != 'нет':
                            output.print_error(Fore.RED + 'Напишите "да" или "нет"!')
                            print(Style.RESET_ALL)
                        else:
                            output.print_error(Fore.RED + 'Контакт не удален!')
                            print(Style.RESET_ALL)
                    else:
                        output.print_error(Fore.RED + 'Контакт не найден!')
                        print(Style.RESET_ALL)
                except TypeError:
                    output.print_error(Fore.RED + 'Проверьте правильность ввода данных!')
                    print(Style.RESET_ALL)
            else:
                output.print_info(Fore.RED + 'Телефонная книга закрыта')
                print(Style.RESET_ALL)
        case 7:
            output.print_exit()
            exit()


def start():
    while True:
        output.print_menu()
        try:
            user_inp = input.input_command()
            if 0 < user_inp < 8:
                handler(user_inp)
            else:
                output.print_error(Fore.RED + 'Укажите номер меню (от 1 до 7)')
                print(Style.RESET_ALL)
        except ValueError:
            output.print_error(Fore.RED + 'Укажите номер меню (от 1 до 7)')
            print(Style.RESET_ALL)
