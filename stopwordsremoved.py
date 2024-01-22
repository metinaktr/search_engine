# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:58:30 2024

@author: Akademik
"""
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
    

nltk.download('stopwords')

text='This is example sentences demonsrating the removal of stopwords'

stop_words=set(stopwords.words('english'))

words=word_tokenize(text)

print(f"Sonuc={words}")

filtered_text=[word for word in words if word.lower() not in stop_words]

print(f"Sonuc={filtered_text}")


