#This particular program will grab the main headlines of the financial blog Zero Hedge
#It will then print the file in the given file
#WON'T work for other blogs or sites!!!
#Zero Hedge is an English-language financial blog that aggregates news and presents editorial opinions from original and outside sources
from bs4 import BeautifulSoup;
import requests;
myUrl="http://www.zerohedge.com/";
req=requests.get(myUrl);
myFileHand=open("zerohedgenews.txt","w")
scrp=req.text;
soup=BeautifulSoup(scrp,"html.parser");
mySoup=soup.find_all('h2',{"class":"title teaser-title"});
val=str(mySoup);
newS=BeautifulSoup(val);
for i in newS.find_all('a'):
	myFileHand.write(str(i.text));
	myFileHand.write("\n");
myFileHand.close();
#Coded by Sridhar Cheebu
