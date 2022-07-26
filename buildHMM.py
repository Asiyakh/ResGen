from ctypes.wintypes import tagPOINT
import os
import random
import numpy as np 
from collections import defaultdict
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from main import priorTag

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

def buildPrior(prior):
    return np.random.choice(list(prior.keys()), 1, True, list(prior.values()))[0]   #random or no?

def priorDict():
    prior = priorTag()
    priorDict = {}
    tot = len(prior)
    for tag in UNIVERSAL_TAGS:
        priorDict[tag] = prior.count(tag)/tot
    return priorDict

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
            newTransition[(tag1,tag2)].append(transition[tag1].count(tag2)/len(transition[tag1]-1))
    return newTransition

def buildTransition():
    oldTransition = transitionDict()
    newTransition =  defaultdict()
    for (tag1, tag2) in oldTransition:
        percentage = oldTransition[(tag1, tag2)]
        if tag1 not in newTransition:
            newTransition1 = defaultdict()
            newTransition1[tag2] = percentage[0]
            newTransition[tag1] = newTransition1
        else:
            (newTransition[tag1])[tag2] = percentage[0]
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

def buildEmission():
    oldEmission = emissionDict()
    newEmission =  defaultdict()
    for (tag, word) in oldEmission:
        percentage = oldEmission[(tag, word)]
        if tag not in newEmission:
            newEmission1 = defaultdict()
            newEmission1[word] = percentage
            newEmission[tag] = newEmission1
        else:
            (newEmission[tag])[word] = percentage
    return newEmission

if __name__ == '__main__':
    prior = priorDict()
    transition = buildTransition()
    emission = buildEmission()
    bulletpoint = open("HMMbulletPoints.txt", "w")
    count = 0
    print(transition['VERB'])
    print(sum(list(transition['NOUN'].values())))
    # while count < 500:
    #     tag = buildPrior(prior)
    #     while  tag != ".":
    #         word =  np.random.choice(list(emission[tag].keys()), 1, True, list(emission[tag].values()))[0]   #random or no?
    #         bulletpoint.write(word)
    #         bulletpoint.write(" ")
    #         tag = np.random.choice(list(transition[tag].keys()), 1, True, list(transition[tag].values()))[0]
    #     bulletpoint.write(".\n") 
    #     count += 1
    
