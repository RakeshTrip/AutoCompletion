# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 06:27:10 2015

@author: Rakesh
"""
import utility as utl 
######################## Main Module for prediction################

def main():
         
     #-----------Formatting new word------------#         
     new_sent = input('Enter a sentence: ') # program stops here for i/p
     text = utl.cleanText(new_sent)
     temp = []
     for words in text.split():
         temp.append(words)
         
     #----------------Predict new word-------------#
         
     key = utl.predictText(temp)
     for word in key:
         new_sent = new_sent + " " +word
     
     print("Predicted Sentence: ",new_sent)
    
     
if __name__ == '__main__':
    main()     
