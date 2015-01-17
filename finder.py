import os, sys, re

row_num = 124
row = 'row' + str(row_num)

with open('words.txt', 'r') as f:
    words = f.read().splitlines()

row_files = os.listdir(row)

with open(os.path.join(row, row_files[0]), 'r') as f:
    cell = f.read().splitlines()

filters = dict()

from dbd import *
from sha1filter import *
