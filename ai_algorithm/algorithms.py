domino_dict_key_name = 'domino'
domino_dict_value_name = 'value'


def count_domino_encounter(domino_hand, domino_nums, current_val):
    """ Counts domino encounter in the snake and adds value to the provided dictionary in params """
    for domino in domino_hand:
        for val in domino:
            if val == current_val:
                domino_nums[current_val] += 1


def count_same_values_in_pieces_and_snake(domino_snake, comp_pieces):
    """ Adds the amount of the identical numbers from the players hand and the domino snake
        to the dictionary created from comprehension """
    num_dict = {k: 0 for k in range(7)}

    for key in num_dict.keys():
        count_domino_encounter(domino_snake, num_dict, key)
        count_domino_encounter(comp_pieces, num_dict, key)

    return num_dict


def get_domino_scores(comp_pieces, num_count_dict):
    """ Returns dictionary with domino and its score value """
    domino_scores_dict = []

    for domino in comp_pieces:
        val = 0
        for num in domino:
            val += num_count_dict[num]
        domino_scores_dict.append(
            {domino_dict_key_name: domino,
             domino_dict_value_name: val})

    return domino_scores_dict


def highest_to_lowest_val_in_dict(list_dict):
    """ Gets all score values, then sorts the list from the highest to the lowest value
        and returns that list for a later use """
    val_lst = []

    for dic in list_dict:
        for k, v in dic.items():
            if domino_dict_value_name == k:
                val_lst.append(v)
    val_lst.sort(reverse=True)

    return val_lst


def get_domino_from_score_value(domino_hand, scores):
    """ Returns domino piece with the highest score value, and updates the list and the dictionary with removing
        the highest value from list, and the domino with that value from the list with dictionaries,
        in order to be able to use that value during iterations outside the function """
    # Iterates through the list with dicts
    for domino in domino_hand:
        # Unpacking dict with domino and its score value
        for k, v in domino.items():
            # To find the domino that has that value
            if k == domino_dict_value_name and v == scores[0]:
                domino_piece = domino[domino_dict_key_name]

                # Looks up an index of domino and value to remove later
                index = next((index for (index, d) in enumerate(domino_hand)
                              if d[domino_dict_value_name] == scores[0]),
                             None)

                # Clearing the data to avoid the reps
                del domino_hand[index]
                scores.pop(0)

                return domino_hand, domino_piece
