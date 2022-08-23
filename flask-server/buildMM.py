import os
import numpy as np 
from collections import defaultdict
import sys
import json
import ast

def priorDict():
    prior = dict()
    bulletpoints = open("trainingSet.txt", "r")
    for line in bulletpoints:
        line=line.split(" ")
        prior[line[0].lower()] = prior.get(line[0].lower(), 0) + 1
    return prior

def transitionDict():
    transition = defaultdict(list)
    bulletpoints = open("trainingSet.txt", "r")
    for line in bulletpoints:
        line = line.strip(".\n")
        line = line.strip(".")
        line=line.split(" ")
        count = 0
        while count < len(line)-1:
            transition[line[count]].append(line[count+1])
            count += 1
        transition[line[count]].append("EOB")
    return transition

def buildPrior(prior):
    tot = sum(list(prior.values()))
    new = []
    for i in list(prior.values()):
        new.append(i/tot)
    return np.random.choice(list(prior.keys()), 1, True, new)[0].capitalize()

def sol(seed):
    transition=transitionDict()
    bulletpoint = ""
    if not seed:
        prior = priorDict()
        word = buildPrior(prior)
    else:
        for s in seed.split(' ')[:-1]:
            bulletpoint+=s
            bulletpoint+=' '
        word = seed.split(' ')[-1] # [generate, with]
        word = word[0].lower() + word[1:]

    while word != "EOB":
        word = word.strip(". ")
        bulletpoint+=word
        word = np.random.choice(transition[word])
        if word == "EOB":
            bulletpoint+=".\n"
            pass
        bulletpoint+=" "
    return bulletpoint.capitalize()


    
    