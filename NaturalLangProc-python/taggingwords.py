#In NLP, it is very important to know about the properties of the words. So it is important to tag them to understand their nature.
#understanding the word's nature and tag will be useful during NLP
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
#The various tags assosciated with words in the English Language are...
#CC: conjunction, coordinating
#CD: numeral, cardinal
#DT: determiner
#IN: preposition or conjunction, subordinating
#JJ: adjective or numeral, ordinal
#JJR: adjective, comparative
#JJS: adjective, superlative
#LS: list item marker
#MD: modal auxiliary
#NN: noun, common, singular or mass
#NNP: noun, proper, singular
#NNS: noun, common, plural
#PDT: pre-determiner
#POS: genitive marker
#PRP: pronoun, personal
#PRP$: pronoun, possessive
#RB: adverb
#RBR: adverb, comparative
#RBS: adverb, superlative
#TO: "to" as preposition or infinitive marker
#UH: interjection
#VB: verb, base form
#VBD: verb, past tense
#VBG: verb, present participle or gerund
#VBN: verb, past participle
#VBP: verb, present tense, not 3rd person singular
#VBZ: verb, present tense, 3rd person singular
#WDT: WH-determiner
#WP: WH-pronoun
#WRB: Wh-adverb