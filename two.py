def thing(string):
    i = 0
    new_string = ''
    while i < len(string):
        counter = 1
        while string[i + 1] == string[i]:
            count += 1
            i += 1

            if i + 1 == len(string):
                break

            new_string
        print(string[i])
        i += 1


thing('hello')

def hmm(string):
    new_string = ''
    i = 0
    while i < len(string):
        counter = 1
        if i + counter < len(string):
        while string[i+counter] == string[i]:
            counter += 1
        new_string += string[i]
        if counter > 1:
            new_string += str(counter)
            i += counter  # skip the number we just added
        else:
            i += 1

    print(new_string)
    return new_string


hmm('hello')