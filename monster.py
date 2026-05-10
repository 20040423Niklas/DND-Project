tracker_list = [] # Haltet alle aktiven Kreaturen


class DeathAbility:
    pass
DEATH_ABI_ARRAY = []


class Monster:
    def __init__(self, typ="mustermann", const_hp=0, hp_dice=[], death_abi=None): 

        self.name = typ.capitalize()
        self.TYPE = typ.capitalize()
        self.CONST_HP = const_hp if type(const_hp) is int else int(const_hp)
        self.HP_DICE = hp_dice       # HP Dices werden durch for loop durchgeprobt und müssen darum eine Liste sein
        self.DEATH_ABI = death_abi

        self.cur_hp = 0

        for dice in self.HP_DICE:
            self.cur_hp += dice.roll()
        self.cur_hp += self.CONST_HP

        self.MAX_HP = self.cur_hp

        tracker_list.append(self) # Wird automatisch in der Tracker Liste hinzugefügt
        # Name - Type - Constant HP - HP Dice - Death Ability - Current HP - Max HP

    def __str__(self): # Zeigt den bloßen Variablennamen als modifizierter String auf
        return f"{self.name} - {self.TYPE} - {self.cur_hp}/{self.MAX_HP}"

    def death_sequence(self):
        """Eine Funktion, die nach bestätigtem Tod eine Death Ability ausführt, sofern es gibt"""
        if self.DEATH_ABI in DEATH_ABI_ARRAY:
            self.DEATH_ABI()
        else:
            tracker_list.remove(self)

    def check_if_dead(self):
        if self.cur_hp < 1:
            self.death_sequence()

    def set_name(self, new_name):
        self.name = new_name

    def set_type(self, new_type):
        self.TYPE = new_type

    def set_death_ability(self,new_abi):
        self.DEATH_ABI = new_abi

    def set_current_hp(self, new_cur):
        if new_cur > self.MAX_HP:
            print("exceeds maximum hp limit - raise hp map via. set_max_hp.")
        self.cur_hp = max(0, min(new_cur, self.MAX_HP))
        # Im Fall das es passieren sollte (warum auch immer)
        if self.cur_hp <= 0:
            self.check_if_dead()

    def set_max_hp(self, new_max):
        self.MAX_HP = new_max

    def change_hp(self, change):
        new_hp = self.cur_hp + change
        self.set_current_hp(new_hp)
    
    """
    Warum nicht HP_DICE und CONST_HP?
    Weil, du dummer hund (ey, sei nicht so gemein), diese Werte nur bei der Erstellung der Klasse benutzt werden und nicht mehr beachtet werden.
    Sehr wahrscheinlich bin ich selber ein dummer hun um eine temporärer Eintrag in einer Variable zu stopfen, habe gerade zu viel kopfschmerzen um es zu ändern.
    """


def show_list():
    for i in range(len(tracker_list)):
        print(f"{i} : {tracker_list[i]}")
