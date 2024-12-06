links = soup.find_all("a",attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
link=links[0].get('href')
product_list="https://amazon.com"+link
