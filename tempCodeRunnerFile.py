from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import pandas as pd

driver=webdriver.Chrome()
url="https://pages.daraz.com.np/wow/gcp/route/daraz/np/upr/router?hybrid=1&data_prefetch=true&prefetch_replace=1&at_iframe=1&wh_pid=%2Flazada%2Fchannel%2Fnp%2Fflashsale%2FeBQX2YfTXs&hide_h5_title=true&lzd_navbar_hidden=true&disable_pull_refresh=true&skuIds=169302458%2C150268528%2C179779770%2C129562539%2C172989829%2C164028435%2C164079325&spm=a2a0e.tm80335409.FlashSale.d_shopMore"
driver.get(url)

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
product_containers = soup.find_all('div', class_='flash-unit card-hover pull-left')
print(product_containers)