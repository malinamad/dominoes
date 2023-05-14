def turn_status(status_value, comp_pieces, player_pieces):
    """ Prints player's turn basing on the status value """
    if len(comp_pieces) == 0:
        print('Status: The game is over. The computer won!')
        return False
    elif len(player_pieces) == 0:
        print('Status: The game is over. You won!')
        return False
    elif status_value == 'computer':
        print('Status: Computer is about to make a move. Press Enter to continue...')
    else:
        print("Status: It's your turn to make a move. Enter your command.")


def display_your_pieces(domino_pieces):
    """ Prints player's domino pieces with indexes """
    print(f'Your pieces:')
    for piece in domino_pieces:
        piece_index = domino_pieces.index(piece)
        print(f'{piece_index + 1}:{piece}')
    print()


def print_domino_snake(domino_snake):
    """ Prints domino snake, if the length exceeds 6 domino,
        then only first and last three domino are shown """
    if len(domino_snake) > 6:
        left_side = ''.join(map(str, domino_snake[:3]))
        right_side = ''.join(map(str, domino_snake[-3:]))
        print(f'{left_side}...{right_side}')
    else:
        print(''.join(map(str, domino_snake)))


def identical_value_count(domino_snake):
    """ If the first and last values are identical, it starts
        to count how many of those values are in the block """
    if domino_snake[0][0] == domino_snake[-1][-1]:
        identical_value = domino_snake[0][0]
        val_count = 0
        for domino in domino_snake:
            for num in domino:
                if num == identical_value:
                    val_count += 1
        return val_count
    else:
        return None


def domino_draw_condition(domino_snake):
    """ If there are more than 7 identical values, the game is over """
    val_count = identical_value_count(domino_snake)
    if val_count is not None and val_count > 7:
        print('Status: The game is over. It\'s a draw!')
        return False
