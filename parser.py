import requests

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

#response = perform_post_request(post_url, post_data)
#print(response)

get_url=base_api_url + "/pd/" + "Sterling-Silver-Rhodium-plated-CZ-Two-Stone-Polished-Ring/QR6713-6"
#get_url=base_api_url + "/pd/" + "<Description>/<Style>"

response = perform_get_request(get_url)
print(response)
