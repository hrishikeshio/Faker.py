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

def create_card():
    return {
        "name": name.find_name(),
        "username": internet.username(),
        "email": internet.email(),
        "address": {
            "streetA": address.street_name(),
            "streetB": address.street_address(),
            "streetC": address.street_address(True),
            "streetD": address.secondary_address(),
            "city": address.city(),
            "ukCounty": address.uk_county(),
            "ukCountry": address.uk_country(),
            "zipcode": address.zip_code()
        },
        "phone": phone_number.phone_number(),
        "website": internet.domain_name(),
        "company": {
            "name": company.company_name(),
            "catchPhrase": company.catch_phrase(),
            "bs": company.bs()
        },
        "posts": [
            {
                "words": lorem.words(),
                "sentence": lorem.sentence(),
                "sentences": lorem.sentences(),
                "paragraph": lorem.paragraph()
            },
            {
                "words": lorem.words(),
                "sentence": lorem.sentence(),
                "sentences": lorem.sentences(),
                "paragraph": lorem.paragraph()
            },
            {
                "words": lorem.words(),
                "sentence": lorem.sentence(),
                "sentences": lorem.sentences(),
                "paragraph": lorem.paragraph()
            }
        ]
    }



def userCard():
    return {
        "name": name.find_name(),
        "username": internet.username(),
        "email": internet.email(),
        "address": {
            "street": address.street_name(true),
            "suite": address.secondary_address(),
            "city": address.city(),
            "zipcode": address.zip_code()
        },
        "phone": PhoneNumber.phone_number(),
        "website": internet.domain_name(),
        "company": {
            "name": company.company_name(),
            "catchPhrase": company.catch_phrase(),
            "bs": company.bs()
        }
    }
