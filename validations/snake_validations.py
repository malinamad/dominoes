error_message = 'Illegal move. Please try again.'
player_status = 'player'


def matching_number_validation_left(domino_snake, player_domino, status):
    """ Checks whether it is possible to place a provided domino piece to left of the snake """
    start_snake_num = domino_snake[0][0]
    if (start_snake_num == player_domino[0]
            or start_snake_num == player_domino[1]):
        return True
    else:
        if status == player_status:
            print(error_message)
        return False


def matching_number_validation_right(domino_snake, player_domino, status):
    """ Checks whether it is possible to place a provided domino piece to right of the snake """
    last_snake_num = domino_snake[-1][1]
    if (last_snake_num == player_domino[0]
            or last_snake_num == player_domino[1]):
        return True
    else:
        if status == player_status:
            print(error_message)
        return False
