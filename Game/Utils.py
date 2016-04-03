__author__ = "Felix Hubert"

import random


def verify_bet(previous, current):
    """
    Verify if the current bet is 'better' than the previous bet.
    To be 'better', refer to the rules of Perudo (higher value dice or higher quantity)
    Will return true if it is and false if not
    :param previous: quantity-value array
    :param current: quantity-value array
    :return: boolean
    """
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
    """
    Will simulate an AI betting based on the previous bet to beat and
    the number of dice available. Will calculate the odds of having a certain
    quantity of dice, and will take his bet considering that. If the odds are not in
    its favor, the AI bet will call a 'bullshit' response.

    To simulate a true player behavior, we should calculate the odds based with
    the die the AI possess. For example, if an AI have 6 dice of the same value,
    the odds are in his favor to go with a higher quantity than 6 on a 36 dice round.
    :param previous: quantity-value array
    :param dice_number: Number of total dice currently used in the game
    :return: bet
    """
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
    """
    Will return a random value higher than the previous value. Used by the AI
    to sometimes up the value of the dice and not the quantity.
    :param previous_value: quantity-value array
    :return: choice_array
    """
    choices = [1]
    for i in range(1, 7):
        if i > previous_value:
            choices.append(i)
        return random.choice(choices)
