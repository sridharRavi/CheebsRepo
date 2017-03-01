import nltk
from nltk.corpus import movie_reviews #ysing the movie review corpus in nltk package.
import random
documents=[(list(movie_reviews.words(fileid)),category) for category in movie_reviews.categories()
			for fileid in movie_reviews.fileids(category)]
random.shuffle(documents);
all_words=[];
for w in movie_reviews.words():
	all_words.append(w.lower())
all_words=nltk.FreqDist(all_words);
#we will print the most commonly used 100 words
#print(all_words.most_common(100));
word_features=list(all_words.keys())[:3000];

def find_features(document):
	words=set(document)
	features=[]
	for w in word_features:
		features[w]=(w in words);
	return features;

featuresets=[(find_features(rev),category) for (rev,category) in documents]
training_set=featuresets[:1000]
testing_set=featuresets[1000:]
classifier=nltk.NaiveBayesClassifier.train(training_set);
#Will provide different accuracy for different datasets
print("NaiveBayesClassifier Algo Efficiency:",(nltk.classify.accuracy(classifier,testing_set))*100)
#will show the most informative features which help in classification
classifier.show_most_informative_features(15);