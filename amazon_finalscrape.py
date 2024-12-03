from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

#Function to extract Product Title
def get_title(soup):
    try:
        #Outer Tag Object
        title=soup.find("span", attrs={'id':'productTitle'})
        
        #Inner NavigatableString Object
        title_value=title.text
        
        #Title as string value
        title_string=title_value.strip()
    except AttributeError:
        title_string=""
    
    return title_string

#Function to extract Product Price
