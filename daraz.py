from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import pandas as pd
import psycopg2
from sqlalchemy import create_engine


options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--headless")  # Optional, run Chrome in headless mode
driver = webdriver.Chrome(options=options)
url="https://pages.daraz.com.np/wow/gcp/route/daraz/np/upr/router?hybrid=1&data_prefetch=true&prefetch_replace=1&at_iframe=1&wh_pid=%2Flazada%2Fchannel%2Fnp%2Fflashsale%2FeBQX2YfTXs&hide_h5_title=true&lzd_navbar_hidden=true&disable_pull_refresh=true&skuIds=169302458%2C150268528%2C179779770%2C129562539%2C172989829%2C164028435%2C164079325&spm=a2a0e.tm80335409.FlashSale.d_shopMore"
driver.get(url)

try:
    # Wait for the elements to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'flash-unit'))
    )
    # Proceed with scraping
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    product_containers = soup.find_all('div', class_='flash-unit')
    print(f"Found {len(product_containers)} product containers.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
    
#Transform the data

import re

products=[]   
# Extract product information
product_containers = soup.find_all('div', class_='flash-unit')
for idx, container in enumerate(product_containers, start=1):
    product_name = container.find('div', class_='sale-title')
    original_price=container.find('span', class_='origin-price-value')  
    discounted_price = container.find('div', class_='sale-price') 
    discount= container.find('span','discount')   
    
    products.append({
    "Name": product_name.text if product_name else 'N/A',
    "original_price": re.sub(r'Rs\.?\s*', '', original_price.text).replace(',', '').strip() if original_price else 'N/A',
    "discount": discount.text.replace('-','').strip() if discount else 'N/A',
    "Discounted_Price": re.sub(r'Rs\.?\s*','',discounted_price.text).replace(',','').strip() if discounted_price else 'N/A'
})



df = pd.DataFrame(products)


engine=create_engine("postgresql+psycopg2://postgres:python@localhost:5432/mydatabase") 
df.to_sql('daraz_products', engine, if_exists='replace',index=False)

print("Data has been successfully loaded into PostgreSQL!")



#Query  data from 'daraz_products' table 
query = "SELECT * FROM daraz_products;"
df_extracted = pd.read_sql(query, engine)
print(df_extracted)
