import os
import random
import numpy as np 
from collections import defaultdict

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
            transition[line[count]].append(line[count+1])
            count += 1
        transition[line[count]].append("EOB")
    return transition

def buildPrior(prior):
    tot = sum(list(prior.values()))
    new = []
    for i in list(prior.values()):
        new.append(i/tot)
    return np.random.choice(list(prior.keys()), 1, True, new)[0]

if __name__ == '__main__':
    prior = priorDict()
    transition = transitionDict()
    bulletpoint = open("bulletPoints.txt", "w")
    count = 0
    while count < 500:
        word = buildPrior(prior)
        while word != "EOB":
            bulletpoint.write(word)
            bulletpoint.write(" ")
            word = random.choice(transition[word])
        
        bulletpoint.write(".\n") 
        count += 1
    
    
    