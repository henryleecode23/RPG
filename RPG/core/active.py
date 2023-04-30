from RPG.core import Character

def attack(attacker: Character, target: Character, hit_chance: int = 75, defend_chance: int = 40):
    if (attacker.attack_check(hit_chance)):
        if (target.defend_check(defend_chance)):
            print(f"{attacker.name} attack {target.name} but {target.name} defend")
        else:
            print(f"{attacker.name} attack {target.name} and {target.name} take damage")
            target.HP -= attacker.STR
    else:
        print(f"{attacker.name} miss {target.name}")
