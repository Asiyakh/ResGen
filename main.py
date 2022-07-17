#!/usr/bin/env python3
from nltk.tokenize import word_tokenize
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()

with open('trial.txt') as f:
    lines = f.readlines()

    for line in lines:
        text = word_tokenize(line)
        nltk.pos_tag(text)
        print(text)


# >>> from nltk.tokenize import word_tokenize
# >>> s = '''Good muffins cost $3.88\nin New York.  Please buy me
# ... two of them.\n\nThanks.'''
# >>> word_tokenize(s)
