import os, sys, re

row_num = 124
row = 'row' + str(row_num)

with open('words.txt', 'r') as f:
    words = f.read().splitlines()

row_files = os.listdir(row)

filters = dict()

from decorators import *
from dbd import *
from sha1filter import *

def run_row(i):
    global words
    print row_files[i]
    with open(os.path.join(row, row_files[i]), 'r') as f:
        rules = f.read().splitlines()
    wordlist = words
    for rule in rules:
        key, value = rule.split(': ')
        print key, value
        if key not in FILTERS:
            continue
        print key, 'in FILTERS'
        wordlist = FILTERS[key](wordlist, value)
        print 'wordlist is now', len(wordlist), 'long'
    print wordlist
