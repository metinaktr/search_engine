import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

#Tokennitzation

text = "feet bats"
t_w= nltk.word_tokenize(text)
print(f"Sonuc={t_w}")

lemmatizer=WordNetLemmatizer()

lemmatized_word=[lemmatizer.lemmatize(word) for word in t_w]
print(f"Lemmatized words={lemmatized_word}")
