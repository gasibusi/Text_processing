from nltk import word_tokenize
import pandas as pd
import numpy as np
import nltk

porter = nltk.PorterStemmer()

data = pd.read_csv('TEXT-Dresses-All-Products.txt',sep="|")

colours = pd.read_csv('color.txt',header=0)
categories = pd.read_csv('category.txt',header=0)
categories = list(categories.category)
names = list(data.ProductName)
descriptions = list(data.Description)

for i in xrange(len(names)):
    description = str(descriptions[i])
    name = str(names[i])
    description = name + '. ' + description
    try:
        tokenized = word_tokenize(description)
        tokenized = [s.lower() for s in tokenized]
        tokenized = [porter.stem(t) for t in tokenized]
        category_index = [tokenized.index(category) for category in categories if category in tokenized]
        print list(np.array(tokenized)[category_index])
        if len(category_index) > 1 and len(set(list(np.array(tokenized)[category_index])))>1:
            for j in range(len(category_index)-1):
                category1 = tokenized[category_index[j]]
                category2 = tokenized[category_index[j+1]]
                if 'wear with' in ' '.join(tokenized[category_index[j]:category_index[j+1]]):
                    print description
                if 'pair with' in ' '.join(tokenized[category_index[j]:category_index[j+1]]):
                    print description
    except UnicodeDecodeError,e:
        continue
