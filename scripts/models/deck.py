

# load modules
from __future__ import annotations
import json
import os
from rich.traceback import install
from scripts.models.flashcard import FlashCard


# enhance tracebacks output in console
install()



class Deck:

    def __init__(self, name:str, **kwargs):
        self.name = name
        self.flashcards:list[FlashCard] = kwargs.get("flashcards", list())
        self.storage_path = kwargs.get("storage_path", "")
        if self.storage_path:
            self.load()

    def ready(self):
        for flashcard in self.flashcards:
            if flashcard.ready():
                return True
        return False
    
    def load(self):
        # Handle not existing file
        if not os.path.exists(self.storage_path):
            raise FileExistsError("This file doesn't exist")
        # Make sure there a no flashcards
        self.flashcards.clear()
        # Create flashcards
        with open(self.storage_path, "r") as file:
            flashcards_data = json.load(file)
            for flashcard_data in flashcards_data:
                self.flashcards.append(FlashCard.from_dict(flashcard_data))

    def save(self):
        flashcards:list[dict] = list()
        for flashcard in self.flashcards:
            flashcards.append(flashcard.to_dict())
        with open(self.storage_path, "w", encoding="utf-8") as file:
            json.dump(flashcards, file, ensure_ascii=False)

    def add_flashcard(self, flashcard:FlashCard):
        self.flashcards.append(flashcard)

    def remove_flashcard(self, flashcard_index:int):
        self.flashcards.pop(flashcard_index)

    def get_flashcards_to_review(self) -> list[FlashCard]:
        return [flashcard for flashcard in self.flashcards if flashcard.ready()]
