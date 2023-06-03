from bs4 import BeautifulSoup
import requests
# https://qgold.com/pl/Jewelry-Rings-Adjustable

url = 'https://qgold.com/pl/Jewelry-Rings-2·Stone-Rings'
requests = requests.get(url)
soup = BeautifulSoup(requests.text, "html.parser")
# tovar = soup.find_all('ya-tr-span')
tovar = soup.find_all("div", class_="product-wrapper").find_all("span")
print(tovar)