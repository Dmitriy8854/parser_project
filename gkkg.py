import requests
import json
import xlsxwriter
from pprint import pprint

def perform_get_request(url):
    response = requests.get(url)
    return response.json()


def perform_post_request(url, data):
    response = requests.post(url, json=data)
    return response.json()

base_api_url='https://jewelers.services/productcore/api'

post_url = base_api_url + '/pl/Jewelry-Rings-Adjustable'
post_data = {
        "filters": [{"key": "ItemsPerPage", "value": "360"}],
        "page": 1,
        "path": "Jewelry-Rings-Adjustable",
        "sortCode": 5
    }


response = perform_post_request(post_url, post_data) #5 секунд
transformer_url = (response['IndexedProducts']['Results'])
list_url = []

for url_detal in transformer_url:
    get_url = base_api_url + "/pd/" + url_detal['URLDescription'] + "/" + url_detal['Style']
    response_detail = perform_get_request(get_url)
    list_url.append(response_detail)#вся информация по кольцам

list_for_excel =[]

#print(list_url[0]['Specifications'][0]['Value'])
# print(list_url[0]['Specifications'][1]['Value'])
# print(list_url[0]['Specifications'][2]['Value'])
# print(list_url[0]['Specifications'][3]['Value'])
# print(list_url[0]['Specifications'][4]['Value'])
def func(rings, key_1, key_2):
    list_empty = []
    for ring in rings:
        value = ring.get(key_1).get(key_2)
        list_empty.append(value)
    return list_empty

# def func2(rings, number):
#     list_empty = []

#     for ring in rings:
#         #value = ring.get('Specifications')[number].get('Value')
#         value = ring[0]['Specifications'][number]['Value']
        
#         list_empty.append(value)
#     return list_empty
#https://images.jewelers.services/0/Videos/QR6710.mp4
#https://images.jewelers.services/qgrepo/QR6710.jpg

def func_image(rings, key_1, key_2):
    list_empty = []     
    base_url = 'https://images.jewelers.services/qgrepo/'

    for ring in rings:
        value = base_url + (ring[key_1][key_2])
        
        list_empty.append(value)
    return list_empty
# def func_video(rings, key_1, key_2):
#     list_empty = []     
#    # base_url = 'https://images.jewelers.services/0/Videos/'
# #     fg = '/mp4'
#     for ring in rings:
#         value = ring.get(key_1).get(key_2)
#         list_empty.append(value)
#     return list_empty 
#https://images.jewelers.services/0/Videos/QR6710.mp4


def func_video(rings, key_1, key_2):
    list_empty1 = []
    for ring in rings:
        value = ring[key_1]
        list_empty1.append(value)
        list_empty2 = []

        for ring1 in (list(list_empty1)):
            if ring1 != None:
                
                base_url_1 = 'https://images.jewelers.services/0/Videos/'
                value1 = base_url_1 + ring1[key_2]

                list_empty2.append(value1)
            else:
                list_empty2.append('None')
    return list_empty2


list_for_excel.append(func(list_url, 'Product', 'Size'))
list_for_excel.append(func(list_url, 'Product', 'MSRP'))
list_for_excel.append(func_image(list_url, 'Product', 'Image'))
list_for_excel.append(func(list_url, 'Product', 'AvailabilityText'))
list_for_excel.append(func_video(list_url, 'Video', 'FileName'))
list_for_excel.append(func(list_url, 'Product', 'CountryOfOrigin'))
# for i in range(20):
#     list_for_excel.append(func2(list_url, i))



# list_empty1 = []
# for ring in list_url:
#     value = ring['Video']
#     list_empty1.append(value)

# list_empty2 = []
# #print(list(list_empty1))
# for ring in (list(list_empty1)):
#     if ring != None:
#        value = ring['FileName'] 
#        list_empty2.append(value)
#     else:
#        list_empty2.append('None')


    #value = ring[3]
    #list_empty2.append(value)
#print(list_empty2)
#print(list_empty2)

# with xlsxwriter.Workbook('rtrt213.xlsx') as workbook:
#     worksheet = workbook.add_worksheet()

#     for row_num, info in enumerate(list_for_excel):
#         worksheet.write_row(row_num, 0, info)


# list_empty =[]
# dr = list_url['Specifications']
# for ring in dr:
#     g = (ring[9]['Value'])
#     if g != None:
#         list_empty.append(g)

# print(list_empty)


# dr = list_url['Specifications']
# for ring in dr:
#     print(ring)
#     if g != None:
#         list_empty.append(g)

# print(list_empty)







    #print(ring['Specifications'][9]['Value'])



# ring.get[0]('Specifications')[number].get('Value')
#     #value = ring.get('Specifications')[number].get('Value')
#         value = (ring[0])      
#         list_empty.append(value)
#pprint(list_empty)
#pprint(list_url[0])
#print(list_url['Specifications'][0]['Value'])