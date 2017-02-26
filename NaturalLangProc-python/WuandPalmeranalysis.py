import nltk
from nltk.corpus import wordnet
#The Wu and Palmer method is mainly used to estimate the amount of semantic similarity between two words.
w1=wordnet.synset("Cup.n.01")
w2=wordnet.synset("Saucer.n.01");
print(w1.wup_similarity(w2));
w1=wordnet.synset("Ship.n.01")
w2=wordnet.synset("Boat.n.01");
print(w1.wup_similarity(w2));
w1=wordnet.synset("Ship.n.01")
w2=wordnet.synset("Submarine.n.01");
print(w1.wup_similarity(w2));
#similarity between Cup and Saucer 0.142 14%similar
#similarity between Ship and Boat 0.909  90% similar
#similarity between Ship and Submarine 0.88 88% similar
