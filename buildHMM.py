import os
import random
import numpy as np 
from collections import defaultdict
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

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

def priorDict():
    prior = dict()
    bulletpoints = open("trainingSet.txt", "r")
    for line in bulletpoints:
        line=line.split(" ")
        prior[line[0]] = prior.get(line[0], 0) + 1
    return prior

def transitionDict():
    transition = defaultdict(list)
    bulletpoints = open("trainingSet.txt", "r")
    for line in bulletpoints:
        line = line.strip(".\n")
        line=line.split(" ")
        count = 0
        
        while count < len(line)-1:
            tag1, tag2 = '', ''
            for word, tag in pos_tag(word_tokenize(line[count]), tagset='universal'):
                tag1 = tag
            for word, tag in pos_tag(word_tokenize(line[count+1]), tagset='universal'):
                tag2 = tag
            
            transition[tag1].append(tag2)
            count += 1
        transition[tag1].append("EOB")
    return transitionDictHelper(transition)

def transitionDictHelper(transition):
    newTransition =  defaultdict(list)
    for tag1 in UNIVERSAL_TAGS:
        for tag2 in UNIVERSAL_TAGS:
            newTransition[(tag1,tag2)].append(transition[tag1].count(tag2)/len(transition[tag1]))
    return newTransition

def emissionDict():
    # organizedTags: {tag:[List of words with this tag]}
    organizedTags = defaultdict(list)
    bulletpoints = open("trainingSet.txt", "r")

    for line in bulletpoints:
        text = pos_tag(word_tokenize(line), tagset='universal')
        count = 0

        for word, tag in text:
            if tag in organizedTags:
                organizedTags[tag].append(word)
            else:
                organizedTags[tag] = [word]

        count += 1
        organizedTags[line[count]].append("EOB")

    return emissionDictHelper(organizedTags)

def emissionDictHelper(organizedTags):
    # organizedTags: {tag:[List of words with this tag]}
    
    organizedTagsWithProbability = defaultdict(list)

    tups = open("output.txt", "r")
    for pair in tups:
        fullLine = pair[1:-2].split(",")
        word = fullLine[0][1:-1]
        tag = fullLine[1][2:-1]
     
        if len(organizedTags[tag]) != 0:
            organizedTagsWithProbability[tag, word] =  organizedTags[tag].count(word)/len(organizedTags[tag])
    
    return organizedTagsWithProbability

if __name__ == '__main__':
    emissionDict()
