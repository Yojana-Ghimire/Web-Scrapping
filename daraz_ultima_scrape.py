from bs4 import BeautifulSoup
import requests
import pandas as pd
url="https://www.jeevee.com/product-campaigns/jeevee-focused-products-670"
Headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})

#HTTP requests
web=requests.get(url,headers=Headers)
print(web)
soup=BeautifulSoup(web.content,'html.parser')

# URL containing product links
links = soup.find("div",class_='text-xs sm:text-lg leading-[1.1] sm:leading-[1.2] text-2-clamp h-7 sm:h-[44px] mb-1').text
print(links)