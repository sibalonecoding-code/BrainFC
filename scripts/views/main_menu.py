

# load modules
import os
import time
import inquirer
from rich.console import Console
from rich.progress import track
from rich.panel import Panel


console = Console()


class MainMenu:

    @staticmethod
    def display_welcome():
        width, height = os.get_terminal_size()
        console.line()
        console.print("🮦   🮧   🮪   🮫   🮬   🮭   🮮   🮽   🮮   🮬   🮭   🮪   🮫   🮧   🮦".center(width), style="dark_orange")
        color = "yellow"
        extra_width = len(f"[{color}][/]") * 3
        console.print(f"[{color}]B r a i n[/]   [{color}]F[/] l a s h [{color}]C[/] a r d".center(width+extra_width), style="dark_orange")
        console.print("🮧   🮦   🮫   🮪   🮭   🮬   🮮   🮽   🮮   🮭   🮬   🮫   🮪   🮦   🮧".center(width), style="dark_orange")
        console.line()
        for _ in track(range(1000), description="Chargement...", transient=True, update_period=0.01, refresh_per_second=100):
            time.sleep(0.002)

    @staticmethod
    def get_main_menu_choice() -> str:
        questions = [
            inquirer.List("menu",
                          message="Menu Principal (Entrée 🮴 pour confirmer)",
                          choices=["Apprendre", "Éditeur", "Statistiques", "Options", "Quitter"])
        ]
        answers = inquirer.prompt(questions=questions)
        return answers["menu"]

    # @staticmethod
    # def select_deck(deckmanager: list[str]) -> str:
    #     decks:list[str] = deckmanager.scan_decks()
    #     decks.append("🮵 Retour")
    #     questions = [
    #         inquirer.List("menu",
    #                       message="Sélection du Deck (Entrée 🮴 pour confirmer)",
    #                       choices=decks)
    #     ]
    #     answers = inquirer.prompt(questions=questions)
    #     return answers["menu"]

