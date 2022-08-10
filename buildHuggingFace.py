import token
import transformers
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch as nlp

# from torchtext.legacy import data
# from torchtext.legacy import datasets

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

#function needs a better name
def priorDict(): # This function returns list of toekens #ignore all the comments was using it for something else
    #data processing
    # tokenizer = transformers.BertTokenizer.from_pretrained('bert-base-uncased')
    # sample_text = "Hi my name is nima."
    # tokens = tokenizer.tokenize(sample_text)
    # print (tokens[0])
    # return None
    # init_token = tokenizer.cls_token
    # pad_token = tokenizer.pad_token
    # unk_token = tokenizer.unk_token

    # init_token_idx = tokenizer.convert_tokens_to_ids(init_token)
    # pad_token_idx = tokenizer.convert_tokens_to_ids(pad_token)
    # unk_token_idx = tokenizer.convert_tokens_to_ids(unk_token)
    # max_input_length = tokenizer.max_model_input_sizes['bert-base-uncased']

    # # print(init_token, pad_token, unk_token)
    # SEED = 1234

    # random.seed(SEED)
    # np.random.seed(SEED)
    # torch.manual_seed(SEED)
    # torch.backends.cudnn.deterministic = True

    # text_preprocessor = functools.partial(cut_and_convert_to_id,
    #                                   tokenizer = tokenizer,
    #                                   max_input_length = max_input_length)

    # tag_preprocessor = functools.partial(cut_to_max_length,
    #                                  max_input_length = max_input_length)


    # TEXT = data.Field(use_vocab = False,
    #               lower = True,
    #               preprocessing = text_preprocessor,
    #               init_token = init_token_idx,
    #               pad_token = pad_token_idx,
    #               unk_token = unk_token_idx)

    # UD_TAGS = data.Field(unk_token = None,
    #                     init_token = '<pad>',
    #                     preprocessing = tag_preprocessor)
    
    # fields = (("text", TEXT), ("udtags", UD_TAGS))
    # train_data, valid_data, test_data = datasets.UDPOS.splits(fields)
    # print(vars(train_data.examples[0]))

    f = open('trainingSet.txt')
    lines = f.readlines()
    tags = []
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    # for token in tokenizer.vocab.keys():
    #     (token)
        # print(token)

    for line in lines:
        # tokens = tokenizer.tokenize("[CLS] " + line + " [SEP]")
        tokens = tokenizer.tokenize(line)
        tokenIds = tokenizer.convert_tokens_to_ids(tokens)
        tags.append(tokens)
        # tags.append(tokenizer.convert_tokens_to_ids((tokens[0])))
        # print(f'Bullet point: {line}')
        # print(f'Tokens: {tokens}' )
        # print(f'TokensId: {tokenIds}' )
        # print(tokens[0])

    # print(tags)
    # print(tags.count("generated")
    return tags

def getBulletPointPrefix(): #better name for function
    # take list created in above function and convert every word to its number usinh tokenizer.convert_tokens_to_ids(pad_token).. 
    # make sure to pad so we know were to start/end 101/102 i believe (a lot of it in the code above commented out)
    # use the probbabiliy.. i tried to use seed but im confused aboyut that
    # after getting prob, u should be able to get next best word which is a number bc we coberted the token and then untokenize it
    # meaning pyt it as a word and thats the next word
    return None
    #Alot of the code intended to be here is commented in the code above
    
    


if __name__ == '__main__':
    prior = priorDict()
    print(prior)

