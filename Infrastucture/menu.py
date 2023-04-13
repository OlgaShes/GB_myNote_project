import Infrastucture.operations as op
import Infrastucture.getting as g
import Infrastucture.view as v

INSTRUCTIONS = 'Для работы с приложением используйте команды:\n'\
                         '1 - чтение всех заметок\n'\
                         '2 - создание новой заметки\n'\
                         '3 - поиск заметок по дате\n'\
                         '4 - поиск заметки по ID\n'\
                         '5 - редактирование или удаление заметки\n'\
                         '6 - для выхода из программы'

SEPARATOR = '========================'

def get_help():
    v.show_text(SEPARATOR)
    v.show_text(INSTRUCTIONS)
    
def main_menu():
    command = ''
    while command != '6':
        v.show_text(SEPARATOR)
        notes = op.read_notes()
        if not notes:
            v.show_text("Ошибка, файл c заметками не найден или пуст. " + 
                        "Для создания новой заметки нажмите 1, " + 
                        "для прекращения работы любую другую клавишу.")
            if input() == '1':
                v.show_text(SEPARATOR)
                new_note = g.get_new_note()
                v.show_text(op.create_note(new_note))
            else:
               command = '6' 
        else:
            command = g.get_command()
            match command:
                case '1':
                    v.show_text(SEPARATOR)
                    v.print_all_notes(notes)
                case '2':
                    v.show_text(SEPARATOR)
                    new_note = g.get_new_note()
                    v.show_text(op.add_note(notes, new_note))
                case '3':
                    v.show_text(SEPARATOR)
                    date = g.get_date()
                    v.print_by_date(notes, date) 
                case '4':
                    v.show_text(SEPARATOR)
                    actions_with_note_by_id(notes, op.find_by_id(notes, g.get_answer("Введите ID заметки: ")))
                case '5':
                    v.show_text(SEPARATOR)
                    v.show_text('Для редактирования заметки введите ее ID, '+
                    'если не знаете ID, введите exit и воспользуйтесь '+ 
                    'поиском по дате или просмотром всех заметок')
                    answ = g.get_answer('')
                    if answ != 'exit':
                        actions_with_note_by_id(notes, op.find_by_id(notes, answ))
                case 'help':
                    v.show_text(SEPARATOR)
                    v.show_text(INSTRUCTIONS)
                case '6':
                    v.show_text('Спасибо за использование нашего приложения! До свидания!')

def actions_with_note_by_id(notes:dict, note: dict):
    v.print_note(note)
    if note:
        id, note_body = note.popitem()
        operation = g.get_changing_operation()
        match operation:
            case '1':
                # изменить заметку
                v.show_text(op.change_note(notes, id, g.get_new_title(), g.get_new_body()))
            case '2':
                # удалить заметку
                v.show_text(op.delete_note(notes, id))
            case '3':
                # найти новую заметку
                actions_with_note_by_id(notes, op.find_by_id(g.get_answer("Введите ID заметки: ")))
            case 'exit':
                # выход из редактирования
                return
            
