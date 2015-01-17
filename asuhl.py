from decorators import prefix
import re

consonants = "BCDFGHJKLMNPQRSTVWXYZ"
vowels = "AEIOU"
def distinct_constants_in_word(word):
	return len(set(filter(lambda x : x in consonants, word)))
	
def get_bounds_from_regexp(regexp, rest):
	bounds = re.findall(regexp, rest)
	if len(bounds) == 1: bounds = bounds + bounds
	return bounds

@prefix("Distinct Consonants")
def handle_distinct_consonants(wordlist, rest):
	bounds = get_bounds_from_regexp('\d+',rest)
	return filter(lambda word: int(bounds[0]) <= distinct_constants_in_word(word) <= int(bounds[1]), wordlist)


def letters_of_set_in_word(word, letters):
	return len(filter(lambda x: x in letters, word))

def handle_something_with_possible_range(word_to_number_function, wordlist, rest):
	if "%" in rest:
		bounds = get_bounds_from_regexp("\d+\.?\d*",rest)
		# print "Bounds for \"" + rest + "\": " + str(bounds)
		return filter(lambda word : float(bounds[0]) <= word_to_number_function(word) * 100. / len(word) <= float(bounds[1]),   wordlist)
	else:
		bounds = get_bounds_from_regexp("\d+",rest)
		# print "Bounds for \"" + rest + "\": " + str(bounds)
		return filter(lambda word : int(bounds[0]) <= word_to_number_function(word) <= int(bounds[1]),   wordlist)



@prefix("Letters located in the bottom row on a QWERTY keyboard")
def handle_bottom_qwerty(wordlist, rest):
	return handle_something_with_possible_range(lambda word : letters_of_set_in_word(word,"ZXCVBNM"), wordlist, rest)
@prefix("Letters located in the middle row on a QWERTY keyboard")
def handle_middle_qwerty(wordlist, rest):
	return handle_something_with_possible_range(lambda word : letters_of_set_in_word(word,"ASDFGHJKL"), wordlist, rest)
@prefix("Letters located in the top row on a QWERTY keyboard")
def handle_top_qwerty(wordlist, rest):
	return handle_something_with_possible_range(lambda word : letters_of_set_in_word(word,"QWERTYUIOP"), wordlist, rest)

@prefix("Vowels")
def handle_vowels(wordlist, rest):
	return handle_something_with_possible_range(lambda word : letters_of_set_in_word(word,vowels), wordlist, rest)

def mostcommon(word):
	return max([0] + [word.count(letter) for letter in word])

@prefix("Most common consonant(s) each account(s) for")
@prefix("Most common consonant(s) each appear(s)")
def handle_most_common_consonants(wordlist, rest):
	return handle_something_with_possible_range(
		lambda word : mostcommon(filter(lambda x : x in consonants, word)),
		wordlist, rest)

@prefix("Most common vowel(s) each account(s) for")
@prefix("Most common vowel(s) each appear(s)")
def handle_most_common_vowels(wordlist, rest):
	return handle_something_with_possible_range(
		lambda word : mostcommon(filter(lambda x : x in vowels, word)),
		wordlist, rest)
