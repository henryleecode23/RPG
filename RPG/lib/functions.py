from random import randint

def randomAbilityScore():
    """
    Return a random ability score.
    The sum of all scores is 25.
    """
    ability = [1, 1, 1, 1, 1, 1]
    for _ in range(19):
        ability[randint(0, 5)] += 1
    return ability
