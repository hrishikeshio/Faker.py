from faker import frandom
from faker import helper
from faker import name
import random
def suffixes():
    return ["Inc", "and Sons", "LLC", "Group", "and Daughters"]

def company_name(format=None):
    if format:
        r = format
    else:
        r=random.randint(0,2)
        if r==0:
            return name.last_name() + " " + company_suffix()
        if r==1:
            return name.last_name() + "-" + name.last_name()
        else:
            return name.last_name() + ", " + name.last_name() + " and " + name.last_name()
        
def company_suffix():
    return frandom.list_element(suffixes())
    

def catch_phrase():
    return frandom.catch_phrase_adjective() + " " +frandom.catch_phrase_descriptor() + " " +frandom.catch_phrase_noun()
    
def bs():
        return frandom.bs_adjective() + " " + frandom.bs_buzz() + " " + frandom.bs_noun()