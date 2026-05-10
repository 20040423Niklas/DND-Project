import csv
import dice
from ActionConnector import Aktions

monster_type_list = []

"""
0 = Name des Monsters
1 = Konstante HP Modifier
2 = HP Würfeln
3 = Todes Fähigkeit
"""

#def load_monster_types():
 #   with open("monster_type_set.csv", "r", newline="") as save_file:
  #      saved_data = csv.reader(save_file, delimiter=";")
   #     for monster in saved_data:
    #        monster_type_list.append(monster_type(monster[0], monster[1], monster[2], monster[3]))
    #return monster_type_list

class monster_type:
    def __init__(self, monster_name, const_hp, hp_dice, death_abi):
        self.MONSTER_NAME = monster_name
        self.CONST_HP = const_hp
        self.HP_DICE = hp_dice
        self.DEATH_ABI = death_abi

    def __str__(self): # Zeigt den bloßen Variablennamen als modifizierter String auf
        return f"{self.MONSTER_NAME} - {self.CONST_HP} - {self.HP_DICE} - {self.DEATH_ABI}"
    
    def get_dices_as_string(self):
        string_parts = []
        dice_names = []
        for dice in self.HP_DICE:
            dice_names.append(dice.DICE_NAME)
        for dice_kind in dice.array:
            number_of_dices = dice_names.count(dice_kind.DICE_NAME)
            if number_of_dices > 0:
                string_parts.append(f"{number_of_dices}w{dice_kind.DICE_NAME}")
        return ",".join(string_parts)

with open("monster_type_set.csv", "r", newline="") as save_file:
    saved_data = csv.reader(save_file, delimiter=";")
    for monster in saved_data:
        monster_type_list.append(monster_type(monster[0], monster[1], monster[2], monster[3]))

def get_monster_types():
    return monster_type_list
    
def save_monster_types():
    with open("test_monster_type_set.csv", "w", newline="") as save_file:
        written_data = csv.writer(save_file, delimiter=";")
        for monster in monster_type_list:
            written_data.writerow([monster.MONSTER_NAME, monster.CONST_HP, monster.HP_DICE, monster.DEATH_ABI])

def add_monster_type(monster_name,const_hp,hp_dice):
    new_type = monster_type(monster_name=monster_name, const_hp=const_hp, hp_dice=hp_dice, death_abi=None)
    monster_type_list.append(new_type)


