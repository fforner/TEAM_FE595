import spacy
import numpy as np
import re
from textblob import TextBlob
import pandas as pd


x = 'I am the best human in the word! I want beens.'

def similarity(x, word1, word2):
    ''' thanks to this funciton it is possible to comapare the similarity
     of all the names in the imput phrases and two words that i wnat.
    '''
    fra = TextBlob(x)
    a = pd.DataFrame(fra.tags)

    z = []
    for i in range(len(a)):
        if a.iloc[i,1] =='NN' or a.iloc[i,1] =='NNS':
            z.append(a.iloc[i,0].lower())
    npl_small = spacy.load('en_core_web_sm')
    for i in z:
        string =str(i)
        good = npl_small(word1).similarity(npl_small(string)) 
        bad = npl_small(word2).similarity(npl_small(string)) #do a similarity with bad  
        print(f'\n The name "{i}" has a similarity with "{str(word1)}" of: {good}, and with "{str(word2)}" of: {bad}')   
    pass


similarity(x, 'seed', 'bad')
            
