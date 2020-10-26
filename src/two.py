import itertools


def count_recurring(string):

    new_string = ''
    i = 0
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