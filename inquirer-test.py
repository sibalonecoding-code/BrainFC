

# load modules
import inquirer
from inquirer.themes import BlueComposure
# from inquirer.themes import GreenPassion
# from inquirer.themes import RedSolace
from rich import print


def ask_questions(questions):
    
    answers = inquirer.prompt(questions, theme=BlueComposure())
    return answers


if __name__ == "__main__":
    
    while True:

        questions = [
            inquirer.Text("name", message="Quel est ton nom?", validate=lambda _, x: len(x) > 0),
            inquirer.Text("age", message="Quel âge as-tu?", validate=lambda _, x: x.isdigit()),
            inquirer.List(
                "gender",
                message="Quel est ton genre?",
                choices=["Homme", "Femme", "Non binaire"],
                carousel=True
            ),
            inquirer.Checkbox(
                "languages",
                message="Quels langages maîtrise-tu?",
                choices=["HTML", "CSS", "Java", "Javascript", "Kotlin", "Ruby", "Python", "C", "C++", "C#"]
            ),
            inquirer.Checkbox(
                "frameworks-css",
                message="Quels frameworks de cette liste sait-tu utiliser?",
                choices=["Bootstrap", "Tailwind CSS", "Bulma", "Foundation", "Materialize", "Skeleton"],
                ignore=lambda answers: "CSS" not in answers["languages"]
            ),
            inquirer.Checkbox(
                "frameworks-py",
                message="Quels frameworks de cette liste sait-tu utiliser?",
                choices=["Inquirer", "Rich", "Pygame", "Frogmouth", "Ursina", "Django"],
                ignore=lambda answers: "Python" not in answers["languages"]
            ),
            inquirer.Confirm("restart", message="Recommencer le questionnaire?", default=False)
        ]

        answers = ask_questions(questions)
        frameworks_css = answers.get("frameworks-css", list())
        frameworks_py = answers.get("frameworks-py", list())
        frameworks = list()
        frameworks.extend([*frameworks_css, *frameworks_py])

        print(f"""Profil:
            nom: {answers['name']}
            âge: {answers['age']}
            genre: {answers['gender']}
            langages: {answers["languages"]}
            frameworks: {frameworks}""")
        
        if not answers["restart"]:
            break
