import requests
import json
res=requests.get("https://auditcity.io/api/data/e7eba98ba5b85dbc98b8def5319ef4c3")
print(res)
data=res.json()
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

with open('data.json', 'r') as f:
    data = json.load(f)


print(data)