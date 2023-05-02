from RPG.lib.functions import *

from enum import Enum
from typing import Callable, Union, List
from random import randint, choice

class AbilityText(Enum):
    STR = "Strength"
    DEX = "Dexterity"
    CON = "Constitution"
    INT = "Intelligence"
    WIS = "Wisdom"
    CHA = "Charisma"

class Ethnic(Enum):
    Human = 0       # 人類
    Elf = 1         # 精靈
    Dwarf = 2       # 矮人


class EquipmentSlot(Enum):
    Head = 0
    Necklace = 1
    Chest = 2
    Ring1 = 3
    Ring2 = 4
    Ring3 = 5
    Ring4 = 6
    Leggings = 7
    Boots = 8
    Back = 9
    MainHand = 10
    OffHand = 11

class Item:
    def __init__(self):
        self.name:str
        self.description:str
        self.slot:EquipmentSlot
        self.specialEffect: Union[Callable, None]
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Equipment({self.name})"

class Character:
    def __init__(self):
        self._id:str # ID
        self.name:str # 名稱 (Name)
        self.ethnic: Ethnic = None # 種族
        self.level:int = None # 等級 (Level)
        self.MAX_experience:int = None # 最大經驗值 (Max Experience)
        self.experience:int = None # 經驗值 (Experience)

        self.STR:int # 力量 (Strength)
        self.DEX:int # 敏捷 (Dexterity)
        self.CON:int # 體質 (Constitution)
        self.INT:int # 智力 (Intelligence)
        self.WIS:int # 智慧 (Wisdom)
        self.CHA:int # 魅力 (Charisma)

        self.MAX_HP:int # 最大生命值 (Max Health Point)
        self.MAX_MP:int # 最大魔力值 (Max Mana Point)
        self.HP:int # 生命值 (Health Point)
        self.MP:int # 魔力值 (Mana Point)

        self.equipment:dict[EquipmentSlot, Item] = {} # 使用中的裝備 (Equipment)
        self.inventory: List[Item] = [] # 背包 (Inventory)


    def __str__(self):
        return f"{self.name}(Lv.{self.level})"

    def __repr__(self):
        return f"{self.ethnic}({self.name})"

    def to_dict(self):
        return {
            "_id": self._id,
            "name": self.name,
            "ethnic": self.ethnic,
            "level": self.level,
            "experience": self.experience,
            "STR": self.STR,
            "DEX": self.DEX,
            "CON": self.CON,
            "INT": self.INT,
            "WIS": self.WIS,
            "CHA": self.CHA,
            "MAX_HP": self.MAX_HP,
            "MAX_MP": self.MAX_MP,
            "HP": self.HP,
            "MP": self.MP
        }

    @classmethod
    def create(cls, id:str, name:str, ethnic: Ethnic, level:int, experience:int, STR:int, DEX:int, CON:int, INT:int, WIS:int, CHA:int, MAX_HP:int, MAX_MP:int,HP:int, MP:int):
        character = cls()
        character._id = id
        character.name = name
        character._ethnic = ethnic
        character.level = level
        character.experience = experience
        character.MAX_experience = character.level * 100 * 1.3
        character.STR = STR
        character.DEX = DEX
        character.CON = CON
        character.INT = INT
        character.WIS = WIS
        character.CHA = CHA
        character.MAX_HP = MAX_HP
        character.MAX_MP = MAX_MP
        character.HP = HP
        character.MP = MP
        return character

    @classmethod
    def create_from_dict(cls, data:dict):
        try:
            character = cls.create(
                data["_id"],
                data["name"],
                data["ethnic"],
                data["level"],
                data["experience"],
                data["STR"],
                data["DEX"],
                data["CON"],
                data["INT"],
                data["WIS"],
                data["CHA"],
                data["MAX_HP"],
                data["MAX_MP"],
                data["HP"],
                data["MP"])
        except KeyError as e:
            raise KeyError(f"KeyError: {e} is not found in {data}")
        return character

    @classmethod
    def random_create(cls, id:str, name:str):
        character = cls()
        character._id = id
        character.name = name
        character.ethnic = choice([e.name for e in Ethnic])
        character.level = 1
        character.MAX_experience = 100 if character.level == 1 else character.level * 50 * 1.3
        character.experience = 0
        AbilityScore = randomAbilityScore()
        character.STR = AbilityScore[0]
        character.DEX = AbilityScore[1]
        character.CON = AbilityScore[2]
        character.INT = AbilityScore[3]
        character.WIS = AbilityScore[4]
        character.CHA = AbilityScore[5]
        character.MAX_HP = character.CON * 10
        character.MAX_MP = character.INT * 10
        character.HP = character.MAX_HP
        character.MP = character.MAX_MP
        return character


    def attack_check(self, chance:int = 75):
        if randint(0, 100) <= chance:
            return True
        else:
            return False

    def defend_check(self, chance:int = 40):
        if randint(0, 100) <= chance:
            return True
        else:
            return False

    def info(self):
        print("========================================")
        print(f"{self.name} (Lv.{self.level})")
        print(f"id: {self._id}")
        print(f"經驗值: {self.experience}/{self.MAX_experience}")
        print(f"生命值: {self.HP}/{self.MAX_HP}")
        print(f"魔力值: {self.MP}/{self.MAX_MP}")
        print("")
        print(f"力量: {self.STR}")
        print(f"敏捷: {self.DEX}")
        print(f"體質: {self.CON}")
        print(f"智力: {self.INT}")
        print(f"智慧: {self.WIS}")
        print(f"魅力: {self.CHA}")
        print("========================================")
    
    def attribute_update(self):
        self.MAX_HP = self.CON * 10
        self.MAX_MP = self.INT * 10
        self.HP = self.MAX_HP
        self.MP = self.MAX_MP

    def level_up(self):
        self.level += 1
        self.MAX_experience = self.level * 100 * 1.3
        print(f"{self.name} 升級了！")
