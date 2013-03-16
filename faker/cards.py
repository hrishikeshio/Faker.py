from faker import name
from faker import address
from faker import internet
from faker import company
from faker import lorem
from faker import phone_number

def create_card():
    return {
        "name": name.find_name(),
        "username": internet.user_name(),
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



def user_card():
    return {
        "name": name.find_name(),
        "username": internet.user_name(),
        "email": internet.email(),
        "address": {
            "street": address.street_name(),
            "suite": address.secondary_address(),
            "city": address.city(),
            "zipcode": address.zip_code()
        },
        "phone": phone_number.phone_number(),
        "website": internet.domain_name(),
        "company": {
            "name": company.company_name(),
            "catchPhrase": company.catch_phrase(),
            "bs": company.bs()
        }
    }
