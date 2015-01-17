import os, sys

row_num = 124
row = 'row' + str(row_num)

with open('words.txt', 'r') as f:
    words = f.read().splitlines()

row_files = os.listdir(row)

with open(os.path.join(row, row_files[0]), 'r') as f:
    cell = f.read().splitlines()

def filter_contains(wordlist, contains):
    return filter(lambda x: contains in x, wordlist)

word_scrabbles = dict()
letter_score = {'A': 1, 'C': 3, 'B': 3, 'E': 1, 'D': 2, 'G': 2, 'F': 4, 'I': 1, 'H': 4, 'K': 5, 'J': 8, 'M': 3, 'L': 1, 'O': 1, 'N': 1, 'Q': 10, 'P': 3, 'S': 1, 'R': 1, 'U': 1, 'T': 1, 'W': 4, 'V': 4, 'Y': 4, 'X': 8, 'Z': 10}
for word in words:
    word_scrabbles[word] = sum(letter_score[c] for c in word)
def filter_by_scrabble_score(wordlist, score):
    global word_scrabbles
    score = [int(i) for i in re.findall('\d+\.?\d+?', score)]
    if len(score) == 1:
        return filter(lambda x: word_scrabbles[x] == score[0], wordlist)
    return filter(lambda x: score[0] <= word_scrabbles[x] <= score[1], wordlist)

    
    

filters = {
    'Contains': 
}
