import json
from datetime import datetime
import config as cn

def read_notes() -> dict:
    try:
        with open(cn.FILE_PATH, 'r', encoding='utf-8') as data:
            note_json = data.read()
        notes = json.loads(note_json, parse_int=int)
        return notes
    except FileNotFoundError:
        return

def save_notes(notes: dict):
    note_json = json.dumps(notes, ensure_ascii=False)
    with open(cn.FILE_PATH, 'w', encoding='utf-8') as data:
        data.write(note_json)

def add_note(notes: dict, new_note: dict) -> str:
    note_id = len(notes)
    while str(note_id) in notes.keys():
        note_id += 1
    notes[note_id] = new_note
    save_notes(notes)
    return 'Заметка успешно сохранена'

def create_note(new_note: dict) -> str:
    note_id = 1
    notes = {}
    notes[note_id] = new_note
    save_notes(notes)
    return 'Заметка успешно сохранена'

def find_by_id(notes: dict, id: str) -> dict:
    id = str(id)
    if id in notes:
        return {id: notes[id]}

def delete_note(notes: dict, id: str) -> str:
    notes.pop(id)
    save_notes(notes)
    return "Заметка удалена"

def change_note(notes: dict, id: str, new_title: str, new_body: str) -> str:
    # Внести изменения
    if new_title:
        notes[id]['note_title'] = new_title
    if new_body:
        notes[id]['note_body'] = new_body
    # Изменить время
    notes[id]['note_date'] = datetime.now().strftime("%d/%m/%Y")
    notes[id]['note_time'] = datetime.now().strftime("%H:%M:%S")
    save_notes(notes)
    return "Заметка сохранена"