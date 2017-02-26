#Lemmatizing is mainly used to return a much better form of the root or stem of a word. The returned word may be the singular form or might even be a synonym for the required word
from nltk.stem import WordNetLemmatizer
wd=WordNetLemmatizer();
print (wd.lemmatize("Good"))
print (wd.lemmatize("Better",pos="a"))#the default Part of Speech parameter is Noun
print (wd.lemmatize("Mice"))
print (wd.lemmatize("Boys"))
print(wd.lemmatize("Geese"))

#Good
#Better
#Mice
#Boys
#Goose