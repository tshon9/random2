import pandas as pd
import re
import numpy as np
import math
import os
import random
import sys
from datetime import datetime as dt
import collections


string = "ACCBADCCA"
k = 3
print
print("string")
def merge_the_tools(string, k):
    # your code goes here
    subset = [string[i:i + k]for i in range(0, len(string), k)]
    final =[]
    for x in subset:
        seen = ''
        for c in x:
            if c not in seen:
                seen+=c
        final.append(seen)
    print (final)

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    return (str(int(abs((dt.strptime(t1, fmt) - dt.strptime(t2, fmt)).total_seconds()))))

def find_angle():
    AB, BC = int(input()), int(input())
    res = str(int(round(math.degrees(math.atan(AB/BC)))))  # to calculate hypotenuse
      # to calculate required angle
    degree = chr(176)  # for DEGREE symbol
    print(res, degree, sep='')


def minion_game(string):
    vowel = ["A","E","I","O","U"]
    all_combinations =[]
    stuart={}
    kevin ={}
    for i in range(0,len(string)):
        for j in range(i+1,len(string)+1):
            all_combinations.append(string[i:j])
    all_combinations = list(set(all_combinations))
    #print(all_combinations)
    score_dict = dict.fromkeys(all_combinations, 0)
    for x in score_dict:
        sb_len = len(x)
        results =0
        for i in range(len(string)):
            if string[i:i+sb_len]==x:
                results+=1
        score_dict[x] = results


    for x in score_dict:
        if x[0] in vowel:
            kevin[x] = score_dict[x]
        else:
            stuart[x] = score_dict[x]

    # for x,y in stuart.items():
    #     print(x,y)

    score1 = 0
    score2 = 0
    for x in stuart:
        score1 += stuart[x]
        # print(score1)
    for x in kevin:
        score2 += kevin[x]
        # print(score2)

    if score1>score2:
        print("Stuart", str(int(score1)), sep=" ")
    elif score1<score2:
        print("Kevin", str(int(score2)), sep=" ")
    else:
        print("Draw")

def happiness_score():
    array = "1 2 3".split()
    like= set("1 0".split())
    dislike = set("2 5 3".split())
    score =0
    print(array)
    for x in array:
        print(x)
        if x in like:
            score+=1
        elif x in dislike:
            score-=1
    print(score)
    print(sum([(i in like) - (i in dislike) for i in array]))

def word_order():
    dict = OrderedDict()
    for i in range(int(input())):
        # If input not in the dictionary, then add it
        # else increment the counter
        key = input()
        if not key in dict.keys():
            dict.update({key: 1})
            continue
        dict[key] += 1

    print(len(dict.keys()))
    print(*dict.values())

def roll():
    return random.randint(1,6)

def run(n):
    total = 0
    rolls=[]
    while total<=n:
        cur = roll()
        rolls.append(cur)
        total += cur
    return rolls[-2]

def sim():
    random.seed()
    iterations = 10000
    count = collections.Counter(run(63) for i in range(iterations))
    for value, cnt in count.items():
        chance = cnt/float(iterations)
        print("{}: {} {}".format(value, chance, chance))
if __name__ == '__main__':
    sim()