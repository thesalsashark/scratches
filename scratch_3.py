import random
import itertools
import tabulate
import PrettyTable

weapons = {'Fist': {'+atk': 0, 'Cost': 10},
           'Wooden Sword': {'+atk': 2, 'Cost': 20},
           'Rusty Sword': {'+atk': 4, 'Cost': 30},
           'Iron Sword': {'+atk': 6, 'Cost': 40},
           'Steel Sword': {'+atk': 8, 'Cost': 50},
           'Sword of Crushing Puss': {'+atk': 100, 'Cost': 10000}}


armor = {"Travelers Cloths": {'+def': 0, 'Cost': 10},
         'Cloth Armor': {'+def': 2, 'Cost': 100},
         'Leather Armor': {'+def': 4, 'Cost': 150},
         'Iron Armor': {'+def': 6, 'Cost': 200},
         'Mail Armor': {'+def': 8, 'Cost': 250},
         'Steel Armor': {'+def': 10, 'Cost': 300}}


class Player:
    def __init__(self, name, curweap=None, curarmor=None):
        if curweap is None:
            curweap = random.choice(list(weapons.keys()))
        if curarmor is None:
            curarmor = random.choice(list(armor.keys()))
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 14
        self.base_defense = 5
        self.critical = .05
        self.gold = 10000
        self.pots = 1
        self.curweap = curweap
        self.weap = []
        self.curarmor = curarmor
        self.armor = []
        self.location = 'D2'
        self.game_over = False

    @property
    def attack(self):
        attack = self.base_attack + weapons[player.curweap]['+atk']
        return attack

player = Player("Tomer")
# weapatk = weapons[player.curweap]['+atk']
# player.curweap = random.choice(list(weapons.keys()))
# print(player.curweap + ': ' + str(weapons[player.curweap]['+atk']))
# print('Base attack: ' + str(player.base_attack))
# print('Player attack: ' + str(player.attack))


def main():
    print(input("Select 1 for Weapons or 2 for Armor"))
    option = input("-> ")
    if option is '1':
        weapons_store()
    elif option is '2':
        armor_store()
    else:
        main()

def weapons_store():
    weapon_name = max(map(len, weapons)) + 2
    weapon_atk = len(str(max(int(d['+atk']) for d in weapons.values()))) + 2
    weapon_cost = len(str(max(int(d['Cost']) for d in weapons.values())))

    print("{:<{weapon_name}} {:<{weapon_atk}} {:<{weapon_cost}}".format('Weapon', 'Atk', 'Cost', weapon_name=weapon_name, weapon_atk=weapon_atk, weapon_cost=weapon_cost))
    for (k1, v1) in weapons.items():
        Atk = v1["+atk"]
        Cost = v1["Cost"]
        print("{:<{weapon_name}} {:<{weapon_atk}} {:<{weapon_cost}}".format(k1, Atk, Cost, weapon_name=weapon_name, weapon_atk=weapon_atk, weapon_cost=weapon_cost))
    option = input("You have %s gold. What would you like to buy?" % player.gold)
    if option is not None:
        player.curweap = list(armor.keys())[(int(option) - 1)] ##get the key the corresponds to the number typed in
        print(player.curweap)
    main()


def armor_store():
    armor_name = max(map(len, armor)) + 2
    armor_def = len(str(max(int(d['+def']) for d in armor.values()))) + 2
    armor_cost = len(str(max(int(d['Cost']) for d in armor.values())))

    print("{:<{armor_name}} {:<{armor_def}} {:<{armor_cost}}".format('Armor', 'Def', 'Cost', armor_name=armor_name, armor_def=armor_def, armor_cost=armor_cost))
    for (k1, v1) in enumerate(armor.items()):
        Def = v1["+def"]
        Cost = v1["Cost"]
        print("{:<{armor_name}} {:<{armor_def}} {:<{armor_cost}}".format(k1, Def, Cost, armor_name=armor_name, armor_def=armor_def, armor_cost=armor_cost))
    option = input("You have %s gold. What would you like to buy?" % player.gold)
    if option is not None:
        player.curarmor = list(armor.keys())[(int(option) - 1)] ##get the key the corresponds to the number typed in
        print(player.curarmor)
    main()

# main()

print("{} : {:<22} : {:^5} : {:^5}".format('Num', 'Name', '+atk', 'Cost'))
for num, (k, v) in enumerate(weapons.items(), start=1):
    print("{:<3} : {:<22} : {:^5} : {:^5}".format(num, k, v['+atk'], v['Cost']))

t = tabulate(['Num', 'Name', '+atk', 'Cost'])
for num, (k, v) in enumerate(weapons.items(), start=1):
    t.add_row(num, (k,v))
print(t)