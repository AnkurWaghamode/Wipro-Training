import requests

url="https://api.restful-api.dev/objects"

response= requests.get(url)

print(response.status_code)
print(response.json())

url="https://api.restful-api.dev/objects?id=3&id=5&id=10"

response= requests.get(url)

print(response.status_code)
print(response.json())

url="https://api.restful-api.dev/objects/7"

response= requests.get(url)

print(response.status_code)
print(response.json())


posturl="https://api.restful-api.dev/objects"

body1={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

r1=requests.post(posturl,json=body1);
print("post status code",r1.status_code)
print(r1.json())

puturl="https://api.restful-api.dev/objects/ff8081819782e69e019be41bcf2f2f10"

body2={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}
r2=requests.put(puturl,json=body1);
print("put status code",r2.status_code)
print(r2.json())

patchurl="https://api.restful-api.dev/objects/ff8081819782e69e019be41bcf2f2f10"

body3={
   "name": "Apple MacBook Pro 16 (Updated Name)"
}
r3=requests.put(puturl,json=body1);
print("patch status code",r3.status_code)
print(r3.json())

delete_url = f"https://api.restful-api.dev/objects/ff8081819782e69e019be41bcf2f2f10"

delete_response = requests.delete(delete_url)

print("Status Code:", delete_response.status_code)
print("Response:", delete_response.json())



