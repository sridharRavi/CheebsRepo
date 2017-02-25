
#Tokenizing an input string into a number of smaller components is very useful for Natural Language Processing
import nltk
from nltk import word_tokenize 
from nltk import sent_tokenize
example_sentence="Hello,There how are you,Iam Sridhar from Chennai,India. Great to see you!!"
words=word_tokenize(example_sentence)
sents=sent_tokenize(example_sentence);
print (words)
print (sents)