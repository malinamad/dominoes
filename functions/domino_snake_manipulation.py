def get_stock_piece(stock, player_pieces):
    """ Adds to players hand a piece from stock, therefore removes that piece from the stock """
    piece = stock[0]
    stock.remove(piece)
    player_pieces.append(piece)


def place_domino_in_front(domino_snake, player_pieces, piece):
    """ Adds a domino piece to the front (left) of the snake """
    player_pieces.remove(piece)
    domino_snake.insert(0, piece)


def place_domino_last(domino_snake, player_pieces, piece):
    """ Adds domino to the last (right) place of the snake """
    player_pieces.remove(piece)
    domino_snake.append(piece)


def reverse_domino_orientation_left(domino_snake, domino):
    """ Reverses domino orientation to the left in case it is to be placed to the left
        and the only fit value is the second """
    start_snake_num = domino_snake[0][0]
    if start_snake_num == domino[0]:
        domino.reverse()


def reverse_domino_orientation_right(domino_snake, domino):
    """ Reverses domino orientation to the left in case it is to be placed to the right
        and the only fit value is the second """
    last_snake_num = domino_snake[-1][1]
    if last_snake_num == domino[1]:
        domino.reverse()
