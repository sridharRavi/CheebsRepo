import nltk
from nltk.corpus import wordnet
#wordnet is a powerful package which provides synonyms,antonyms,lemmas for your required text(Corpus)
#synsets will return the sets of all possible synonyms for the word
val=wordnet.synsets("Nice")
print (val[0].definition())#will provide the actual definition of thhe word
print(val);
synonyms=[];
antonyms=[]
for i in wordnet.synsets("perfect"):
	for j in i.lemmas():
		synonyms.append(j);
		if j.antonyms():
			antonyms.append(j);
print(synonyms)
print (antonyms)
