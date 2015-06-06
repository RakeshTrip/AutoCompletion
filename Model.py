# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 22:28:51 2015

@author: Rakesh
"""

import nltk.stem 
from itertools import chain
import time
import pickle
from utility import cleanText
######################## Main Module for creating corpus################

def main():
     
     start_time = time.time()
     file_train = "C:\\Users\\Rakesh\\Desktop\\tweets.txt"     
     
     #----------Tokenization and build corpus----------------#   
     bgs = nltk.bigrams(" ")
     tgs = nltk.trigrams(" ")
     ngs = nltk.ngrams(" ", 4)     
          
     fp = open(file_train, 'rb')
     for line in fp:
         text = cleanText(line)
         tokens = nltk.word_tokenize(text)        
         #Create your bigrams
         bgs = chain(bgs, nltk.bigrams(tokens))
         tgs = chain(tgs, nltk.trigrams(tokens))
         ngs = chain(ngs, nltk.ngrams(tokens,4))
         
     fbdist = nltk.FreqDist(bgs)
     ftdist = nltk.FreqDist(tgs)
     fndist = nltk.FreqDist(ngs)
     
     file_pickle = "C:\\Users\\Rakesh\\Desktop\\bgs.pickle"
     with open(file_pickle, 'wb') as handle:
         pickle.dump(fbdist, handle)
     handle.close()
     
     file_pickle = "C:\\Users\\Rakesh\\Desktop\\tgs.pickle"
     with open(file_pickle, 'wb') as handle:
         pickle.dump(ftdist, handle)
     handle.close()
     
     file_pickle = "C:\\Users\\Rakesh\\Desktop\\ngs.pickle"
     with open(file_pickle, 'wb') as handle:
         pickle.dump(fndist, handle)
     handle.close()
     
     print("--- %s seconds to build corpus---" % (time.time() - start_time))
    
     
if __name__ == '__main__':
    main()       
