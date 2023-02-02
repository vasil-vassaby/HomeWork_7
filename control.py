import model
import output
import input
import colorama
from colorama import Fore, Style

colorama.init()


def handler(inp: int):
    match inp:
        case 1:
            model.set_file()
            model.open_file()
            model.phonebook_open()
        case 2:
            if model.phonebook_open():
                contacts = model.get_all_contact()
                output.print_contact(contacts)
        case 3:
            if model.phonebook_open():
                contact_id = input.input_contact_id()
                output.print_contact(model.get_contact(contact_id))
        case 4:
            if model.phonebook_open():
                contact = model.new_contact(model.get_all_contact())
                output.print_contact(contact)
                user_answer = input.save_contact()
                if user_answer == 'да':
                    model.set_file()
                    model.save_file()
                    print('Контакт успешно создан!')
                else:
                    output.print_error('Контакт не сохранен!')
        case 5:
            if model.phonebook_open():
                contact = model.change_contact(model.get_all_contact())
                output.print_contact(contact)
                user_answer = input.change_contact()
                if user_answer == 'да':
                    model.set_file()
                    model.save_file()
                    print('Контакт успешно изменен!')
                else:
                    output.print_error('Контакт не изменен!')
        case 6:
            if model.phonebook_open():
                contact = model.remove_contact(model.get_all_contact())
                output.print_contact(contact)
                user_answer = input.remove_contact()
                if user_answer == 'да':
                    model.set_file()
                    model.save_file()
                    print('Контакт успешно удален!')
                else:
                    output.print_error('Контакт не удален!')
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
            print(Fore.RED + 'Укажите номер меню (от 1 до 7)')
            print(Style.RESET_ALL)
