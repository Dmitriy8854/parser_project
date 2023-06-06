import requests
import json

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
print(response)

#print(response['Products'])

for data in range(response.IndexedDocuments):
  
    #get_url=base_api_url + "/pd/" + "Sterling-Silver-Rhodium-plated-CZ-Two-Stone-Polished-Ring/QR6713-6"
    get_url=base_api_url + "/pd/" + data['Descprtion'] + "/" + data['Style']

    response2 = perform_get_request(get_url) #1 секунд
    # Decode JSON string into a Python object
    #data = response.json()
#WebPath
    #for image in range(response2['Images']):
        #Обработка картинкой
        #Скачиваешь

        print(response['Product']['Sku'])
        print(response['Images'])
    

rings = (response['IndexedProducts']['Results'])
d = []
data = [['Size', 'MSRP']]
for ring in rings:
    get_url = base_api_url + "/pd/" + ring['URLDescription'] + "/" + ring['Style']
    response_detail = perform_get_request(get_url)
    for image in range(response_detail['Product']):
        print(image['MSRP'])