def print_note(my_note: dict):
    if my_note:
        note = my_note.copy()
        id, note_body = note.popitem()
        print('\n#' + id)
        for value in note_body.values():
            print(value)
        print()          
    else:
        print('\nЗаметка с таким ID не найдена')
    
def print_all_notes(notes: dict):
    for id in notes.keys():
        print_note({id: notes[id]})

def print_by_date(notes: dict, date: str):
    not_found = True
    for id in notes.keys():
        if notes[id]['note_date'] == date:
            print_note({id: notes[id]})
            not_found = False
    if not_found: 
        print("Нет заметок с такой датой")

def show_text(text):
    print(text)

