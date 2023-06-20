import requests

headers_a = {'accept': 'application/json'}
petID = '333'
data_my = {
  "id": 333,
  "category": {
    "id": 333,
    "name": "esgcategory"
  },
  "name": "esg",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 333,
      "name": "esgtags"
    }
  ],
  "status": "available"
}
data_new = {
  "id": 333,
  "category": {
    "id": 333,
    "name": "ESGCATEDORY"
  },
  "name": "ESG_NAME",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 333,
      "name": "ESG_TAGS"
    }
  ],
  "status": "sold"
}

# POST request
res = requests.post("https://petstore.swagger.io/v2/pet", headers = headers_a, json = data_my)
print('--- POST request code --- ', res.status_code)
print('--- POST request --- ', res.json())

# PUT request
res = requests.put("https://petstore.swagger.io/v2/pet", headers = headers_a, json = data_new)
print('\n--- PUT request --- ', res.status_code)
print('--- PUT request code --- ', res.json())

# GET request
res = requests.get(f"https://petstore.swagger.io/v2/pet/{petID}", headers = headers_a)
print('\n--- GET request --- ', res.status_code)
print('--- GET request code --- ', res.json())

# DELETE request
res = requests.get(f"https://petstore.swagger.io/v2/pet/{petID}", headers = headers_a)
print('\n--- DELETE request code --- ', res.status_code)
print('--- DELETE request --- ', res.json())