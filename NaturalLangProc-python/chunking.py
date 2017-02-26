#chunking allows us to group words togther by the tags!! Here we use regular expressions
import nltk
from nltk.tokenize import PunktSentenceTokenizer
#PunktSentenceTokenizer is a customizable tokenizer. It can scan a particular text body(corpus) and apply the same tokenizing pattern to another text!
req_text="Iam a man of very high honour. So don't you mess with me"
samp_text="This road leads to one of the most dangerous places on the Earth"
custom_token=PunktSentenceTokenizer(samp_text)
tokens=custom_token.tokenize(req_text)
for i in tokens:
	words=nltk.word_tokenize(i)
	tagged=nltk.pos_tag(words)
	print(tagged);
	#we will chunk together nouns,verbs,adverbs
	myChunk=r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"""
	chunkParse=nltk.RegexpParser(myChunk);
	chunked=chunkParse.parse(tagged);
	print (chunked)
	chunked.draw();#matplotlib must be installed to get the chunk tree. It helps to visualize your chunk data!
