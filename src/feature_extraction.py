### Import packages to create absolute file path & make code independent of operating system

from pathlib import Path
import os.path
import sys

import warnings
warnings.filterwarnings("ignore")

### Import packages for data manipulation

import pandas as pd
import numpy as np
import re

### Import feature extraction help functions

from common_utils.feature_helpers import JaccardSimilarity, Similarity, WordCounter, CodeCheck, CodeCounter, Ngrams, TopTagEncoder, toptagslist

### Read in dataset

print(os.getcwd())

base_path = Path("__file__").parent
full_path = (base_path / "../data/processed/stackoverflow_preprocessed_all.csv").resolve()
stackoverflow = pd.read_csv(os.path.join(full_path))

stackoverflow.info()

### Preparing input for training word embeddings

from gensim.models import Word2Vec

sentences = [str(x).split(' ') for x in stackoverflow['answer_text_clean']]
print(sentences)

model = Word2Vec(sentences, 
                 min_count=5,   # Ignore words that appear less than this
                 size=300,      # Dimensionality of word embeddings
                 workers=4,     # Number of processors (parallelisation)
                 window=5,      # Context window for words during training
                 iter=10,       # Number of epochs training over corpus
                 )

model.vector_size
len(model.wv.vocab)
model.most_similar('easy')
model.most_similar('python')


from sklearn.decomposition import PCA
from matplotlib import pyplot

X = model[model.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(model.wv.vocab)
for i, word in enumerate(words):
	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()

### Drop all observations / rows with any missing values in the column "answer_text_clean"

stackoverflow = stackoverflow.dropna(how='any', subset=['answer_text_clean', 'question_title_clean'])

### Print out dataset for overview

stackoverflow.head()

### Check if Similarity score class works as desired

similarity_scorer = Similarity(stackoverflow)
stackoverflow_new = similarity_scorer.transform(stackoverflow)
stackoverflow_new.head(10)

### Check if Jaccard Similarity score class works as desired

jaccard_similarity = JaccardSimilarity(stackoverflow)
stackoverflow_new = jaccard_similarity.transform(stackoverflow)
stackoverflow_new.head(10)

### Check if WordCounter class works as desired

wordcounter = WordCounter(stackoverflow[['answer_text_clean']])
stackoverflow_new = wordcounter.transform(stackoverflow[['answer_text_clean']])
stackoverflow_new.head()

### Check if CodeCheck class works as desired

codecheck = CodeCheck(stackoverflow) 
stackover_new = codecheck.transform(stackoverflow)
stackover_new.head()

### Check ratio of code vs. no code in answers

stackover_new['code_binary'].value_counts()

### Check if CodeCounter class works as desired

codecount = CodeCounter(stackoverflow) 
stack_new = codecount.transform(stackoverflow)
stack_new.head()

### Check distribution of code counts

stack_new['code_count'].value_counts().sort_index()

### Check if Ngrams classs works as desired

ngrams = Ngrams(stackoverflow['answer_text_clean'])
stackover_new = ngrams.transform(stackoverflow[['answer_text_clean']])
print(stackover_new)

### Check if TopTagsEncoder works as desired

toptagencoded = TopTagEncoder(stackoverflow)
stack_tags_new = toptagencoded.transform(stackoverflow)
print(stack_tags_new)

### Save data tested on feature extraction functions to a csv file

base_path = Path("__file__").parent
full_path = (base_path / "../data/processed/stackoverflow_modeling.csv").resolve()
stackoverflow.to_csv(os.path.join(full_path))

