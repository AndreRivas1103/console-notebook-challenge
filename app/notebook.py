from ctypes.wintypes import tagSIZE
from datetime import datetime


class Note:
    HIGH: str = 'HIGH'
    MEDIUM: str = 'MEDIUM'
    LOW: str = 'LOW'

    def __init__(self, code, title, text, importance, creation_date: datetime, tags: []):
        self.code: str = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date: datetime = creation_date
        self.tags: list[str] = []

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"



class Notebook:
    def __init__(self, notes):
       self.notes: list[Note] = []

    def add_note(self, title, text, importance, creation_date: datetime, tags: []) -> int:
        code = len(self.notes) + 1
        note = Note(str(code), title, text, importance, creation_date,tags)
        self.notes.append(note)
        return code

    def delete_note(self, code:int):
        self.notes = [note for note in self.notes if note.code != str(code)]

    def important_notes(self) -> list[Note]:
        return [note for note in self.notes if note.importance in (Note.HIGH, Note.MEDIUM)]


    def notes_by_tag(self, tag: str) -> list[Note]:
        return [note for note in self.notes if tag in note.tags]

    def tag_with_most_notes(self) -> str:
        pass
