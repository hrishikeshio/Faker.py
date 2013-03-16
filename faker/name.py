from faker import frandom
from faker import helper
import random
def first_name():
	""""""
	return frandom.first_name()

def last_name():
	""""""
	return frandom.last_name()

def find_name():
	""""""
	r = random.randint(0,10) 
	if r==0:
		return frandom.name_prefix() + " " + first_name() + " " + last_name()
	elif r==1:
		return first_name() + " " + last_name() + " " + frandom.name_suffix()
    
	return first_name() + " " + last_name()
