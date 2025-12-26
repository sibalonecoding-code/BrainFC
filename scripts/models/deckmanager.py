

# load modules
from __future__ import annotations
import os
from rich.traceback import install
from scripts.models.deck import Deck


install()


class DeckManager:
    
    def __init__(self, **kwargs):
        self.data_folder = kwargs.get("data_folder", "data/")
        self.decks: dict[str, Deck] = kwargs.get("decks", dict())

    def data_folder_exists(self) -> bool:
        return os.path.exists(self.data_folder)

    def deck_exists(self, name:str) -> bool:
        return name in self.scan_decks()

    def scan_decks(self) -> list[str]:
        if not self.data_folder_exists():
            os.makedirs(self.data_folder)
        return [item for item in os.listdir(self.data_folder) if item.endswith(".json")]

    def get_deck(self, name:str) -> Deck:
        if not self.deck_exists(name):
            return None
        deck = Deck(name, storage_path=f"{self.data_folder}{name}.json")
        deck.load()
        return deck
