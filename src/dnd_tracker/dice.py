import random

class Dice:
    def __init__(self, dice_name, max_num):
        self.DICE_NAME = dice_name
        self.MAX_NUM = max_num

    def __str__(self):
        return self.DICE_NAME

    def roll(self):
        return random.randint(1, self.MAX_NUM)
    
    def roll_with_advantage(self):
        roll_1 = self.roll()
        roll_2 = self.roll()
        return {"primary_roll":max(roll_1, roll_2),"secondary_roll":min(roll_1, roll_2)}

    def roll_with_disadvantage(self):
        roll_1 = self.roll()
        roll_2 = self.roll()
        return {"primary_roll":min(roll_1, roll_2),"secondary_roll":max(roll_1, roll_2)}
    


w4 = Dice("w4", 4)
w6 = Dice("w6", 6)
w8 = Dice("w8", 8)
w10 = Dice("w10", 10)
w12 = Dice("w12", 12)
w100 = Dice("w100", 100)
w20 = Dice("w20", 20)

array = [w4, w6, w8, w10, w12, w100, w20]

# Funktion, welches das aufschreiben fon Würfelarray vereinfacht, so wie def set_dices("5w20")    
def set_dices(input_dice):
    dice_set = []
    try:
        count_str, sides_str = input_dice.lower().split('w')
        count = int(count_str)
        sides = int(sides_str)
    except (ValueError, AttributeError):
        raise ValueError("Notation must be in format 'XwY', e.g. '6w4' for six 4-sided dice.")
    
    for i in array:
        if sides == i.MAX_NUM:
            for y in range(count):
                dice_set.append(i)
            break

    return dice_set
