import requests 
from bs4 import BeautifulSoup;

with open("sample.html","r") as f:
    html_doc=f.read()
soup = BeautifulSoup(html_doc,'html.parser')
print(soup.prettify(),type(soup.title.string))
print(soup.title.string)
print(soup.div)
print(soup.find_all("div"))
#print(soup.select("div.italic"))
print(soup.findAll(class_="italic"))
#i=0
#for parent in soup.find(class_="yojana").parents:
 #   i+=1
    #print(parent)
    #if(i==2):
     #   break

cont = soup.find(class_="container") 
print(cont)   