from faker import frandom
from faker import helper
import random
def email():
        return helper.slugify(user_name()) + "@" + helper.slugify(domain_name())
    

def user_name():
    r=random.randint(0,1)
    if r == 0:
        result = frandom.first_name()    
    else:
        result = frandom.first_name() + frandom.list_element([".", "_"]) + frandom.last_name()
    return result
    

def domain_name():
    return domain_word() + "." + frandom.domain_suffix()
    

def domain_word():
    return frandom.first_name().lower()
    

def ip():
    result = []
    for i in range(4):
        result.append(str(random.randint(0,255)))
    return (".").join(result)