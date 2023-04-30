def find_cogs(path: str) -> list:
    """Find all cogs in a path"""
    from os import walk
    cogs = []
    for t in walk(path):
        path = t[0][2:].replace("/", ".")
        files = t[2]
        for file in files:
            if file.endswith(".py"):
                cogs.append(path+"."+file[:-3])
    return cogs

def get_config(path: str) -> dict:
    """Get config from a path"""
    from json import load
    return load(open(path, "r"))

def get_player(player: str, database) -> dict:
    """Get a player from database"""
    return database.Player.find_one({"id": player})

def is_player_exist(player: str, database) -> bool:
    """Check if a player exist in database"""
    r = database.Player.find_one({"id": player})
    return r != None

def save_player(player, database) -> None:
    from RPG.core import Character
    player: Character
    if isinstance(player, Character):
        database.Player.insert_one(player.to_dict())

def kill_player(player: str, database) -> None:
    """Kill a player"""
    database.Player.delete_one({"id": player})

