import requests
from bs4 import BeautifulSoup
import pandas as pd

product_name = []
product_price = []
Link = []
for i in range(2,5):
    url = "https://www.flipkart.com/search?q=mobile+under+10%2C000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r = requests.get(url)
    soup=BeautifulSoup(r.text, "lxml")
    names = soup.find_all("div", class_ = "_4rR01T")
    for i in names:
        name = i.text
        product_name.append(name)
    prices=soup.find_all("div", class_ ="_30jeq3 _1_WHN1")
    for i in prices:
        price = i.text
        product_price.append(price)
df = pd.DataFrame({"Product Name": product_name, "Prices":product_price})
df.to_csv("E:/fkscrap1.csv")


