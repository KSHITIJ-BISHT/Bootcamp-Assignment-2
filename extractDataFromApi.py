
#- collect data from those APIs
#- save the data in a file (json/txt file)

#Using exchange rates api
import requests
import json
import xmltodict
 
url = "https://api.exchangeratesapi.io/latest?base=USD"
 
response = requests.get(url)
data = response.text
#parsed = json.loads(data)
print(data)
with open('currency.json', 'w') as outfile:  
    json.dump(data, outfile)

print("----------------------------------------------------------------------------------------")
#Using animenewsnetwork api 
url = "https://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=4658"
 
response = requests.get(url)
data = response.text
parsed = xmltodict.parse(data)
print(parsed)
with open('anime.json', 'w') as outfile:  
    json.dump(parsed, outfile)

