from decorators import prefix
import re

def distinct_constants_in_word(word):
	return len(set(filter(lambda x : x in "BCDFGHJKLMNPQRSTVWXYZ", word)))
	
def get_bounds_from_regexp(rest, regexp):
	bounds = re.findall(regexp, rest)
	if len(bounds) == 1: bounds = bounds + bounds
	return bounds

@prefix("Distinct Consonants")
def handle_distinct_consonants(wordlist, rest):
	bounds = get_bounds_from_regexp('\d+',rest)
	return filter(lambda word: int(bounds[0]) <= distinct_constants_in_word(word) <= int(bounds[1]), wordlist)


def letters_of_set_in_word(word, letters):
	return len(filter(lambda x: x in letters, word))

@prefix("Letters located in the bottom row on a QWERTY keyboard")
def handle_bottom_qwerty(wordlist, rest):
	if re.match("\d+", rest): # Exact number
		return filter(lambda word : letters_of_set_in_word(word, "ZXCVBNM") == int(rest), wordlist)
	if "%" in rest:
		bounds = get_bounds_from_regexp("\d+\.?\d*%",rest)
		print bounds
	else:
		bounds = get_bounds_from_regexp("\d+",rest)
		print bounds

wordlist = ["zzz","qwertyuioz","zzzzzz"]
print handle_bottom_qwerty(wordlist,"3") #zzz
print handle_bottom_qwerty(wordlist,"exactly 10% of the letters") #qwertyuioz
print handle_bottom_qwerty(wordlist,"between 5 and 6 of the letters") #
print handle_bottom_qwerty(wordlist,"exactly 1 of the letters")
print handle_bottom_qwerty(wordlist,"between 20.1% and 30.1% of the letters")

		
