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


response = perform_post_request(post_url, post_data) #5 секунд
transformer_url = (response['IndexedProducts']['Results'])
list_url = []

for url_detal in transformer_url:
    get_url = base_api_url + "/pd/" + url_detal['URLDescription'] + "/" + url_detal['Style']
    response_detail = perform_get_request(get_url)
    list_url.append(response_detail)#вся информация по кольцам


def func(rings, key_1, key_2):
    list_empty = []
    for ring in rings:
        value = ring.get(key_1).get(key_2)
        list_empty.append(value)
    return list_empty


def func2(rings, number):
    list_empty = []

    for ring in rings:
        value = ring.get('Specifications')[number].get('Value')
        
        list_empty.append(value)
    return list_empty


def func_image(rings, key_1, key_2):
    list_empty = []     
    base_url = 'https://images.jewelers.services/qgrepo/'

    for ring in rings:
        value = base_url + (ring[key_1][key_2])
        
        list_empty.append(value)
    return list_empty


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


list_for_excel =[]


list_for_excel.append(func(list_url, 'Product', 'Size'))
list_for_excel.append(func(list_url, 'Product', 'MSRP'))
list_for_excel.append(func_image(list_url, 'Product', 'Image'))
list_for_excel.append(func(list_url, 'Product', 'AvailabilityText'))
list_for_excel.append(func_video(list_url, 'Video', 'FileName'))
list_for_excel.append(func(list_url, 'Product', 'CountryOfOrigin'))
for i in range(20):
    list_for_excel.append(func2(list_url, i))


# Вывод данных в ексель
with xlsxwriter.Workbook('rtrt1.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, info in enumerate(list_for_excel):
        worksheet.write_row(row_num, 0, info)
