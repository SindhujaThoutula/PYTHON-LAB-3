import nltk
import re, collections
from nltk.corpus import wordnet as wn
from nltk import pos_tag,ne_chunk
from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from collections import Counter
from nltk import FreqDist
from nltk import ngrams
from operator import itemgetter
with open('Sindhu.txt','r') as f:
 L=f.readlines()
print("L", L)
fr=''
for t in L:
    fr= fr + t
print(fr)
fr_word = word_tokenize(fr)
fr_sent = sent_tokenize(fr)
lemmatizer = WordNetLemmatizer()
fr_lemma = []
for word in fr_word:
    fr_lema = lemmatizer.lemmatize(word.lower())
    fr_lemma.append(fr_lema)
print("\n LEMMATIZATION")
print(fr_lemma)
fr_pos = pos_tag(fr_lemma)
print("BIGRAM")
n = 2
gram=[]
bigrams = ngrams(fr_lemma, n)
for grams in bigrams:
    gram.append(grams)
print(gram)
str1 = " ".join(str(x) for x,y in fr_pos)
str1_word = word_tokenize(str1)
print("BIGRAM(with freq)")
fdist1 = nltk.FreqDist(gram)
top_5 = fdist1.most_common()
top_five = fdist1.most_common(5)
top=sorted(top_5, key=itemgetter(0))
print(top)
print('TOP 5 BIGRAMS(with freq)')
print(top_five)
sent1 = sent_tokenize(fr)
rep_sent1 = []
for sent in sent1:
    for word,words in gram:
        for ((s, t), l) in top_five:
            if (word, words == s, t):
                rep_sent1.append(sent)
print ("TOP 5 BIGRAMS STATEMENTS")
print(max(rep_sent1,key=len))
