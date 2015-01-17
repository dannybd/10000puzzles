from ctypes import c_float, c_uint

@prefix('Contains')
def filter_contains(wordlist, contains):
    return filter(lambda x: contains in x, wordlist)

@prefix('Base Scrabble score')
def filter_by_scrabble_score(wordlist, value):
    global words
    word_scrabbles = dict()
    letter_score = {'A': 1, 'C': 3, 'B': 3, 'E': 1, 'D': 2, 'G': 2, 'F': 4, 'I': 1, 'H': 4, 'K': 5, 'J': 8, 'M': 3, 'L': 1, 'O': 1, 'N': 1, 'Q': 10, 'P': 3, 'S': 1, 'R': 1, 'U': 1, 'T': 1, 'W': 4, 'V': 4, 'Y': 4, 'X': 8, 'Z': 10}
    for word in words:
        word_scrabbles[word] = sum(letter_score[c] for c in word)
    value = [int(i) for i in re.findall('\d+\.?\d+?', value)]
    if len(value) == 1:
        value = [value[0], value[0]]
    return filter(lambda x: value[0] <= word_scrabbles[x] <= value[1], wordlist)

@prefix('Ends with')
def filter_ends_with(wordlist, value):
    return filter(lambda x: x.endswith(value), wordlist)

@prefix('Length')
def filter_length(wordlist, value):
    value = [int(i) for i in re.findall('\d+\.?\d+?', value)]
    if len(value) == 1:
        value = [value[0], value[0]]
    return filter(lambda x: value[0] <= len(x) <= value[1], wordlist)

def letter_sum(word):
    total = 0
    for c in word:
	total += ord(c) - ord('A') + 1
    return total

@prefix('Sum of letters (A=1, B=2, etc)')
def filter_sum_of_letters(wordlist, value):
    value = [int(i) for i in re.findall('\d+\.?\d+?', value)]
    if len(value) == 1:
        value = [value[0], value[0]]
    return filter(lambda x: value[0] <= letter_sum(x) <= value[1], wordlist)

def filter_sum_of_letters_divisible_by_n(wordlist, value, n):
    boolean = (value == 'YES')
    return filter(lambda x: (letter_sum(x) % n != 0) == boolean, wordlist)

@prefix('Sum of letters (A=1, B=2, etc) is divisible by 2')
def filter_sum_of_letters_divisible_by_2(wordlist, value):
    return filter_sum_of_letters_divisible_by_n(wordlist, value, 2)

@prefix('Sum of letters (A=1, B=2, etc) is divisible by 3')
def filter_sum_of_letters_divisible_by_3(wordlist, value):
    return filter_sum_of_letters_divisible_by_n(wordlist, value, 3)

@prefix('Sum of letters (A=1, B=2, etc) is divisible by 5')
def filter_sum_of_letters_divisible_by_5(wordlist, value):
    return filter_sum_of_letters_divisible_by_n(wordlist, value, 5)

@prefix('Sum of letters (A=1, B=2, etc) is divisible by 7')
def filter_sum_of_letters_divisible_by_7(wordlist, value):
    return filter_sum_of_letters_divisible_by_n(wordlist, value, 7)

def base_26(word):
    val = 0
    for c in word:
        val *= 26
        val += ord(c) - ord('A')
    return val

def filter_base_26_divisible_by_n(wordlist, value, n):
    boolean = (value == 'YES')
    return filter(lambda x: (base_26(x) % n != 0) == boolean, wordlist)

@prefix('Word interpreted as a base 26 number (A=0, B=1, etc) is divisible by 2')
def filter_base_26_divisible_by_2(wordlist, value):
    return filter_base_26_divisible_by_n(wordlist, value, 2)

@prefix('Word interpreted as a base 26 number (A=0, B=1, etc) is divisible by 3')
def filter_base_26_divisible_by_3(wordlist, value):
    return filter_base_26_divisible_by_n(wordlist, value, 3)

@prefix('Word interpreted as a base 26 number (A=0, B=1, etc) is divisible by 5')
def filter_base_26_divisible_by_5(wordlist, value):
    return filter_base_26_divisible_by_n(wordlist, value, 5)

@prefix('Word interpreted as a base 26 number (A=0, B=1, etc) is divisible by 7')
def filter_base_26_divisible_by_7(wordlist, value):
    return filter_base_26_divisible_by_n(wordlist, value, 7)

@prefix('Word interpreted as a base 26 number (A=0, B=1, etc) is exactly representable in IEEE 754 double-precision floating point format')
def filter_double_exact(wordlist, value):
    boolean = (value == 'YES')
    test = lambda x: x == float(x)
    return filter(lambda x: test(base_26(x)) == boolean, wordlist)

@prefix('Word interpreted as a base 26 number (A=0, B=1, etc) is exactly representable in IEEE 754 single-precision floating point format')
def filter_single_exact(wordlist, value):
    boolean = (value == 'YES')
    test = lambda x: x == c_float(x).value
    return filter(lambda x: test(base_26(x)) == boolean, wordlist)

@prefix('Word interpreted as a base 26 number (A=0, B=1, etc) is representable as an unsigned 32-bit integer')
def filter_single_exact(wordlist, value):
    boolean = (value == 'YES')
    test = lambda x: x == c_uint(x).value
    return filter(lambda x: test(base_26(x)) == boolean, wordlist)
