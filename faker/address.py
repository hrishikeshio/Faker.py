from faker import frandom
from faker import helper
import random

def zip_code():
	return helper.replace_symbol_with_number(frandom.array_element(["#####", '#####-####']))

def zip_code_format(format):
	return helper.replace_symbol_with_number(["#####", '#####-####'],format)

def city():
	r = random.randint(0,4)
	if r == 0:
		return frandom.city_prefix() + " " + frandom.first_name() + frandom.city_suffix()
	elif r==1:
		return frandom.city_prefix() + " " + frandom.first_name()
	elif r==2:
		return frandom.first_name() + frandom.city_suffix()
	else:
		return frandom.last_name() + frandom.city_suffix()

def street_name():
	r = random.randint(0,2)
	if r == 0:
		return frandom.last_name() + " " + frandom.street_suffix()
	else:
		return frandom.first_name() + " " + frandom.street_suffix()
        
def street_address(use_full_address=False):
	address = ""
	r = random.randint(0,3)
	if r==0:
		address = helper.replace_symbol_with_number("#####") + " " + street_name()
	elif r==1:
		address = helper.replace_symbol_with_number("####") +  " " + street_name()
	else:
		address = helper.replace_symbol_with_number("###") + " " + street_name()
	if use_full_address:
		return address + " " + secondary_address()
	else:
		return address

def secondary_address():
	return helper.replace_symbol_with_number(frandom.array_element(['Apt. ###','Suite ###']))

def br_state(use_abbr=False):
	if use_abbr:
		return frandom.br_state_abbr() 
	else:
		return frandom.br_state()

def uk_county():
	return frandom.uk_county()

def uk_country():
	return frandom.uk_country()
    
def us_state(use_abbr=False):
	if use_abbr:
		frandom.us_state_abbr()
	else:
		frandom.us_state()
    