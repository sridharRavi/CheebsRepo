#Named Entity Parsing allows you to parse the sentence on natural entities such as Organization,Country etc.
import nltk
from nltk.tokenize import PunktSentenceTokenizer
samp_text="India is a country found on a really strong ethical reason. We were the original peacekeepers of South Asia"
req_text="Michaelangelo lived most of his life in Italy, a few years in the Vatican employed by the church. He painted the Sistine Chapel at St.Peter's Basilica. He was a famed 16th century painter" 
custom_token=PunktSentenceTokenizer(samp_text)
tokens=custom_token.tokenize(req_text)
for i in tokens:
	words=nltk.word_tokenize(i)
	tagged=nltk.pos_tag(words)
	print(tagged);
	net=nltk.ne_chunk(tagged);
	net.draw();#MATPLOTLIB Required!!
#ex..
#PERSON
#ORGANIZATION
#GPE-like Italy,Spain
#FACILITY
#DATE
#TIME
#LOCATION
#MONEY
#PERCENT