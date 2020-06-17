import wikipedia
import nltk
import re
from collections import Counter 

#removes all numbers and punctuations
def removeDigAndPunc(list):
    pattern = '[^A-Za-z+=#/@#$%&*~ ]'
    list = [re.sub(pattern,'',i) for i in list]
    return list

print("Wikipedia article")

# Tensorflow content is retrieved from its respective Wikipedia Page
string = (wikipedia.page("Tensorflow").content)
print(string)
print()
token = nltk.word_tokenize(string)
new_string = removeDigAndPunc(token)
#while("" in new_string):
    #new_string.remove("")
print("Wikipedia article without numbers and punctuations")
print()
for i in new_string:
    print(i,end = ' ')
print()
stop_words = set(nltk.corpus.stopwords.words('english'))                # finds all stopwords
print("Stop words used:")
print()
print(stop_words)
print()
nostopstring = []
for i in new_string:
    if i not in stop_words:
        nostopstring.append(i)                             #appends words that are not part of stop words
print("Wikipedia article without stopwords")
print()
for i in nostopstring:
    print(i,end = ' ')
print()
unique =set(nostopstring)
print("Number of distinct words =",len(unique))
length1 = len(unique)
Counter = Counter(unique)
top_ten = Counter.most_common(10)
print("Top 10 words")
for i in top_ten:
    print(i[0],i[1],(i[1]/length1)*100)