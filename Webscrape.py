import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.com/s?k=iphone&refresh=1"

with open('Amazon.html', 'r', encoding='utf-8') as f:
    html = f.read()

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

product_divs = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-vgvrqzb9qhw04209lhl7wx6b1b s-latency-cf-section puis-card-border')

Product_Name = []
Product_Price = []
Product_Review = []

for div in product_divs:
    product_name_elem = div.find('span', class_='a-size-medium a-color-base a-text-normal')
    if product_name_elem:
        Product_Name.append(product_name_elem.text.strip())
    else:
        Product_Name.append('')

    product_price_elem = div.find('span', class_='a-price-whole')
    if product_price_elem:
        Product_Price.append(product_price_elem.text.strip())
    else:
        Product_Price.append('')

    product_review_elem = div.find('i', class_='a-icon a-icon-star-small a-star-small-4 aok-align-bottom')
    if product_review_elem:
        Product_Review.append(product_review_elem.text.strip())
    else:
        Product_Review.append('')


for i in range(len(Product_Name)):
    print(f"Product Name: {Product_Name[i]}")
    print(f"Product Price: {Product_Price[i]}")
    print(f"Product Review: {Product_Review[i]}")
    print()

import sqlite3
import requests
from bs4 import BeautifulSoup

conn = sqlite3.connect('amazon_products.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Products
             (Name TEXT, Price TEXT, Review TEXT)''')

for i in range(len(Product_Name)):
    c.execute("INSERT INTO Products (Name, Price, Review) VALUES (?, ?, ?)",
              (Product_Name[i], Product_Price[i], Product_Review[i]))
    
conn.commit()
conn.close()

