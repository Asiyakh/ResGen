#!/usr/bin/env python3

import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import ssl


#nltk.download() #comment out after running once. 
def priorTag():
    f = open('trainingSet.txt')
    lines = f.readlines()
    tags=[]

    for line in lines:
        text = pos_tag(word_tokenize(line), tagset='universal')
        tags.append(text[0][1])
    return tags

with open('trainingSet.txt') as f:
    lines = f.readlines()
    f = open("tags.txt", "w")

    for line in lines:
        text = pos_tag(word_tokenize(line), tagset='universal')

        for pair in text: # pair -> (word, tag)
            f.write(str(pair))
            f.write('\n')
        
    f.close()

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download()
#
# with open('trial.txt') as f:
#     lines = f.readlines()
#
#     for line in lines:
#         text = word_tokenize(line)
#         nltk.pos_tag(text)
#         print(text)


# >>> from nltk.tokenize import word_tokenize
# >>> s = '''Good muffins cost $3.88\nin New York.  Please buy me
# ... two of them.\n\nThanks.'''
# >>> word_tokenize(s)
