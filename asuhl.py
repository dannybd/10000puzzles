from decorators import prefix
import re

consonants = "BCDFGHJKLMNPQRSTVWXYZ"
vowels = "AEIOU"
letters = consonants + vowels

# Precompute anagramset
with open('words.txt', 'r') as f:
	fullwordlist = f.read().splitlines()
sortedwordlist = ["".join(sorted(word)) for word in fullwordlist]
freqdict = {}
for sw in sortedwordlist:
	if sw in freqdict: freqdict[sw] += 1
	else: freqdict[sw] = 1
sortedwordlist = set(sortedwordlist)
anagramset = set([sw for sw in freqdict.keys() if freqdict[sw] > 1])


def distinct_consonants_in_word(word):
	return len(set(filter(lambda x : x in consonants, word)))
def distinct_vowels_in_word(word):
	return len(set(filter(lambda x : x in vowels, word)))
	
def get_bounds_from_regexp(regexp, rest):
	bounds = re.findall(regexp, rest)
	if len(bounds) == 1: bounds = bounds + bounds
	return bounds

@prefix("Distinct consonants")
def handle_distinct_consonants(wordlist, rest):
	bounds = get_bounds_from_regexp('\d+',rest)
	return filter(lambda word: int(bounds[0]) <= distinct_consonants_in_word(word) <= int(bounds[1]), wordlist)

@prefix("Distinct vowels")
def handle_distinct_vowels(wordlist, rest):
	bounds = get_bounds_from_regexp('\d+',rest)
	return filter(lambda word: int(bounds[0]) <= distinct_vowels_in_word(word) <= int(bounds[1]), wordlist)

@prefix("Distinct letters")
def handle_distinct_letters(wordlist, rest):
	bounds = get_bounds_from_regexp('\d+',rest)
	return filter(lambda word: int(bounds[0]) <= len(set(word)) <= int(bounds[1]), wordlist)

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

@prefix("Most common letter(s) each account(s) for")
@prefix("Most common letter(s) each appear(s)")
def handle_most_common_letters(wordlist, rest):
	return handle_something_with_possible_range(
		mostcommon,
		wordlist, rest)

@prefix("Contains at least one doubled letter")
def handle_doubled_letter(wordlist, rest):
	def has_doubled_letter(word):
		return re.search("(.)\\1", word) != None
	return filter(lambda word : (rest == "YES") == (has_doubled_letter(word)), wordlist)

@prefix("Has at least one anagram that is also in the word list")
def handle_has_anagram(wordlist, rest):
	return filter(lambda word: (rest == "YES") == ("".join(sorted(word)) in anagramset), wordlist)

@prefix("Can be combined with one additional letter to produce an anagram of something in the word list")
def handle_plus_one_letter_has_anagram(wordlist, rest):
	def test(word, memo={}):
		if word in memo: return memo[word]
		for l in letters:
			if ''.join(sorted(word+l)) in sortedwordlist:
				memo[word] = True
				return memo[word]
		memo[word] = False
		return memo[word]
	return filter(lambda word: (rest == "YES") == test(word), wordlist)

@prefix("Can be combined with two additional letters to produce an anagram of something in the word list")
def handle_plus_two_letter_has_anagram(wordlist, rest):
	def test(word,memo={}):
		if word in memo: return memo[word]
		for l1 in letters:
			for l2 in letters[letters.find(l1):]:
				if ''.join(sorted(word+l1+l2)) in sortedwordlist:
					memo[word] = True
					return memo[word]
		memo[word] = False
		return memo[word]
	return filter(lambda word: (rest == "YES") == test(word), wordlist)
