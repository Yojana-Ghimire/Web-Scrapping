import requests
def FetchAndSaveToFile(url,path):
    r = requests.get(url)
    with open(path,"w", encoding="utf-8") as f:
        f.write(r.text)
    
url = "https://ioepas.edu.np/"
FetchAndSaveToFile(url, "data/ioepas.html")