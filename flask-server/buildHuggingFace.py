from sre_parse import Tokenizer
import token
import tokenize
import transformers
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch as nlp
import gensim.downloader as api #gensim API
from gensim.models import KeyedVectors
import string

from transformers import BertTokenizer, BertModel, BertForMaskedLM, AutoTokenizer, AutoModel

import numpy as np

import time
import random
import functools

UNIVERSAL_TAGS = [
    "VERB",
    "NOUN",
    "ADP",
    "DET",
    "ADJ",
    "CONJ",
    ".",
    "NUM",
    "PRT",
    "ADV",
    "PRON"
]


def getBulletPointPrefix(sentence): #better name for function
    # take list created in above function and convert every word to its number usinh tokenizer.convert_tokens_to_ids(pad_token)..
    # make sure to pad so we know were to start/end 101/102 i believe (a lot of it in the code above commented out)

    word_vectors = KeyedVectors.load('vectors.bin') #load pre-trained GLOVE word vectors, trained on twitter data
    punctuation = ["!", ",", ".", "?", "'"]   
    sentence = sentence.split()
    prompt = " "
    for word in sentence:
        try:
            result = word_vectors.similar_by_word(word) #are there similar words?  If yes locate the top 10 most similar
            result = [x[0] for x in result] #create a list of similar words
            #choice = random.choice(result) #pick one of the most similar ones at random
            choice = result[0] #alternately, select the MOST similar word based on embedding proximity
        except: #we will end up here if there are NO similar words among the training data
            choice = word
        if choice not in punctuation: #if we generated a punctuation symbol, we don't want it
            prompt = prompt + " " + choice

    return prompt    
    
def solHF(seed):
    return getBulletPointPrefix(seed)

if __name__ == "__main__":
    vectors = api.load('glove-wiki-gigaword-50')
    vectors.save('vectors.bin')