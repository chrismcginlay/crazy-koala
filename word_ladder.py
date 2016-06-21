# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 09:40:24 2016

@author: chrismcginlay
Word Ladder Game
"""
import enchant

eng_dict = enchant.Dict("en_GB")
word_initial = "LISP"
word_final = "JAVA"
history = []
history.append(word_initial)
word_2chk = ""
word_exists = False #Word is in the dictionary

while word_2chk!=word_final:
    print(history)
    last_word = history[-1]
    word_exists = False
    
    while not word_exists:
        selection = 0
        while selection<1 or selection>4:
            selection = int(input(
                "Please select the number of the letter to alter 1-4"))
        letter_index = selection-1 #python strings are zero indexed
        print("You have selected letter {0} ie {1}." \
            .format(selection,last_word[selection-1]))
            
        letter_new = input("Please select a new letter ")
        word_2chk =     last_word[:letter_index] + \
                        letter_new + \
                        last_word[letter_index+1:]
        word_exists = eng_dict.check(word_2chk)
        if not word_exists:
            print("{0} is not allowed - it's not in the dictionary" \
                .format(word_2chk))
                
    history.append(word_2chk)
    
print("You took {0} attempts".format(len(history)-1))
print(history)
    
