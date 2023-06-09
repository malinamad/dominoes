from functions.game_interface import (turn_status, display_your_pieces,
                                      print_domino_snake, domino_draw_condition)
from functions.game_prep import (generate_domino_set, split_domino,
                                 determine_first_player, determine_starting_domino)
from functions.gameplay import player_makes_move


def launch_the_domino_game():
    """ Main function """
    domino_set = generate_domino_set()

    stock_pieces = split_domino(domino_set, 14)
    computer_pieces = split_domino(domino_set, 7)
    player_pieces = domino_set

    status = determine_first_player(computer_pieces, player_pieces)
    domino_snake = determine_starting_domino(computer_pieces, player_pieces)

    while True:
        print('=' * 70)
        print(f'Stock pieces: {len(stock_pieces)}')
        print(f'Computer pieces: {len(computer_pieces)} \n')
        print_domino_snake(domino_snake)
        print()

        display_your_pieces(player_pieces)

        run_game = turn_status(status, computer_pieces, player_pieces)
        if run_game is False:
            break
        run_game = domino_draw_condition(domino_snake)
        if run_game is False:
            break

        if status == 'player':
            player_makes_move(stock_pieces, domino_snake, player_pieces, status)
        else:
            input()
            player_makes_move(stock_pieces, domino_snake, computer_pieces, status)
        status = 'player' if status == 'computer' else 'computer'


if __name__ == '__main__':
    launch_the_domino_game()
