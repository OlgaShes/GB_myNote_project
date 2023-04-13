from datetime import datetime

def get_new_note() -> dict:
    new_note = {}
    new_note = {
    'note_title': input('Введите заголовок заметки: '),
    'note_body': input('Введите текст заметки: '),
    'note_date': datetime.now().strftime("%d/%m/%Y"),
    'note_time': datetime.now().strftime("%H:%M:%S")
    }
    return new_note

def get_date() -> str:
   year = input('Введите год: ')
   month = input('Введите месяц: ')
   day = input('Введите день: ')
   return f'{day}/{month}/{year}'

def get_command() -> str:
    print(('\nВведите команду или help для вывода справки:'))
    command = input().strip()
    while command not in ('1', '2', '3', '4', '5', '6', 'help'):
        print('Некорректный ввод')
        command = input().strip()
    return command

def get_changing_operation() -> str:
    operation = input('Хотите изменить эту заметку? '
                  '(1 - изменить, 2 - удалить, 3 - искать другую заметку, '
                  +'exit для отмены изменений)\n').strip()
    while operation not in ('1', '2', '3', 'exit'):
        print('Некорректный ввод. \nВведите:\n'
              '1 для изменения,\n'
              '2 для удаления,\n'
              '3 для поиска другой заметки,\n'
              'exit для отмены изменений')
        operation = input().strip()
    return operation

def get_new_title() -> str:
    change = input('Введите новый заголовок заметки или нажмите ENTER для сохранения старого: ')
    return change

def get_new_body() -> str:
    change = input('Введите новый текст заметки или нажмите ENTER для сохранения старого: ')
    return change

def get_answer(text: str) -> str:
    return input(text)