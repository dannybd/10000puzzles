import os, sys, re

with open('words.txt', 'r') as f:
    words = f.read().splitlines()

row_num = 124
row = 'row' + str(row_num)

row_files = os.listdir(row)

filters = dict()

from decorators import *
from dbd import *
from asuhl import *
from sha1filter import *

def run_row(i, verbose=False):
    global words
    if verbose:
        print row_files[i]
    with open(os.path.join(row, row_files[i]), 'r') as f:
        rules = f.read().splitlines()
    wordlist = words
    for rule in rules:
        key, value = rule.split(': ')
        if verbose:
            print key, value
        if key not in FILTERS:
            continue
        if verbose:
            print key, 'in FILTERS'
        wordlist = FILTERS[key](wordlist, value)
        if verbose:
            print 'wordlist is now', len(wordlist), 'long'
    if verbose:
        print wordlist

def check_rule(wordlist, rule):
    if ': ' not in rule:
        return wordlist
    key, value = rule.split(': ')
    print rule
    if key not in FILTERS:
        return wordlist
    print 'in FILTERS', FILTERS[key].__name__
    wordlist = FILTERS[key](wordlist, value)
    print 'wordlist is now', len(wordlist), 'long'
    return wordlist

examples = filter(lambda x: x.startswith('normal'), os.listdir('examples'))

def check_example(i):
    print examples[i]
    with open(os.path.join('examples', examples[i]), 'r') as f:
        rules = f.read().splitlines()
    global words
    wordlist = words
    for rule in rules:
        print rule
        wordlist = check_rule(wordlist, rule)
    print wordlist
