# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 22:28:51 2015

@author: Rakesh
"""

import re
import time
import pickle
from nltk.corpus import stopwords
import nltk.stem
######################## Clean the text #############
def cleanText(line):
    if isinstance(line, str):
        text = str(line)
    else:
        text = line.decode("utf-8")
    
    text = re.sub(r"http\S+", "", text)
     
    text = ' '.join(re.sub("(@[A-Za-z0-9]+) |([^0-9A-Za-z \t]+)|(\w+:\/\/\S+) "," ",text).split())  
   
    tokens = ""
    
    stop = stopwords.words('english')
    english_lemma = nltk.stem.WordNetLemmatizer()
    
    for words in text.split():
        words = words.lower()
        if len(words) is not 1 and words not in stop:
            tokens = tokens + " " +  english_lemma.lemmatize(words)
    return tokens
    
    
######################## predict the word ############

def predictText(temp):
    
     fbdist, ftdist, fndist = load_corpus()
    
     start_time = time.time()
     
     size = len(temp)
       
     if size >= 3:  
         key1 = matchn(fndist, temp[size-3:])
         if key1:
             key = matchn(fndist, key1[1:]) # last 3 word in 4 word key
             if not key:
                 key = key1[-1]
             else:
                 key = key[len(key)-2:]
         else:
             key = key1
             
     elif size == 2:
         key1 = matcht(ftdist, temp)
         if key1: 
             key = matchn(fndist, key1)
             if not key:
                 key = key1[-1]
             else:
                 key = key[len(key)-2:]
         else:
             key = key1
             
     elif size == 1:
         key1 = matchb(fbdist, temp)   
         if key1:          
             key = matcht(ftdist, key1)
             if not key:
                 key = key1[-1]
             else:
                 key = key[len(key)-2:]
         else:
             key = key1        
     else:
         print("Invalid string!")
     
     #print("--- %s seconds to predict new text ---" % (time.time() - start_time))
     return key 
######################## Match and Print ############

def matchb(fdist, f):
     
     Max_Freq = 0
     key = []
     for k in fdist.keys():
         if k[0] == f[0]:
             if Max_Freq < fdist[k]:
                 Max_Freq = fdist[k]
                 key = k 
            
     #print(f, pred_word, Max_Freq)
     return key

def matcht(fdist, f):
     Max_Freq = 0
     key = []
     for k in fdist.keys():
         if k[0] == f[0] and k[1] == f[1]:
             if Max_Freq < fdist[k]:
                 Max_Freq = fdist[k]
                 key = k 
             
     #print(f, pred_word, Max_Freq)
     return key     
     
def matchn(fdist, f):     
     Max_Freq = 0
     key = []
     for k in fdist.keys():
         if k[0] == f[0] and k[1] == f[1] and k[2] == f[2]:
             if Max_Freq < fdist[k]:
                 Max_Freq = fdist[k]
                 key = k
             
     #print(f, pred_word, Max_Freq)
     return key  


######################## load corpus ############   
def load_corpus():

    
     file_pickle = "C:\\Users\\Rakesh\\Desktop\\bgs.pickle"
     with open(file_pickle, 'rb') as handle:
         fbdist = pickle.load(handle)
     handle.close()
     
     file_pickle = "C:\\Users\\Rakesh\\Desktop\\tgs.pickle"
     with open(file_pickle, 'rb') as handle:
         ftdist = pickle.load(handle)
     handle.close()
     
     file_pickle = "C:\\Users\\Rakesh\\Desktop\\ngs.pickle"
     with open(file_pickle, 'rb') as handle:
         fndist = pickle.load(handle)
     handle.close()
     
     return fbdist, ftdist, fndist
