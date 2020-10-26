import itertools


def count_recurring(string):
    '''
    Takes in a string of lower-case letters and returns a new string containing those letters.
    Adjacent occurances are replaced by the number of occurrances.
    '''

    new_string = ''
    count = 1
    
    for x, y in itertools.zip_longest(string, string[1:]):
        if x == y:
            count += 1
        else:
            new_string += x
            if count > 1:
                new_string += str(count)
            count = 1

    return new_string