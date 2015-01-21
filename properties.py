from decorators import pyramid_property

@pyramid_property('ABUSIR')
def begins_with_ex(word):
	return word.startswith('EX')

@pyramid_property('AMENEMHAT')
def begins_with_un_up(word):
	# todo: just begins with UN?
	return word.startswith('UN') or word.startswith('UP')

@pyramid_property('AMENYQEMAU')
def starts_ends_same_letter(word):
	return word[0] == word[-1]

@pyramid_property('BIKHERIS')
def contains_sh(word):
	return 'SH' in word

@pyramid_property('DJOSER')
def contains_ch(word):
	return 'CH' in word

def to_multiset(things):
	multiset = dict()
	for i in things:
                if i not in multiset:
                        multiset[i] = 0
		multiset[i] += 1
	return dict(multiset)

@pyramid_property('HAWARA')
def contains_three(word):
	multiset = to_multiset(word)
	return 3 in multiset.values()

@pyramid_property('KHUI')
def ends_with_s(word):
	return word.endswith('S')

_vowels = frozenset('AEIOU')

@pyramid_property('LISHT')
def contains_no_vowels(word):
	word_letters = frozenset(word)
	return word_letters == word_letters - _vowels

@pyramid_property('NURI')
def starts_ends_same_two_letters(word):
        return word[:2] == word[-2:]

@pyramid_property('QAKAREIBI')
def starts_with_b(word):
        return word.startswith('B')

@pyramid_property('SETHKA')
def ends_with_ed_or_ing(word):
        return word.endswith('ED') or word.endswith('ING')

@pyramid_property('MEIDUM')
def only_one_type_of_vowel(word):
        return len(set(word).intersection(_vowels)) == 1

@pyramid_property('UNAS')
def contains_all_vowels(word):
        return set(word).issuperset(_vowels)

@pyramid_property('NEFEREFRE')
def only_top_qwerty_row(word):
        return set(word).issubset(set('QWERTYUIOP'))

@pyramid_property('MERENRE')
def alternate_vowels_and_consonants(word):
        zig, zag = set(word[::2]), set(word[1::2])
        vowels, consonants = set('AEIOU'), set('BCDFGHJKLMNPQRSTVWXYZ')
        if zig.intersection(vowels) and zig.intersection(consonants):
                return False
        if zag.intersection(vowels) and zag.intersection(consonants):
                return False
        return zig.intersection(vowels) == zag.intersection(consonants)

@pyramid_property('MENKAURE')
def alphabetical_order(word):
        for i in range(1, len(word)):
                if word[i] < word[i-1]:
                        return False
        return True

@pyramid_property('MAZGHUNA')
def double_letter(word):
        for i in range(1, len(word)):
                if word[i] == word[i-1]:
                        return True
        return False
