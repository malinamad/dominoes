from random import shuffle, sample

def generate_domino_set():
    """ Generates unique dominoes set and returns it in a list """
    domino_set = []
    for num in range(7):
        for num_sec in range(7):
            if [num_sec, num] not in domino_set:
                domino_set.append([num, num_sec])
    return domino_set


def split_domino(domino_set, quantity):
    """ Splits the domino set between players and stock """
    shuffle(domino_set)
    pieces = sample(domino_set, quantity)
    for piece in pieces:
        domino_set.remove(piece)
    return pieces

def players_max_values(first_player_list, second_player_list):
    """ Gets max domino from one of the players """
    return max(first_player_list), max(second_player_list)

def determine_first_player(first_player_list, second_player_list):
    """ Determines on the highest combination or double of the players
        who will be the first player to start """
    max_computer_piece, max_player_piece = players_max_values(first_player_list,
                                                              second_player_list)
    first_player = 'player' if max_computer_piece > max_player_piece else 'computer'
    return first_player


def determine_starting_domino(first_player_list, second_player_list):
    """ Returns the combination of starting point which is the highest one among the players, and
        also removes that highest from the player's list who has that value """
    domino_snake = []
    max_computer_piece, max_player_piece = players_max_values(first_player_list,
                                                              second_player_list)
    if max_computer_piece > max_player_piece:
        first_player_list.remove(max_computer_piece)
        domino_snake.append(max_computer_piece)
    else:
        second_player_list.remove(max_player_piece)
        domino_snake.append(max_player_piece)
    return domino_snake