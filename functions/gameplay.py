from ai_algorithm.algorithms import (count_same_values_in_pieces_and_snake, get_domino_scores,
                                     highest_to_lowest_val_in_dict, get_domino_from_score_value)
from functions.domino_snake_manipulation import (get_stock_piece, place_domino_last,
                                                 place_domino_in_front, reverse_domino_orientation_left,
                                                 reverse_domino_orientation_right)
from validations.snake_validations import matching_number_validation_right, matching_number_validation_left


def player_makes_move(stock, domino_snake, domino_pieces, status):
    """ The player & computer moves """
    if status == 'player':
        while True:
            try:
                player_input = int(input())
                if player_input > 0:
                    piece = domino_pieces[player_input - 1]
                    validation = matching_number_validation_right(domino_snake, piece, status)
                    if validation is False:
                        continue
                    reverse_domino_orientation_right(domino_snake, piece)
                    place_domino_last(domino_snake, domino_pieces, piece)

                elif player_input < 0:
                    abs_player_input = abs(player_input)
                    piece = domino_pieces[abs_player_input - 1]
                    validation = matching_number_validation_left(domino_snake, piece, status)
                    if validation is False:
                        continue
                    reverse_domino_orientation_left(domino_snake, piece)
                    place_domino_in_front(domino_snake, domino_pieces, piece)

                else:
                    if stock:
                        get_stock_piece(stock, domino_pieces)
                break
            except (ValueError, IndexError):
                print('Invalid input. Please try again.')

    else:
        pieces_count = count_same_values_in_pieces_and_snake(domino_snake, domino_pieces)
        domino_score_dict = get_domino_scores(domino_pieces, pieces_count)
        sorted_score_list = highest_to_lowest_val_in_dict(domino_score_dict)

        while True:
            try:
                domino_score_dict, piece = get_domino_from_score_value(domino_score_dict, sorted_score_list)
            except TypeError:
                if stock:
                    get_stock_piece(stock, domino_pieces)
                break
            validation_right = matching_number_validation_right(domino_snake, piece, status)
            validation_left = matching_number_validation_left(domino_snake, piece, status)
            if validation_right is False and validation_left is False:
                continue
            elif validation_right is True:
                reverse_domino_orientation_right(domino_snake, piece)
                place_domino_last(domino_snake, domino_pieces, piece)
            elif validation_left is True:
                reverse_domino_orientation_left(domino_snake, piece)
                place_domino_in_front(domino_snake, domino_pieces, piece)
            break
