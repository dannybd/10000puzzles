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
from marked import *

def run_row(i):
    global words
    with open(os.path.join(row, row + '_col' + str(i) + '.txt'), 'r') as f:
        rules = f.read().splitlines()
    wordlist = words
    deferred_rules = []
    for rule in rules:
        if ': ' not in rule:
            continue
        if 'overlap' in rule:
            deferred_rules.append(rule)
            continue
        key, value = rule.split(': ')
        key = key.lower()
        if key not in FILTERS:
            continue
        wordlist = FILTERS[key](wordlist, value)
    for rule in deferred_rules:
        key, value = rule.split(': ')
        key = key.lower()
        if key not in FILTERS:
            continue
        wordlist = FILTERS[key](wordlist, value)
    return wordlist

def check_rule(wordlist, rule):
    if ': ' not in rule:
        return wordlist
    key, value = rule.split(': ')
    key = key.lower()
    #print rule
    if key not in FILTERS:
        global failures
        if key not in failures:
            failures['skipped: '+key] = 0
        failures['skipped: '+key] += 1
        return wordlist
    #print 'Found key in FILTERS: calling function', FILTERS[key].__name__
    wordlist = FILTERS[key](wordlist, value)
    #print 'wordlist is now', len(wordlist), 'long'
    return wordlist

examples = filter(lambda x: x.startswith('normal'), os.listdir('examples'))
failures = dict()
answers = dict()
def check_example(i):
    print examples[i]
    with open(os.path.join('examples', examples[i]), 'r') as f:
        rules = f.read().splitlines()
    correct = re.findall('[A-Z]{2,}(?=:)', rules[0])[0]
    global words
    wordlist = words
    deferred_rules = []
    for rule in rules:
        if 'overlap' in rule:
            deferred_rules.append(rule)
            continue
        #print rule
        wordlist = check_rule(wordlist, rule)
        if correct not in wordlist:
            print 'FAIL: word', correct, 'not found!'
            key = rule.split(': ')[0]
            bad_func = FILTERS[key].__name__
            print '~~~', bad_func, 'is the culprit'
            global failures
            if bad_func not in failures:
                failures[bad_func] = 0
            failures[bad_func] += 1
            return
    for rule in deferred_rules:
        #print rule
        wordlist = check_rule(wordlist, rule)
        if correct not in wordlist:
            print 'FAIL: word', correct, 'not found!', rule
            key = rule.split(': ')[0]
            print key in FILTERS
            bad_func = FILTERS[key].__name__
            print bad_func
            print '~~~', bad_func, 'is the culprit'
            global failures
            if bad_func not in failures:
                failures[bad_func] = 0
            failures[bad_func] += 1
            return
    print len(wordlist)
    #print wordlist
    #print
    #print 'PASS:', correct, 'found in wordlist!'
    #print

def check_all_examples():
    global failures
    failures = dict()
    for i in range(len(examples)):
        try:
            check_example(i)
        except Exception, e:
            print e
    print
    print
    for k in failures.keys():
        print k, '\t\t', failures[k]


