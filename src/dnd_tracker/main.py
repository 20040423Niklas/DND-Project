import dice, monster, os, monster_type
from rich import print

tracker_list = monster.tracker_list

def add():
    print("Willst du ein premade Monster wählen?")
    print("[blue]{monster}[/blue]")
    print("")
    print("oder durch [b]leere Eingabe[/b] das letzte Monster nehmen: [yellow]{monster}[/yellow]")
    print("oder durch [green][+][/green] ein neues Monster Typ erstellen")
    if(ask_input() == ""):
        pass
    pass # Frage, ob [premade Monster wählen] [Leere Eingabe = letztes gewähltes premade Monster] ["+" = Spontan Monster erstellen]

def kill(): #Monster töten aber mit death abillity /Niklas 
    pass

def change(): #hp verändern /Niklas
    pass

def edit(): #speziell zur Bearbeitung von Monster stets /Artur
    pass

def rename(): #persönlichen Namen von Monstern ändern /Niklas
    pass

def heal(): #zum heilen von Monstern /Artur
    pass

def damage(): #zum schaden von monstern/Artur
    pass

def save(): #zum speichern von Spielständen /Niklas
    pass

def load(): #zum laden von Spielständen /Niklas
    pass

def delete(): #zum sofortigen löschen von Monstern /Artur
    pass


command_collection = {"add":add,"kill":kill,"change":change,"heal":heal,"damage":damage,"load":load,"save":save,"rename":rename,"edit":edit}

# [color][/color] [][/]

def clear_terminal():
    os.system("cls")

def ask_input():
    return input("> ")

command_string = ""
for command in command_collection.keys():
    command_string = command_string + f"[green]{command}[/green], "


while True:
    clear_terminal()
    monster.show_list()
    print(f"Mögliche Commands: {command_string}")

    user_input = input("> ")

    if user_input == "exit":
        break

    try:
        command_collection[user_input]()
    except:
        print("Unknown Command")
