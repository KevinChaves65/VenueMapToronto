import requests

KEY = '5PVPALFHGVS3C5PJANFS'
URL = 'https://www.eventbriteapi.com/v3/events/search'

headers = {
    'Authorization': f'Bearer {'5PVPALFHGVS3C5PJANFS'}',
}

params = {
    'location.address': 'Toronto',
    'expand': 'venue',
}

response = requests.get(URL, headers=headers, params=params)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())