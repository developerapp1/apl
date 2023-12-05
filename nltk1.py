import nltk
from nltk.stem import PorterStemmer

w  = PorterStemmer()
print(w.stem('walking'))
print(w.stem('walktalking'))
print(w.stem('rides'))