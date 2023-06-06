from bs4 import BeautifulSoup
import requests
import asyncio
import aiohttp
import xlsxwriter
from aiohttp import ClientSession
import re
# https://qgold.com/pl/Jewelry-Rings-Adjustable


data =[['Товар', 'Цена']]
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


#async def get_page_data(session):
   # url = "https://qgold.com/pl/Jewelry-Rings-2·Stone-Rings"
    
    #async with session.get(url=url) as response:
       # response_text = await response.text()
       # soup = BeautifulSoup(await response_text, 'html.parser')
        #contain = soup.find('div', class_='products')
        #tovar2 = soup.css.select("span")
       # print(tovar2)
        
#async with session.get(url=url) as response:
 #   response_text = await response.text()
 #   soup = BeautifulSoup(await response_text, 'html.parser')
    #contain = soup.find('div', class_='products')
 #   tovar2 = soup.css.select("span")
 #   print(tovar2)


#def main():
#    asyncio.run(get_page_data(session=w))
#asyncio.run(get_page_data())

#if __name__ == "__main__":
#    main()


#tovar = soup.find_all("div", class_="row product-list")
# tovar = soup.find_all("div", class_="product-wrapper").find("span")
#dffr = soup.find("li", class_="item safari").find("span")
#tovar1 = soup1.find("div", class_="price-tag msrp")
#tovar1 = soup.find_all(class_=re.compile("ya-tr-span"))
#tovar1 = soup.find_all(string=re.compile("value"))
#tovar1 = soup.find_all('div', class_='price-tag msrp')
#tovar1 = soup.find_all(string=re.compile("value"))
tovar2 = soup.css.select("span")
#tovar = soup.find("li", class_="item safari").find("span")
data.append([tovar2])
# Добавление в ексель
wb = xlsxwriter.Workbook("dufuf.xlsx")
ws = wb.add_worksheet()
ws.write(data)
#with xlsxwriter.Workbook('rtrt.xlsx') as workbook:
 #   worksheet = workbook.add_worksheet()
#    worksheet.write_row(data)
 #   for row_num, info in enumerate(data):
 #       worksheet.write_row(row_num)
      

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

dict_params = { 1: response_detail['Product']['CountryOfOrigin'],
                2: response_detail['Product']['Size'],
                3: response_detail['Product']['MSRP'],
                4: response_detail['Product']['Image'],
                5: response_detail['Product']['AvailabilityText'],
                6: response_detail['Video']['FileName'],
                7: response_detail['Video']['Path'],
                8: response_detail['Specifications'][0]['Value'], # Product Type
                9: response_detail['Specifications'][1]['Value'],# Jewelry Type
                10: response_detail['Specifications'][2]['Value'],# Ring Type
                11: response_detail['Specifications'][3]['Value'],# Material: Primary - Color
                12: response_detail['Product']['CountryOfOrigin'], # Country of Origin
                13: response_detail['Specifications'][4]['Value'],# Metal
                14: response_detail['Specifications'][5]['Value'],# Material: Primary - Purity
                15: response_detail['Specifications'][6]['Value'],# Plating
                16: response_detail['Specifications'][7]['Value'], # Silver Tone
                17: response_detail['Specifications'][8]['Value'],# Sold By Unit
                18: response_detail['Specifications'][9]['Value'],# Band Width
                19: response_detail['Specifications'][10]['Value'], #Completeness
                20: response_detail['Specifications'][11]['Value'], #Finish
                21: response_detail['Specifications'][12]['Value'], #Item Weight U/M
                22: response_detail['Specifications'][13]['Value'], #Profile Type
                23: response_detail['Specifications'][14]['Value'], #Ring Top Length
                24: response_detail['Specifications'][15]['Value'], #Ring Top Width
                25: response_detail['Specifications'][16]['Value'], #Sizeable
                26: response_detail['Specifications'][17]['Value'], #Thickness
                27: response_detail['Specifications'][18]['Value'], #Stone Type
                28: response_detail['Specifications'][19]['Value'], #?
            }