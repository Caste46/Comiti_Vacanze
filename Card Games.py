def get_rounds(number):
    """
 
     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    return [number, number + 1, number + 2] 
    
def concatenate_rounds(rounds_1, rounds_2):
    """
 
    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2
    
def list_contains_round(rounds, number):
    """
 
    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    if(number in rounds):
        return True
    else:
        return False
        
def card_average(hand):
    """
 
    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    total = 0
    for item in hand:
        total += item
    return total / len(hand)
    
def approx_average_is_average(hand):
    """
 
    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """
    first_average = card_average([hand[0], hand[-1]])
    second_average = hand[int(len(hand) / 2)]
    real_average = card_average(hand)
    if((first_average == real_average) or (second_average == real_average)):
        return True
    else:
        return False
    
def average_even_is_average_odd(hand):
    """
 
    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    list_even = hand[::2]
    sum_even = sum(list_even)
    list_odd = hand[1::2]
    sum_odd = sum(list_odd)
    average_even = sum_even / len(list_even)
    average_odd = sum_odd / len(list_odd)
    if(average_even == average_odd):
        return True
    else:
        return False
    
def maybe_double_last(hand):
    """
 
    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22
    return hand