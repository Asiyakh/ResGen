from sre_parse import Tokenizer
from transformers import AutoTokenizer, AutoModelForCausalLM #hugging face API
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch as nlp
import gensim.downloader as api #gensim API
from gensim.models import KeyedVectors
import string

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


def getBulletPoint(seed): #better name for function
    # take list created in above function and convert every word to its number usinh tokenizer.convert_tokens_to_ids(pad_token)..
    # make sure to pad so we know were to start/end 101/102 i believe (a lot of it in the code above commented out)
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")    

    sentence = seed.capitalize()
    input_ids = tokenizer(sentence, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, do_sample=False, max_length=40, pad_token_id=tokenizer.eos_token_id)
    sentence = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0];
    sentence = sentence.split(".")[0] #Don't want anything after a period
    prompt = sentence.split("\n")[0] #Don't want anything after a newline

    return prompt+"."
    
def solHF(seed):
    return getBulletPoint(seed)
