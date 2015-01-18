from decorators import pyramid_property

@pyramid_property('ABUSIR')
def begins_with_ex(word):
	return word.starts_with('EX')

@pyramid_property('AMENEMHAT')
def begins_with_un_up(word):
	# todo: just begins with UN?
	return words.starts_with('UN') or words.starts_with('UP')

@pyramid_property('AMENYQEMAU')
def starts_ends_same_letter(word):
	return word[0] == word[1]

@pyramid_property('BIKHERIS')
def countains_sh(word):
	return 'SH' in word

@pyramid_property('DJOSER')
def contains_sh(word):
	return 'CH' in word

def to_multiset(things):
	multiset = dict(lambda:0)
	for i in things:
		multiset[i] += 1
	return dict(multiset)

@pyramid_property('HAWARA')
def contains_three(word):
	multiset = to_multiset(word)
	return 3 in multiset.values()

@pyramid_property('KHUI')
def ends_with_s(word):
	return word[-1] == s

_vowels = frozenset('AEIOU')

@pyramid_property('LISHT')
def contains_no_vowels(word):
	word_letters = frozenset(word)
	return word_letters == word_letters - _vowels
