
# This program is responsible to: 1. Tokenize
#                                 2. Remove Stop words
#                                 3. Remove punctuation characters

import nltk
from nltk.corpus import stopwords
import string 


nltk.download('punkt')

stop_words= stopwords.words('english')
#punct = string.punctuation

sentence="HI !! Its great to have u as prt of this class. I'm delighted to be hosting this session - Workwithme. Can I start ?? "


def tokenize(sen):
    """
    
    Parameters: sen (str) 
                sen is the sentence the user input
                
                
    This function is responsible to: 1. Tokenize
                                     2. Remove Stop words
                                     3. Remove punctuation characters
                                     
    """
    word_list = nltk.word_tokenize(sen)
    filtered_words = []
    for word in word_list:
        if (word not in string.punctuation) and (word not in stopwords.words('english')):
            filtered_words.append(word.lower())
            
    return filtered_words


the_words = tokenize(sentence)
print(the_words)