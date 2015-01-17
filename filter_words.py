#!/usr/bin/python
import sys
import argparse
import decorators

import sha1filter
import dbd


def main(row, col, words):
    rule_file = 'row{0}/row{0}_col{1}.txt'.format(row, col)
    with open(rule_file, 'r') as rules:
        filter_words(rules, words)
    for word in words:
        print(word)

def filter_words(rules, words, verbose=False):
    for rule in rules:
        if verbose: print("wordlist_size: {}".format(len(words)))
        (rule_prefix, rule_suffix) = rule.split(': ')
        if rule_prefix in decorators.FILTERS:
            if verbose: print "applying rule: {}".format(rule)
            filter_function = decorators.FILTERS[rule_prefix]
            words, old_words = filter_function(words, rule_suffix), words
        else:
            if verbose: sys.stderr.write("skipping rule: {}\n".format(rule))
    return words

parser = argparse.ArgumentParser(description='Filters a word list')
parser.add_argument('rules', type=argparse.FileType('r'))
parser.add_argument('words', nargs='?', type=argparse.FileType('r'),
                     default=sys.stdin)

if __name__ == "__main__":
    args = parser.parse_args()
    words = args.words.read().splitlines() 
    rules = args.rules.read().splitlines() 
    for word in filter_words(rules, words):
        print word
