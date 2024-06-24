import requests
import json
res=requests.get("https://auditcity.io/api/data/e7eba98ba5b85dbc98b8def5319ef4c3")
print(res)
data=res.json()
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

with open('data.json', 'r') as f:
    data = json.load(f)
def read_json_file(data):
    with open('data.json', 'r') as f:
        data = json.load(f)
        return data

def analyze_data(data):
    print(data)

def main():
    filename = 'data.json'
    data = read_json_file(filename)
    if data:
        analyze_data(data)

if __name__ == '__main__':
    main()

print(data)
