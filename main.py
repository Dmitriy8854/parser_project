from bs4 import BeautifulSoup
import requests
import asyncio
import aiohttp
import re
# https://qgold.com/pl/Jewelry-Rings-Adjustable

url = 'https://qgold.com/pl/Jewelry-Rings-2·Stone-Rings'
#r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"})
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")
# print(soup)
url1 = 'https://qgold.com/pd/sterling-silver-rhodium-plated-cz-two-stone-round-bypass-ring/qr6709-6'
request1 = requests.get(url1)
soup1 = BeautifulSoup(request1.text, "html.parser")
tovar1 = soup.find_all('div', class_="row product-list")
#print(tovar1)

#async def get_page_data(session):
    
 #   async with session.post('https://qgold.com/pl/Jewelry-Rings-2·Stone-Rings') as response:
  #      soup = BeautifulSoup(await response, 'html.parser')
        #contain = soup.find('div', class_='products')
  #      tovar2 = soup.css.select("span")
#        print(tovar2)
        
#get_page_data(session)


async def get_page_data(session):
    url = "https://qgold.com/pl/Jewelry-Rings-2·Stone-Rings"
    
    async with session.get(url=url) as response:
        response_text = await response.text()
        soup = BeautifulSoup(await response_text, 'html.parser')
        #contain = soup.find('div', class_='products')
        tovar2 = soup.css.select("span")
        print(tovar2)
        
#def main():
#    asyncio.run(get_page_data(session=w))
asyncio.run(get_page_data())

#if __name__ == "__main__":
#    main()


#tovar = soup.find_all("div", class_="row product-list")
# tovar = soup.find_all("div", class_="product-wrapper").find("span")
#tovar = soup.find("li", class_="item safari").find("span")
#tovar1 = soup1.find("div", class_="price-tag msrp")
#tovar1 = soup.find_all(class_=re.compile("ya-tr-span"))
#tovar1 = soup.find_all(string=re.compile("value"))
#tovar1 = soup.find_all('div', class_='price-tag msrp')
#tovar1 = soup.find_all(string=re.compile("value"))
#tovar = soup.css.select("span")
#tovar = soup.find("li", class_="item safari").find("span")



#d =[]
#for i in tovar:
#    f = i.find("span")
#    d.append(f)
#print(tovar)

#print(tovar)

#def fromSoup():
   # url = 'https://qgold.com/pl/Jewelry-Rings-2·Stone-Rings'
   # request = requests.get(url)
   # soup = BeautifulSoup(request.text, "html.parser")

  #  for link in soup.find_all('ngcontent-jag-c83'):
  #      print(link.get('href'))    

#fromSoup()

#https://question-it.com/questions/1644455/beautifulsoup-ne-mozhet-najti-tegi-vnutri-bloka-xml