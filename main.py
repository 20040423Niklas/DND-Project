import dice, monster, os, monster_type
from rich import print
from ActionConnector import AktionConnector
import sys

action_handler = AktionConnector()

tracker_list = monster.tracker_list

# [color][/color] [][/]
def new_funktion():
    return None

def clear_terminal():
    os.system("cls")

def ask_input():
    return input("> ")

while True:
    clear_terminal()
    monster.show_list()
    print("")
    print("Mögliche Commands:"
    "[green]add[/green], "
    "[green]rename[/green], "
    "[green]change[/green], "
    "[green]kill[/green], "
    "[green]heal[/green], "
    "[green]save[/green], "
    "[green]load[/green], "
    "[green]delete[/green]")
    user_input = input("> ")

    if user_input=="exit":
        monster_type.save_monster_types()
        break

    #try:
    action_handler.execute_function(user_input)
    #except:
     #   print(f"Command {user_input} not found")


    """
    if(user_input == "add"):
        print("Willst du ein premade Monster wählen?")
        print("[blue]{monster}[/blue]")
        print("")
        print("oder durch [b]leere Eingabe[/b] das letzte Monster nehmen: [yellow]{monster}[/yellow]")
        print("oder durch [green][+][/green] ein neues Monster Typ erstellen")
        if(ask_input() == ""):
            pass
        pass # Frage, ob [premade Monster wählen] [Leere Eingabe = letztes gewähltes premade Monster] ["+" = Spontan Monster erstellen]
    elif(user_input == "rename"):
        pass
    elif(user_input == "change"):
        pass
    elif(user_input == "kill"):
        pass
    elif(user_input == "heal"):
        pass
    elif(user_input == "save"):
        pass
    elif(user_input == "load"):
        pass
    elif(user_input == "delete"):
        pass
"""