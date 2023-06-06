import requests
import json
import xlsxwriter
def perform_get_request(url):
    response = requests.get(url)
    return response.json()


def perform_post_request(url, data):
    response = requests.post(url, json=data)
    return response.json()

base_api_url='https://jewelers.services/productcore/api'

post_url = base_api_url + '/pl/Jewelry-Rings-2%C2%B7Stone-Rings'
post_data = {
        "filters": [{"key": "ItemsPerPage", "value": "360"}],
        "page": 1,
        "path": "Jewelry-Rings-2·Stone-Rings",
        "sortCode": 5
    }



#response = perform_post_request(post_url, post_data, f) #5 секунд
response = perform_post_request(post_url, post_data) #5 секунд
#print(response['LandingPageStyle']['Style'])LangindPageInfo
#print(response['LangindPageInfo']['LandingPageStyle'][0]['Style'])
#print(response['IndexedProducts']['Results'][0]['URLDescription'])
#get_url=base_api_url + "/pd/" + data['Descprtion'] + "/" + data['Style']
stil =(response['LangindPageInfo']['LandingPageStyle'][0]['Style']) #Стиль
disc = (response['IndexedProducts']['Results'][0]['URLDescription']) #Дескриптор
#print(response['LangindPageInfo']['LandingPageStyle'][0]['Style'])


get_url = base_api_url + "/pd/" + disc + "/" + stil
response_detail = perform_get_request(get_url)

#https://images.jewelers.services/0/Videos/QR6710.mp4

#print(response_detail['Product']['CountryOfOrigin'])
# print(type(response_detail['Product']['Size']))
# print(type(response_detail['Product']['MSRP']))
# #print(response_detail['LangindPageInfo'])
#print(type(response_detail[0]))
print(type(response_detail['Product']))
#print(response_detail['Product']['Status'])
#print(response_detail['Product']['Image'])
# print(response_detail['Product']['AvailabilityText'])
print(type(response_detail['Video']))
#print(response_detail.get('Video').get('FileName'))
# print(type(response_detail['Specifications'][0]['Value']))# Product Type
# print(response_detail['Specifications'][1]['Value'])# Jewelry Type
# print(response_detail['Specifications'][2]['Value'])# Ring Type
# print(response_detail['Specifications'][3]['Value'])# Material: Primary - Color
# print(response_detail['Product']['CountryOfOrigin']) # Country of Origin
# print(response_detail['Specifications'][4]['Value'])# Metal
# print(response_detail['Specifications'][5]['Value'])# Material: Primary - Purity
# print(response_detail['Specifications'][6]['Value'])# Plating
# print(response_detail['Specifications'][7]['Value']) # Silver Tone
# print(response_detail['Specifications'][8]['Value'])# Sold By Unit
# print(response_detail['Specifications'][9]['Value'])# Band Width
# print(response_detail['Specifications'][10]['Value']) #Completeness
# print(response_detail['Specifications'][11]['Value']) #Finish
# print(response_detail['Specifications'][12]['Value']) #Item Weight U/M
# print(response_detail['Specifications'][13]['Value']) #Profile Type
# print(response_detail['Specifications'][14]['Value']) #Ring Top Length
# print(response_detail['Specifications'][15]['Value']) #Ring Top Width
# print(response_detail['Specifications'][16]['Value']) #Sizeable
# print(response_detail['Specifications'][17]['Value']) #Thickness
# print(response_detail['Specifications'][18]['Value']) #Stone Type
# print(response_detail['Specifications'][19]['Value']) #?

# print(response['IndexedProducts']['Results'][0]['URLDescription'])

#print(response['IndexedProducts']['Results'][0]['URLDescription']
#still =(response['LangindPageInfo']['LandingPageStyle'][0]['Style'])
# rings = (response['IndexedProducts']['Results'])
# d = []
# data = [['Size', 'MSRP']]
# for ring in rings:
#     get_url = base_api_url + "/pd/" + ring['URLDescription'] + "/" + ring['Style']
#     response_detail = perform_get_request(get_url)


#     d.append(response_detail)
# ring = d[0]
# print(ring['Product']['Size'])
# # for i in ring:
#     de = (i['Product']['Size'])
#     gde = (i['Product']['MSRP'])
#     data.append([de, gde])
 #   for image in range(response2['Images']):
        #Обработка картинкой
        #Скачиваешь

  #       print(response['Product']['Sku'])
   #      print(response['Images'])


# with xlsxwriter.Workbook('rtrt1.xlsx') as workbook:
#     worksheet = workbook.add_worksheet()

#     for row_num, info in enumerate(data):
#         worksheet.write_row(row_num, 0, info)


def func(rings, key_1, key_2):
    list_empty1 = []
    for ring in list_url:
        value = ring[key_1]
        list_empty1.append(value)
        list_empty2 = []

        for ring1 in (list(list_empty1)):
            if ring1 != None:
                value1 = ring1[key_2] 
                list_empty2.append(value1)
            else:
                list_empty2.append('None')