from spacy.en import English
from nltk import word_tokenize
import pandas as pd
import numpy as np
import nltk
import sys

porter = nltk.PorterStemmer()
parser = English()

data = pd.read_csv('TEXT-Dresses-All-Products.txt',sep="|")
data = data.drop_duplicates('ProductId')

colours = pd.read_csv('color.txt',header=0)
categories = pd.read_csv('category.txt',header=0)
categories = list(categories.category)
features = pd.read_csv('features.txt',header=0)
features = list(features.features)


names = list(data.ProductName)
descriptions = list(data.Description)

sent = []
for description in descriptions:
    sent = sent + str(description).decode('utf-8').split(".")
#for sentence in sent:
#    tokens = parser(sentence)
#    tokenized = [s.lower_ for s in tokens]
#    tokenized = [porter.stem(t) for t in tokenized]

#    if 'dress' in tokenized:
#        dress_id = tokenized.index('dress')
#        pos =  [t.pos_ for t in tokens]
#        if pos[max(dress_id-1,0)]=='ADJ':
#            print sentence
#sys.exit()
        
sub_sent = []
for i in xrange(len(features)):
    feature = features[i]
    print 'the feature to look at is ', feature
    for sentence in sent:
        tokens = parser(sentence)  
        tokenized = [s.lower_ for s in tokens]
        tokenized = [porter.stem(t) for t in tokenized]
        if feature in tokenized and 'dress' in tokenized: 
            print sentence
    sys.exit()
