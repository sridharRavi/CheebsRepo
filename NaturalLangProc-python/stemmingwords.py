#The Stem of any word can be described as the base of the word. The words of the same stem usually convey the same meaning!! So very important to analyse thse words in NLP
#Ex. I must MEET him
#I just MET him
#He scheduled a MEETING
#In this case all of these highlightd words have the exact same meaning although in a different tense and context
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
st=PorterStemmer();
myList=["Pythonistas","Pythonly","Pythonic","Pythonified"]
#Let us check the stem words for our List
for w in myList:
	print st.stem(w);
#The stem of every word of our list is!!
#Pythonista
#Pythonli
#Python
#Pythonifi
#let us now try it for a completely different sentence!!
mySent="Hello there! Do you want fries with that?"
wd=word_tokenize(mySent)
for w in wd:
	print st.stem(w)
#Hello
#there
#Do
#you
#want
#fri
#with
#that