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
def get_price(soup):
    try:
        price=soup.find("span",attrs={'id':'priceblock_ourprice'}).string.strip()
    except AttributeError:
        try:
            #if there is some deal price
            price=soup.find("span",attrs={'id':'priceblock_dealprice'}).string.strip()    
        except:
            price = ""
    return price

#Function to extract product rating
def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()            
    except AttributeError:
        try:
            rating = soup.find("span",attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating=""
    return rating

#Function to extract number of user reviews
def get_review_count(soup):
    try:
        review_count=soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
    except AttributeError:
        review_count=""
    return review_count

#Function to extract Availability Status
def get_availability(soup):
    try:
       available= soup.find("div",attrs={'id':'availability'})
       available= available.find("span").string.strip()
    except:
        available = "Not Available"
    return available
                              

if __name__ == '__main__':
    #Headers for request
    Headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})
    
    #The Webpage URL
    url = "https://www.amazon.com/s?k=laptops+on+sale+clearance+2024&crid=J0OOO1J6Z0CL&sprefix=lap%2Caps%2C503&ref=nb_sb_ss_ts-doa-p_2_3"
    #HTTP request
    webpage=requests.get(url,headers=Headers)
    print(webpage)

    print(type(webpage.content))

    #Converting bytes into html format

    soup=BeautifulSoup(webpage.content, 'html.parser')

#Fetch links as list of Tag objects
    links = soup.find_all("a",attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    
    #Store the links
    links_list=[]
    
    #Loop for extracting links from Tag objects
    for link in links:
        links_list.append(link.get('href'))
    d = {'title':[],'price':[],'rating':[],'reviews':[],'availability':[]}
    
    #Loop for extracting product details from each link
    for link in links_list:
        new_webpage= requests.get("https://www.amazon.com" + link, headers=Headers)    
        new_soup = BeautifulSoup(new_webpage.content,"html.parser")
        
        #Function calls to display all necessary product information
        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['rating'].append(get_rating(new_soup))
        d['reviews'].append(get_review_count(new_soup))
        d['availability'].append(get_availability(new_soup))
    
    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df['title'].replace('',np.nan,inplace=True)
    amazon_df=amazon_df.dropna(subset=['title'])
    amazon_df.to_csv("amazon_data.csv",header=True,index=False)    
print(amazon_df)    