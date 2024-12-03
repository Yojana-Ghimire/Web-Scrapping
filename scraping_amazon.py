from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://www.amazon.com/s?k=laptops+on+sale+clearance+2024&crid=J0OOO1J6Z0CL&sprefix=lap%2Caps%2C503&ref=nb_sb_ss_ts-doa-p_2_3"

#Headers for request
Headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})

#HTTP request
webpage=requests.get(url,headers=Headers)
print(webpage)