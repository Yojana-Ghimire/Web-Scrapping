from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://www.amazon.com/s?k=laptops+on+sale+clearance+2024&crid=J0OOO1J6Z0CL&sprefix=lap%2Caps%2C503&ref=nb_sb_ss_ts-doa-p_2_3"

#Headers for request
Headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})

#HTTP request
webpage=requests.get(url,headers=Headers)
print(webpage)

print(type(webpage.content))

#Converting bytes into html format

soup=BeautifulSoup(webpage.content, 'html.parser')

#Fetch links as list of Tag objects
links = soup.find_all("a",attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
link=links[0].get('href')
product_list="https://amazon.com"+link

new_webpage = requests.get(product_list,headers=Headers)

#Soup object containing all data
new_soup=BeautifulSoup(new_webpage.content, 'html.parser')

print(new_soup.find('span',attrs={"id":"productTitle"}).text.strip())
