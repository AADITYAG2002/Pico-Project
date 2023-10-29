import re
import json
from lib.porter_stemmer import PorterStemmer

def tokenize(sentence):
    #tokenization
    special_characters = ['!','?','"','#','$','%','&','(',')','*','+','/',':',';','<','=','>','@','[','\\',']','^','`','{','|','}','~','\t']
    for i in special_characters:
        sentence = sentence.replace(i, '')
    word_list = re.sub(r"[^a-zA-Z0-9]", " ", sentence.lower()).split(' ')
    return word_list

def stem(word):
    #Stemming http://people.scs.carleton.ca/~armyunis/projects/KAPI/porter.pdf
    p = PorterStemmer()
    stemmed_word = p.stem(word,0, len(word)-1)
    return stemmed_word

def bow(sentence):
    sentence = sentence.lower()    
    sentence_words = tokenize(sentence)
    sentence_words = [stem(word) for word in sentence_words]

    #Vectorization : bag of words
    bag_of_words = json.load(open('words.json', 'r'))
    bag = [0]*len(bag_of_words)
    for w in sentence_words:
        for i,word in enumerate(bag_of_words):
            if word == w:
                bag[i] = 1

    return bag
