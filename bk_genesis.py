import os, sys
import nltk
from nltk.corpus import words
import itertools
import math
import time

#"All" English words list
word_list = words.words()

print(word_list[0:2])


for L in range(2, len(word_list)+1):
    print("Sleeping")
    time.sleep(10)
    print("Going to work")
    for subset in itertools.combinations(word_list, L):

        last_line_number = 0
        print(subset)
        new_book = ' '.join(subset)
        book_title = new_book[0:100]
        print(new_book)

        
        with open('./index') as f:
            for line in f:
                pass
            last_line = line

            saved_last_line_number = " ".join(last_line.split()[2:])
            last_line_number = int(saved_last_line_number)
            print("Number:" + str(last_line_number+1))
        
        #Index new book
        
        f = open("./index", "a")
        f.write("\nTitle:" + book_title.replace(" ", "-") + " Number: " + str(last_line_number+1))
        f.close()

        #Save new book
        subfolder = os.makedirs(os.getcwd() + "/library/en/" + str(last_line_number+1))
        b = open("./library/en/" + str(last_line_number+1) + "/" + book_title.replace(" ", "-") + ".txt", "a")
        b.write(new_book)
        b.close()

