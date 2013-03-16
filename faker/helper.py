import re
import random
def slugify(istring):
    return re.sub(r'\W+','.',istring.lower())

# parses string for a symbol and replace it with a random number from 1-10
def replace_symbol_with_number(istring, symbol=False):
    # default symbol is '#'
    if not symbol:
        symbol = '#'
    ostring = ''
    for i in range(len(istring)):
        if istring[i] == symbol:
            ostring += str(random.randint(0,10))
        else:
            ostring += istring[i]
    return ostring

# takes an array and returns it randomized
def shuffle(o):
    random.shuffle(o)
    return o
