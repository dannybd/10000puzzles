from decorators import prefix
from ctypes import c_float
from asuhl import handle_something_with_possible_range
import re

@prefix('Contains')
def filter_contains(wordlist, contains):
    return filter(lambda x: contains in x, wordlist)

@prefix('Starts with')
def filter_starts_with(wordlist, value):
    return filter(lambda x: x.startswith(value), wordlist)

@prefix('Ends with')
def filter_ends_with(wordlist, value):
    return filter(lambda x: x.endswith(value), wordlist)

@prefix('Starts with a vowel')
def filter_starts_with_a_vowel(wordlist, value):
    boolean = (value == 'YES')
    return filter(lambda x: (x[0] in 'AEIOU') == boolean, wordlist)

def scrabble_score(word):
    letter_score = {
        'A': 1, 'B': 3, 'C': 3,  'D': 2, 'E': 1, 'F': 4, 'G': 2,
        'H': 4, 'I': 1, 'J': 8,  'K': 5, 'L': 1, 'M': 3, 'N': 1,
        'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
        'V': 4, 'W': 4, 'X': 8,  'Y': 4, 'Z': 10,
    }
    return sum(letter_score[c] for c in word)

@prefix('Base Scrabble score')
def filter_by_scrabble_score(wordlist, value):
    return handle_something_with_possible_range(scrabble_score, wordlist, value)

@prefix('Ends with')
def filter_ends_with(wordlist, value):
    return filter(lambda x: x.endswith(value), wordlist)

@prefix('Length')
def filter_length(wordlist, value):
    return handle_something_with_possible_range(len, wordlist, value)

def letter_sum(word):
    return sum([ord(c) - ord('A') + 1 for c in word])

@prefix('Sum of letters (A=1, B=2, etc)')
def filter_sum_of_letters(wordlist, value):
    return handle_something_with_possible_range(letter_sum, wordlist, value)

def filter_sum_of_letters_divisible_by_n(wordlist, value, n):
    boolean = (value == 'YES')
    return filter(lambda x: (letter_sum(x) % n == 0) == boolean, wordlist)

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
    return filter(lambda x: (base_26(x) % n == 0) == boolean, wordlist)

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
def filter_uint32(wordlist, value):
    boolean = (value == 'YES')
    test = lambda x: 0 <= x <= 2**32-1
    return filter(lambda x: test(base_26(x)) == boolean, wordlist)

@prefix('Word interpreted as a base 26 number (A=0, B=1, etc) is representable as an unsigned 64-bit integer')
def filter_uint64(wordlist, value):
    boolean = (value == 'YES')
    test = lambda x: 0 <= x <= 2**64-1
    return filter(lambda x: test(base_26(x)) == boolean, wordlist)
