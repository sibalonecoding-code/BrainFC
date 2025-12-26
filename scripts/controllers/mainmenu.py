

# load modules
from __future__ import annotations
from scripts.models.deckmanager import DeckManager
from scripts.views.mainmenu import MainMenuView


# main menu controller
class MainMenuController:

    @classmethod
    def run(cls, deckmanager:DeckManager, params:dict) -> dict:
        # display main menu screen
        MainMenuView.display_welcome()
        # main menu
        choice = MainMenuView.get_main_menu_choice()
        if choice == "Apprendre": params["scene"] = "learn"
        elif choice == "Éditeur": params["scene"] = "editor"
        elif choice == "Statistiques": params["scene"] = "stats"
        elif choice == "Paramètres": params["scene"] = "settings"
        elif choice == "Quitter": params["scene"] = ""
        # return result
        return params
