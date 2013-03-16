
def phone_number():
	return helper.replace_symbol_with_number(frandom.phone_formats())

def phone_number_format(phone_formats_array_index):
	return helpers.replace_symbol_with_number(definitions.phone_formats()[phone_formats_array_index])
