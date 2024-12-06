from bs4 import BeautifulSoup
import requests
import pandas as pd
url="https://www.imdb.com/list/ls548439420/?ref_=hm_em00079_1_csegbest_movies_sm"

Headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})

webpage=requests.get(url,headers=Headers)

soup=BeautifulSoup(webpage.content,'html.parser')
title=soup.find('h3',class_='ipc-title__text').text
print(title)
rating=soup.find('span',attrs={'class':'ipc-rating-star--rating'}).text
print(rating)
release = soup.find('span',class_='sc-300a8231-7 eaXxft dli-title-metadata-item').text
print(release)
#duration=soup.find('span',class_='sc-300a8231-7 eaXxft dli-title-metadata-item').text
no_of_rating= soup.find('span',class_='ipc-rating-star--voteCount').text
print(no_of_rating)