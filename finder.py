import os, sys, re

with open('words.txt', 'r') as f:
    words = f.read().splitlines()

row_num = 124
row = 'row' + str(row_num)

row_files = os.listdir(row)

filters = dict()
failures = dict()
answers = dict()

from decorators import *
from dbd import *
from asuhl import *
from sha1filter import *
from marked import *

ABUSIR = [(10, 72), (100, 60), (100, 87), (102, 16), (102, 26), (109, 42), (111, 23), (115, 13), (115, 40), (123, 89), (20, 62), (20, 84), (20, 87), (29, 75), (38, 79)]
AMENEMHAT = [(10, 63), (105, 68), (106, 58), (108, 61), (108, 68), (11, 76), (110, 47), (115, 106), (115, 98), (117, 105), (117, 67), (119, 70), (13, 57), (15, 75), (18, 80), (20, 69), (20, 81), (20, 83), (23, 52), (24, 66), (29, 82), (34, 72), (37, 46), (43, 65), (5, 67), (5, 74), (50, 64)]
AMENYQEMAU = [(100, 26), (101, 51), (102, 106), (102, 114), (102, 44), (103, 54), (103, 56), (103, 93), (104, 97), (105, 21), (105, 47), (105, 73), (106, 127), (108, 48), (108, 55), (109, 50), (109, 52), (110, 106), (111, 110), (111, 13), (113, 131), (113, 80), (114, 134), (114, 26), (114, 52), (114, 8), (114, 81), (115, 103), (115, 129), (115, 51), (115, 67), (116, 46), (117, 111), (117, 98), (119, 136), (120, 108), (120, 129), (121, 25), (121, 72), (122, 24), (122, 41), (122, 62), (122, 7), (122, 91), (123, 81), (124, 21), (124, 30), (14, 84), (29, 52), (33, 55), (35, 48), (37, 77), (39, 53), (4, 76), (41, 54), (42, 76), (45, 43), (48, 52), (49, 87)]
BIKHERIS = [(0, 71), (100, 18), (101, 105), (104, 126), (106, 103), (106, 12), (111, 16), (112, 107), (120, 131), (120, 45), (121, 124), (121, 19), (123, 9), (17, 60), (19, 84), (2, 67), (23, 54), (3, 78), (38, 87), (39, 62), (40, 53), (41, 79), (42, 76), (42, 92), (45, 81)]
DJOSER = [(102, 32), (103, 20), (105, 15), (105, 22), (105, 28), (107, 25), (108, 12), (109, 18), (109, 23), (109, 27), (113, 34), (114, 111), (114, 134), (114, 29), (116, 16), (116, 8), (118, 15), (118, 9), (119, 131), (119, 25), (120, 21), (121, 125), (123, 125), (123, 128), (123, 15), (123, 18), (123, 2), (124, 136), (28, 51), (32, 51), (39, 96), (40, 47), (40, 58), (40, 68), (42, 98), (44, 46), (44, 91), (44, 97), (46, 43), (47, 95), (49, 39)]
HAWARA = [(102, 55), (104, 110), (104, 93), (106, 103), (106, 57), (11, 64), (11, 73), (111, 21), (111, 35), (111, 92), (112, 58), (114, 63), (114, 78), (115, 112), (119, 63), (120, 51), (120, 80), (121, 52), (123, 38), (123, 66), (15, 70), (16, 85), (20, 78), (21, 75), (29, 88), (30, 77), (34, 51), (35, 82), (36, 65), (41, 77), (45, 56), (46, 82), (5, 72), (50, 59), (50, 86)]
KHUI = [(1, 67), (100, 102), (100, 35), (100, 52), (100, 71), (101, 110), (101, 121), (101, 42), (101, 48), (101, 52), (101, 74), (102, 113), (102, 55), (102, 65), (102, 70), (103, 117), (103, 119), (103, 39), (103, 44), (103, 63), (104, 100), (104, 103), (104, 110), (104, 114), (104, 122), (104, 38), (104, 44), (104, 46), (104, 89), (105, 60), (105, 88), (106, 106), (106, 119), (106, 122), (106, 37), (106, 67), (106, 75), (107, 102), (107, 108), (107, 46), (107, 70), (107, 72), (107, 76), (108, 104), (108, 105), (108, 110), (108, 96), (108, 97), (108, 98), (109, 35), (109, 56), (109, 95), (11, 71), (110, 100), (110, 102), (110, 32), (110, 47), (110, 51), (110, 63), (110, 89), (111, 115), (111, 120), (111, 122), (111, 34), (111, 77), (111, 79), (111, 96), (112, 103), (112, 34), (113, 106), (113, 112), (113, 116), (113, 36), (113, 51), (114, 42), (114, 90), (114, 93), (115, 106), (115, 117), (115, 46), (115, 88), (115, 96), (115, 98), (116, 124), (118, 81), (119, 106), (119, 118), (119, 30), (119, 37), (119, 62), (119, 70), (119, 75), (12, 73), (120, 29), (120, 45), (120, 66), (120, 80), (121, 27), (121, 29), (121, 41), (121, 52), (121, 60), (121, 71), (122, 105), (122, 84), (123, 104), (123, 39), (123, 54), (123, 59), (123, 87), (123, 92), (123, 94), (123, 95), (124, 110), (124, 123), (14, 82), (18, 63), (18, 76), (18, 84), (23, 53), (25, 56), (29, 87), (33, 53), (36, 93), (4, 72), (40, 66), (41, 93), (43, 52), (43, 75), (44, 51), (44, 94), (44, 97), (45, 53), (45, 58), (45, 90), (46, 70), (46, 72), (47, 55), (48, 53), (48, 81), (50, 58)]
LISHT = [(100, 37), (101, 120), (108, 67), (111, 44), (117, 111), (41, 72), (42, 65), (46, 49)]
MAZGHUNA = [(100, 102), (100, 121), (100, 35), (100, 41), (100, 75), (101, 32), (101, 87), (102, 63), (103, 20), (103, 37), (103, 71), (104, 69), (104, 78), (104, 83), (105, 48), (105, 76), (105, 82), (106, 75), (106, 91), (107, 111), (107, 45), (107, 47), (107, 74), (107, 85), (107, 87), (108, 50), (108, 61), (108, 83), (109, 105), (109, 58), (11, 58), (110, 104), (111, 119), (111, 22), (111, 35), (111, 51), (111, 54), (112, 103), (112, 67), (113, 119), (113, 35), (114, 103), (114, 42), (114, 48), (114, 52), (115, 111), (115, 116), (115, 75), (116, 80), (119, 29), (119, 78), (121, 49), (122, 75), (122, 91), (123, 128), (123, 69), (124, 136), (22, 61), (22, 78), (24, 73), (24, 83), (25, 56), (25, 80), (26, 52), (26, 79), (26, 84), (26, 87), (26, 88), (27, 52), (27, 65), (27, 86), (27, 90), (28, 71), (29, 62), (29, 86), (30, 59), (31, 56), (31, 59), (32, 71), (32, 73), (34, 85), (35, 76), (35, 81), (36, 73), (36, 83), (37, 59), (38, 58), (38, 91), (40, 49), (41, 86), (43, 83), (45, 66), (46, 66), (46, 82), (48, 69), (49, 65)]
MEIDUM = [(100, 102), (101, 116), (102, 17), (103, 111), (105, 17), (105, 31), (106, 23), (106, 50), (107, 69), (107, 70), (109, 30), (109, 40), (111, 22), (112, 129), (112, 97), (113, 110), (115, 107), (115, 129), (116, 130), (117, 124), (117, 134), (117, 18), (119, 28), (119, 45), (119, 72), (120, 20), (120, 29), (122, 135), (122, 5), (122, 58), (122, 76), (123, 126), (123, 16), (123, 22), (123, 7), (21, 73), (28, 71), (31, 60), (35, 67), (37, 46), (40, 44), (42, 86)]
MENKAURE = [(100, 37), (104, 79), (105, 103), (105, 93), (107, 39), (108, 51), (108, 91), (114, 9), (117, 111), (117, 18), (120, 26), (40, 93)]
MERENRE = [(100, 49), (100, 66), (101, 108), (101, 34), (101, 51), (101, 64), (102, 117), (102, 34), (103, 45), (103, 85), (104, 42), (104, 63), (104, 72), (104, 75), (105, 112), (105, 37), (105, 73), (105, 84), (106, 44), (106, 72), (108, 56), (108, 58), (109, 41), (109, 56), (110, 117), (110, 62), (110, 65), (111, 122), (111, 56), (111, 69), (112, 54), (114, 104), (114, 113), (114, 122), (114, 38), (115, 121), (115, 48), (120, 115), (120, 34), (120, 62), (121, 37), (122, 38), (122, 54), (122, 58), (123, 108), (123, 121), (123, 90), (124, 118), (124, 125), (36, 50), (43, 73), (43, 77), (44, 68), (46, 77), (46, 90), (47, 91), (48, 58)]
NEFEREFRE = [(102, 120), (114, 99), (117, 102), (117, 103), (117, 104), (117, 106), (117, 111), (117, 112), (117, 113), (117, 114), (117, 118), (117, 121), (117, 34), (117, 35), (117, 36), (117, 41), (117, 42), (117, 48), (117, 50), (117, 57), (117, 58), (117, 64), (117, 65), (117, 66), (117, 68), (117, 72), (117, 74), (117, 88), (117, 90), (123, 124)]
NURI = [(107, 39), (113, 67), (117, 111), (117, 56), (117, 59), (117, 73), (117, 76), (117, 89), (36, 92), (40, 93), (50, 96)]
PEPI = [(0, 69), (1, 73), (100, 16), (101, 49), (105, 15), (105, 18), (107, 74), (108, 33), (109, 18), (110, 26), (110, 90), (111, 119), (111, 62), (113, 103), (113, 131), (113, 70), (113, 92), (114, 19), (114, 74), (115, 34), (116, 23), (118, 70), (119, 105), (119, 99), (12, 64), (121, 71), (122, 106), (122, 123), (122, 49), (124, 27), (124, 3), (15, 73), (17, 59), (2, 72), (20, 75), (21, 80), (25, 52), (25, 83), (28, 66), (28, 72), (29, 64), (31, 89), (33, 64), (35, 48), (35, 62), (39, 70), (39, 75), (46, 66), (49, 67), (5, 70), (50, 60), (50, 61), (50, 86)]
QAKAREIBI = [(101, 122), (101, 82), (102, 127), (102, 14), (102, 86), (103, 31), (103, 98), (104, 71), (106, 53), (106, 89), (107, 83), (109, 130), (109, 27), (109, 36), (110, 28), (110, 36), (111, 123), (112, 86), (112, 92), (113, 20), (114, 22), (114, 85), (115, 23), (115, 28), (119, 116), (119, 27), (12, 83), (120, 114), (120, 21), (121, 41), (121, 60), (121, 64), (122, 105), (122, 38), (122, 4), (122, 75), (123, 116), (124, 3), (15, 73), (21, 77), (24, 77), (28, 57), (29, 73), (29, 84), (30, 63), (30, 69), (31, 90), (34, 58), (35, 84), (39, 55), (48, 43), (50, 86)]
SETHKA = [(100, 123), (100, 85), (101, 59), (101, 75), (103, 61), (104, 84), (105, 89), (106, 104), (106, 83), (107, 64), (108, 108), (108, 59), (108, 78), (109, 19), (109, 21), (109, 86), (110, 81), (111, 11), (111, 17), (111, 75), (112, 60), (113, 34), (113, 39), (113, 65), (114, 21), (115, 131), (115, 58), (115, 60), (119, 76), (120, 69), (121, 62), (122, 115), (123, 118), (123, 121), (124, 119), (15, 63), (20, 78), (22, 69), (23, 62), (23, 68), (23, 88), (24, 73), (24, 76), (24, 78), (25, 58), (25, 64), (25, 68), (25, 80), (26, 67), (26, 88), (28, 62), (29, 60), (30, 59), (30, 66), (31, 66), (31, 85), (32, 66), (32, 86), (33, 59), (33, 60), (33, 71), (34, 85), (35, 69), (35, 75), (35, 80), (35, 82), (36, 89), (37, 81), (38, 55), (38, 59), (38, 72), (38, 77), (38, 81), (38, 90), (39, 59), (39, 60), (39, 90), (40, 77), (40, 81), (41, 96), (43, 81), (44, 68), (44, 82), (46, 42), (46, 75), (48, 40), (48, 62), (48, 76), (49, 60), (49, 70), (49, 86), (49, 99), (50, 40), (50, 72)]
SOBEKNEFERU = [(1, 76), (10, 60), (108, 74), (11, 65), (111, 56), (114, 120), (12, 63), (12, 80), (123, 82), (14, 78), (16, 69), (17, 68), (17, 73), (18, 62), (18, 63), (18, 64), (18, 76), (19, 72), (20, 79), (21, 63), (22, 54), (23, 53), (23, 57), (4, 68), (48, 58), (5, 63)]
UNAS = [(10, 80), (12, 82), (13, 61), (14, 57), (14, 80), (15, 56), (15, 63), (15, 74), (15, 82), (16, 61), (16, 79), (17, 84), (18, 67), (18, 83), (19, 64), (2, 75), (20, 59), (22, 58), (5, 72)]

def testname(foo):
    test = []
    for n in foo:
        temp = check_cell(*n)
        if len(temp) != 1:
            continue
        test.append(temp[0])
    for x in test:
        print x

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

def check_cell(row, col):
    global words
    with open(os.path.join('row'+str(row), 'row'+str(row)+'_col'+str(col)+'.txt'), 'r') as f:
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


