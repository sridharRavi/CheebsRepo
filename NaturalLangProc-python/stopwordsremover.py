#Stop words can be defined as any words which are in almost all cases UNNECESSARY for Natural Language Processing!
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nList=[];#list which will store the most USEFUL WORDS FOR NLP
example_sentence="Hello Boys and Girls, today we present to you the legendary singer Bob Dylan!!"
stwords=set(stopwords.words("English"))
reqwords=word_tokenize(example_sentence);
for w in reqwords:
	if w not in stwords:
		nList.append(w);
print(nList)




