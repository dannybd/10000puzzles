from decorators import prefix
import re

def distinct_constants_in_word(word):
	return len(set(filter(lambda x : x in "BCDFGHJKLMNPQRSTVWXYZ", word))))
	
@prefix("Distinct Consonants")
def handle_distinct_consonants(wordlist, rest):
	bounds = re.findall('%d+',rest)
	if len(bounds) == 1:
		bounds = [bounds,bounds]
	return filter(lambda word: bounds[0] <= distinct_constants_in_word(word) <= bounds[1], wordlist)
