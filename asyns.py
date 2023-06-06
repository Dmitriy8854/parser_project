import asyncio
import aiohttp
import xlsxwriter
async def perform_get_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def perform_post_request(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            return await response.text()




# base_api_url='https://jewelers.services/productcore/api'

# post_url = base_api_url + '/pl/Jewelry-Rings-2%C2%B7Stone-Rings'
# post_data = {
#         "filters": [{"key": "ItemsPerPage", "value": "360"}],
#         "page": 1,
#         "path": "Jewelry-Rings-2·Stone-Rings",
#         "sortCode": 5
#     }


# response = perform_post_request(post_url, post_data) #5 секунд
# transformer_url = (response['IndexedProducts']['Results'])
# list_url = []

# for url_detal in transformer_url:
#     get_url = base_api_url + "/pd/" + url_detal['URLDescription'] + "/" + url_detal['Style']
#     response_detail = perform_get_request(get_url)
#     list_url.append(response_detail)#вся информация по кольцам

base_api_url='https://jewelers.services/productcore/api'



async def main():
 #  root_categories = ['https://jewelers.services/productcore/api/pl/Jewelry-Rings-2%C2%B7Stone-Rings']
    root_categories = ['https://jewelers.services/productcore/api/pl/Jewelry-Rings-2%C2%B7Stone-Rings']

 #   get_url = 'https://jsonplaceholder.typicode.com/posts/1'

    post_url = root_categories[0]
    post_data = {
        "filters": [{"key": "ItemsPerPage", "value": "360"}],
        "page": 1,
        "path": "Jewelry-Rings-2·Stone-Rings",
        "sortCode": 5
    }

    tasks = [
#        asyncio.create_task(perform_get_request(get_url)),
        asyncio.create_task(perform_post_request(post_url, data=post_data))
    ]
    results = await asyncio.gather(*tasks)
#    print(f"GET response: {results[0]}")
    print(f"POST response: {results[0]}")
    
    tasks2 = [
#        asyncio.create_task(perform_get_request(get_url)),
        asyncio.create_task(perform_get_request(post_url))
    ]

    results = await asyncio.gather(*tasks2)
  


transformer_url = (results['IndexedProducts']['Results'])
    
list_url = []

for url_detal in transformer_url:
    get_url = base_api_url + "/pd/" + url_detal['URLDescription'] + "/" + url_detal['Style']
    response_detail = perform_get_request(get_url)
    list_url.append(response_detail)#вся информация по кольцам


async def func(rings, key_1, key_2):
    list_empty = []
    for ring in rings:
        value = ring.get(key_1).get(key_2)
        list_empty.append(value)
    return list_empty


async def func2(rings, number):
    list_empty = []

    for ring in rings:
        value = ring.get('Specifications')[number].get('Value')
            
        list_empty.append(value)
    return list_empty


async def func_image(rings, key_1, key_2):
    list_empty = []     
    base_url = 'https://images.jewelers.services/qgrepo/'

    for ring in rings:
        value = base_url + (ring[key_1][key_2])
            
        list_empty.append(value)
    return list_empty


async def func_video(rings, key_1, key_2):
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

task_3 = [
    list_for_excel.append(asyncio.create_task(func(list_url, 'Product', 'Size'))),
    list_for_excel.append(asyncio.create_task(func(list_url, 'Product', 'MSRP'))),
    list_for_excel.append(asyncio.create_task(func_image(list_url, 'Product', 'Image'))),
    list_for_excel.append(asyncio.create_task(func(list_url, 'Product', 'AvailabilityText'))),
    list_for_excel.append(asyncio.create_task(func_video(list_url, 'Video', 'FileName'))),
    list_for_excel.append(asyncio.create_task(func(list_url, 'Product', 'CountryOfOrigin'))),
    for i in range(20):
        list_for_excel.append(asyncio.create_task(func2(list_url, i)))

]
    # Вывод данных в ексель
with xlsxwriter.Workbook('rtrt1.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, info in enumerate(list_for_excel):
        worksheet.write_row(row_num, 0, info)



if __name__ == '__main__':
    asyncio.run(main())