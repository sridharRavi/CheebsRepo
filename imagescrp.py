#simple python program to download images from a web page!!
from bs4 import BeautifulSoup;
import requests;
import wget;
#please provide a complete url if possible like 'www.leonardodavinci.net'
myUrl=raw_input("enter the required url");
mod_url="http://"+myUrl
req=requests.get(mod_url);
scrp=req.text;
val=1;
newFileHand=open("imgtext.txt","wb");
soup=BeautifulSoup(scrp,"html.parser");
for i in soup.find_all('img'):
    newVal=mod_url+"/"+i.get('src');
    wget.download(newVal);
    newFileHand.write("\n".join(newVal));
newFileHand.close();

#coded by Sridhar Cheebu
#The resultant file will contain the separate image links
#The download will occur in the working directory where you downloaded this file