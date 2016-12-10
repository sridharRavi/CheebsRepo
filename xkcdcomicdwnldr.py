from bs4 import BeautifulSoup;
import requests;
import urllib2;
main_url="http://www.xkcd.com";
print "xkcd, sometimes styled XKCD, is a webcomic created by Randall Munroe. The comic's tagline describes it as 'A webcomic of romance, sarcasm, math, and language'"
print "The issue number ranges from 1 to 1768.New comics are added every three days";
urlInput=raw_input("Enter the issue number of xkcd you want to download");
mod_url=main_url+"/"+urlInput+"/";
req=requests.get(mod_url);
if(req.status_code==404):
	print "Oops ,try reloading the page!!"
scrp=req.text;
soup=BeautifulSoup(scrp,"html.parser");
mySoup=soup.find_all('div',{"id":"comic"});
val=str(mySoup);
newS=BeautifulSoup(val,"html.parser");
print "comic description"
for i in newS.find_all('img'):
    print i['title'];
    getVal=i['src'];
#print getVal;
reqObj=urllib2.urlopen("http:"+getVal);
myFileHand=open("xkcd %s.png" %(urlInput),"wb");
myFileHand.write(reqObj.read());
myFileHand.close();
#print mySoup;
#coded by Sridhar Cheebu ;-}


