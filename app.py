'''
Module for find_pairs_sum function that finds pairs of integers from a list that
sum to a given value(target_sum).
'''

def find_pairs_sum(numbers_set: set, target_sum: int):
    '''
    Function taking input the list of numbers as well as the target sum
    '''
    is_list_length_valid = len(numbers_set) >= 2
    pairs = set()

    if not is_list_length_valid:
        return "Wrong input. Please provide a list of two (or more) integers"

    for current_number in numbers_set:
        complement = target_sum - current_number
        if complement in numbers_set and complement != current_number:
            pairs.add(tuple(sorted([current_number, complement])))

    result = "No pairs were found" if len(pairs) == 0 else pairs

    print("List: " + str(numbers_set))
    print("Target sum: " + str(target_sum))
    print("Result: " + str(result) + '\n')

    return result
