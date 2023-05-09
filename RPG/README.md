# README

## Enums
### Ethnic
- Human
- Elf
- Dwarf
### Ability
- STR
- DEX
- CON
- INT
- WIS
- CHA
### Slot
- Head
- Body
- Hand
- Legging
- Boots
## Item
- _id: `str`
- name: `str`
- description: `str`
- slot: `Slot`
- ability: `Dict[Ability, int]`
- price: `int`
- skill: `List[Callable]`
- image: `str`
    - should be the image url

## Character
present class: `Character`
### Attributes
- _id: `str`
- name: `str`
- ethnic: `Ethnic` 
- level: `int`
- experience: `int`
- MAX_experience: `int`
- money: `int`
- ability: `Dict[Ability, int]`
- hp: `int`
- MAX_hp: `int`
- mp: `int`
- MAX_mp: `int`
- equipment: `Dict[Slot, Item]`
- inventory: `List[Item]`
### Methods
- create: `classmethod`
  - Args: `Dict[str, Any]`
    - Return: `Character`

