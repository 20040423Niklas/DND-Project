import dice, monster, os, monster_type
from rich import print

tracker_list = monster.tracker_list

monster.Monster("Goblin", 2, dice.set_dices("3w4"))
monster.Monster("Goblin", 2, dice.set_dices("3w4"))
monster.Monster("Goblin", 2, dice.set_dices("3w4"))
monster.Monster("Goblin", 2, dice.set_dices("3w4"))
monster.Monster("Goblin", 2, dice.set_dices("3w4"))

# [color][/color] [][/]

def clear_terminal():
    os.system("cls")

def ask_input():
    return input("> ")

while True:
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
    clear_terminal()
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
