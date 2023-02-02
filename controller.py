import model
import view


def handler(inp: int):
    match inp:
        case 1:
            view.show_all(model.db_dict)
        case 2:
            model.read_db('database.txt')
            view.db_success(model.db_dict)
        case 4:
            model.db_dict.append(view.new_contact())
        case 7:
            view.exit_program()


def start():
    while True:
        user_inp = view.show_menu()
        handler(user_inp)
