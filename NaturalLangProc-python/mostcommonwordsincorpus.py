import nltk
from nltk.corpus import movie_reviews #ysing the movie review corpus in nltk package.
import random

#documents=[(list(movie_reviews.words(fileid)),category) for category in movie_reviews.categories()
#			for fileid in movie_reviews.fileids(category)]
#random.shuffle(documents);
all_words=[];
for w in movie_reviews.words():
	all_words.append(w.lower())
all_words=nltk.FreqDist(all_words);
#we will print the most commonly used 100 words
print(all_words.most_common(100))
