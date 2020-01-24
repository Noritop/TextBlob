# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 10:03:51 2020

@author: Axel
"""

from textblob import sentiments, TextBlob

blob_naive_sentiment = ''
file = "source.txt"

f = open(file)
text = str(f.readlines())
text = text.replace("['", "")
text = text.replace("']", "")
f.close()

blob = TextBlob(text)
if blob.detect_language() != "en":
    blob = blob.translate(from_lang="fr", to='en')
    
a = str(blob)
a.replace("['", "")
a.replace("0]'", "")

blob_pattern = TextBlob (a)
blob_naive = TextBlob (a, analyzer=sentiments.NaiveBayesAnalyzer())

if blob_naive.sentiment[0] == 'pos':
    blob_naive_sentiment = 'positive'
else:
    blob_naive_sentiment = 'negative'

print('classification = ', blob_naive_sentiment)
print('proba. pos = ', round(blob_naive.sentiment[1],3))
print('proba. neg = ', round(blob_naive.sentiment[2],3))
print('subjectivity (0.0 -> subjective ; 1.0 - objective) =', round(blob_pattern.sentiment[1],3))











