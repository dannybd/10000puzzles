#!/usr/bin/env python

from hashlib import sha1
from decorators import prefix

@prefix('SHA-1 hash of lowercased word, expressed in hexadecimal, contains')
def SHA1Contains(words, x):
    x = x.strip().lower()
    return [word for word in words if sha1(word.lower()).hexdigest().find(x) is not -1]

@prefix('SHA-1 hash of lowercased word, expressed in hexadecimal, ends with')
def SHA1EndsWith(words, x):
    x = x.strip().lower()
    return [word for word in words if sha1(word.lower()).hexdigest().endswith(x)]

@prefix('SHA-1 hash of lowercased word, expressed in hexadecimal, starts with')
def SHA1StartsWith(words, x):
    x = x.strip().lower()
    return [word for word in words if sha1(word.lower()).hexdigest().startswith(x)]
