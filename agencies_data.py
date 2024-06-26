import requests
import json

res=requests.get("https://auditcity.io/api/data/e7eba98ba5b85dbc98b8def5319ef4c3")
class MyClass:
    def __init__(self):
        self.data = None

    def get_request(self):
        self.data = "Data fetched from request"
        print("Request executed")

    def process_data(self):
        if self.data:
            print("Processing data:", self.data)
        else:
            print("No data to process")

def read_json_file(data):
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"File '{data.json}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from '{data.json}': {e}")
        return None
def analyze_data(data):
    if data:
        print("Analyzing JSON data:")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("No data to analyze.")

def main():
    filename = 'data.json'
    data = read_json_file(filename)

if __name__ == '__main__':
    main()
    instance = MyClass()
    instance.get_request()
    instance.process_data()
