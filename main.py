

# load modules
import os
from scripts.models.deckmanager import DeckManager
from scripts.controllers.mainmenu import MainMenuController


# clear console functino
def clear():
    if os.name == "nt": os.system("cls")
    else: os.system("clear")


# main function
def main():
    # initialize
    params:dict = {"scene": "mainmenu"}
    dm = DeckManager(data_folder=f"data{os.sep}")
    # main loop
    while params["scene"]:
        clear()
        if params["scene"] == "mainmenu": params:dict = MainMenuController.run(dm, params)
        elif params["scene"] == "learn": pass
        elif params["scene"] == "editor": pass
        elif params["scene"] == "stats": pass
        elif params["scene"] == "settings": pass


# program's starting point
if __name__ == "__main__":
    main()
