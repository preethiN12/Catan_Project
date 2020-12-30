def rollDice(getNumbDice):
    import random
    rollResult = []
    for i in range(getNumbDice):
        roll_dice = random.randint(1, 6)
        rollResult.append(roll_dice)
    print(rollResult)
    return rollResult

rollDice(2)