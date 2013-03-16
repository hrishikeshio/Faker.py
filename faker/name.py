import random as rand
from frandom import first_name_
from frandom import last_name_
from frandom import name_prefix_
from frandom import name_suffix_
def first_name():
	""""""
	return first_name_()

def last_name():
	""""""
	return last_name_()

def find_name():
	""""""
	r = rand.randint(0,10) 
	if r==0:
		return name_prefix_() + " " + first_name() + " " + last_name()
	elif r==1:
		return first_name() + " " + last_name() + " " + name_suffix_()
    
	return first_name() + " " + last_name()
