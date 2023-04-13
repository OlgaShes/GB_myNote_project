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
        command = g.get_command()
        match command:
            case '1':
                v.show_text(SEPARATOR)
                v.print_all_notes(op.read_notes())
            case '2':
                v.show_text(SEPARATOR)
                new_note = g.get_new_note()
                v.show_text(op.add_note(new_note))
            case '3':
                v.show_text(SEPARATOR)
                date = g.get_date()
                v.print_by_date(op.read_notes(), date) 
            case '4':
                v.show_text(SEPARATOR)
                actions_with_note_by_id(op.find_by_id(g.get_answer("Введите ID заметки: ")))
            case '5':
                v.show_text(SEPARATOR)
                v.show_text('Для редактирования заметки введите ее ID, '+
                  'если не знаете ID, введите exit и воспользуйтесь '+ 
                  'поиском по дате или просмотром всех заметок')
                answ = g.get_answer('')
                if answ != 'exit':
                    actions_with_note_by_id(op.find_by_id(answ))
            case 'help':
                v.show_text(SEPARATOR)
                v.show_text(INSTRUCTIONS)
            case '6':
                v.show_text('Спасибо за использование нашего приложения! До свидания!')

def actions_with_note_by_id(note: dict):
    v.print_note(note)
    if note:
        id, note_body = note.popitem()
        operation = g.get_changing_operation()
        match operation:
            case '1':
                # изменить заметку
                v.show_text(op.change_note(id, g.get_new_title(), g.get_new_body()))
            case '2':
                # удалить заметку
                v.show_text(op.delete_note(id))
            case '3':
                # найти новую заметку
                actions_with_note_by_id(op.find_by_id(g.get_answer("Введите ID заметки: ")))
            case 'exit':
                # выход из редактирования
                return
            