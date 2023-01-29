import re
import json
from urllib.request import urlopen

url = "https://ipinfo.io/json"
answer = urlopen(url)
datas = json.load(answer)

ip = datas["ip"]
org = datas["org"]
city = datas["city"]
country = datas["country"]
region = datas["region"]
zone = datas["timezone"]

print("Details external IP: ")
print(f"IP: {ip}\nRegion: {region}\nCountry: {country}\nCity: {city}\nOrg.: {org}\nZone: {zone}")
