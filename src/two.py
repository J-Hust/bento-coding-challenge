import re

def count_recurring(string) : 
  
    new_string = ''
    i = 0
    
    while i < len(string) - 1: 
        count = 1

        while string[i] == string[i + 1]:
            i += 1
            count += 1
              
            if i + 1 == len(string): 
                break

        new_string += string[i]
        if count > 1:
            new_string += str(count)

        i += 1

    # if last character was not repeated, add it in now
    if not re.match(r'[0-9]', new_string[-1]):
        new_string += string[-1]
      
    return new_string