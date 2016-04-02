__author__ = "Felix Hubert"

import random


def verify_bid(previous, current):
    previous_quantity = int(previous[0])
    previous_value = int(previous[1])
    current_quantity = int(current[0])
    current_value = int(current[1])

    if current_quantity == -1 and current_value == -1:
        return True

    if current_quantity > previous_quantity:
        return True
    elif current_quantity == previous_quantity:
        if current_value > previous_value:
            if previous_value == 1:
                return False
            return True
        if current_value == 1 and previous_value != 1:
            return True
    return False


def AI_bet(previous, dice_number):
    dice_probability = float(dice_number) / 6

    previous_quantity = previous[0]
    previous_value = previous[1]

    if previous_quantity > dice_probability:
        return [-1, -1]

    if previous_quantity == 0:
        return [1, up_value(previous_value)]

    action = random.randint(1, 2)

    if action == 1:
        if previous_quantity + 1 <= dice_probability:
            return [previous_quantity + 1, previous_value]
        else:
            return [-1, -1]
    else:
        if previous_value == 1:
            return [previous_quantity + 1, random.choice(range(1, 7))]
        else:
            return [previous_quantity, up_value(previous_value)]


def up_value(previous_value):
    choices = [1]
    for i in range(1, 7):
        if i > range:
            choices.append(i)
        return random.choice(choices)
