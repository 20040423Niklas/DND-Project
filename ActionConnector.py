import monster
from rich import print
import monster_type
import monster
from dice import set_dices
import sys

last_monster_class = None
tracker_list = monster.tracker_list

class Aktions():

    def ask_input(self):
        return input("> ")

    def out(self):
        print("sd")

    def remove(self):
        print("remove")

    def add(self):
        print("Willst du ein premade Monster wählen?")
        print("[blue]{monster}[/blue]")
        print("")
        print("oder durch [b]leere Eingabe[/b] das letzte Monster nehmen: [yellow]{monster}[/yellow]")
        print("oder durch [green][+][/green] ein neues Monster Typ erstellen")
        user_input = self.ask_input()
        if user_input == "":
            pass
        elif user_input == "monster":
            data = monster_type.get_monster_types()
            monster_name_list = [type.MONSTER_NAME for type in data]
            print("available Monster types:")
            for element in monster_name_list:
                print(f"{monster_name_list.index(element)}:{element}")
            entered_monster = self.ask_input()
            type = data[int(entered_monster)]
            print(type.HP_DICE)
            dice_set = set_dices(type.HP_DICE)
            m = monster.Monster(type.MONSTER_NAME,type.CONST_HP,dice_set,type.DEATH_ABI)
        elif user_input == "+":
            print("bitte gebe einen namen ein: ")
            monster_name = self.ask_input()
            print("bitte gebe die const - hp ein: ")
            const_hp = int(self.ask_input())
            print("gebe die Würfel ein: ")
            hp_dice = self.ask_input()
            
            monster_type.add_monster_type(monster_name,const_hp,hp_dice)
            type = monster_type.monster_type_list[-1]
            monster.Monster(type.MONSTER_NAME,type.CONST_HP,set_dices(type.HP_DICE))
            
    def rename(self):
        print("Wähle einen índex:")
        index = self.ask_input()
        tracker_list[int(index)].rename()
    
    def change(self):
        print("Gebe einen index ein:")
        index = self.ask_input()
        index = int(index)
        print("Gebe einen Schadenswert ein:")
        damage = int(self.ask_input())
        tracker_list[index].change_hp(damage)

    
   



            



            



class AktionConnector(Aktions):
    
    def __init__(self):
        pass

    def execute_function(self, function_name: str):
        function = self.__getattribute__(function_name)
        function()
        
        




